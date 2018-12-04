Title: S'abonner aux commits avec Git pub-sub
Date: 2018-12-04 23:07
Slug: abonnement-commit-gitpubsub
Author: Nicolas Drufin
category: git
Summary: Dans l'ère des webhooks qui sont maintenant sur toutes les forges git qui se respectent, il y a encore des mécanismes basiques mais redoutablement efficace qui subsistent...

Dans l'ère des webhooks qui sont maintenant sur toutes les forges git qui se respectent, il y a encore des mécanismes basiques mais redoutablement efficace qui subsistent : [Publish-subscribe](https://fr.wikipedia.org/wiki/Publish-subscribe).

## Le principe du Publish-subscribe appliqué à Git

Le but de ce mécanisme consiste à mettre en place un flux dans lequel des *éditeurs* vont envoyer des informations et des *abonnés* vont choisir de traiter où non cette information. Dans notre cas avec Git, les *éditeurs* seront des hooks et les *abonnés* des services permettant de mettre à jour un déploiement.

## Installation de gitpubsub serveur

Plusieurs mécanismes de *Publish-subscribe* peuvent faire l'affaire, ici j'ai fait le choix d'utiliser [gitpubsub](https://github.com/Starfight/gitpubsub), un projet de [Daniel Gruno](https://github.com/Humbedooh). Le projet étant un vieux de quelques années, j'ai pris le soin de le forker pour le remettre un peu au goût du jour.

La première chose à faire est d'installer les dépendances en Lua :

```
$ apt install luarocks
$ luarocks install luasocket luajson luafilesystem penlight
```

Pour la configuration, on copie le fichier d'exemple qui sert principalement à définir sur l'interface réseau :

```
$ cp gitpubsub.cfg.sample gitpubsub.cfg
```

Ensuite, on peut simplement démarrer le fichier `gitpubsub.lua` avec un service. Pour **systemd**, on crée un service dans `/etc/systemd/system/gitpubsub-server.service` :

```
[Unit]
Description=Gitpubsub server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/gitpubsub
ExecStart=/usr/bin/lua gitpubsub.lua
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

On recharge ensuite le démon de systemd et on démarre le service :

```
$ systemctl daemon-reload
$ systemctl start gitpubsub-server
```

On peut déjà tester le service en lançant un `curl` sur l'adresse http://localhost:2069/json, ce qui nous donne quelque chose de cet ordre là :

```
$ curl http://localhost:2069/json
{"stillalive": 1543958509.098668}
```

Pour le hook, j'ai préféré utiliser celui en python. Celui-ci nécessite qu'on installe [httplib2](https://pypi.org/project/httplib2/) avec `pip` ou `apt` :

```
$ apt install python-httplib2
```

On peut mettre ensuite le hook `post_receive.py` directement dans le dossier `hook/post-receive.d` du dépôt git. Pour ma part, je me suis servi du [dossier de template de git](https://git-scm.com/docs/git-init#_template_directory) pour créer un lien symbolique. Cela permet à **Gitea** de créer un dossier de hooks contenant par défaut mon hook pour **gitpubsub** tout en pouvant le modifier globalement après coup si besoin.  

On peut à nouveau tester en faisant un commit :

```
$ curl http://localhost:2069/json
{"commit": {"files": ["test.txt"], "hash": "0f59df9d7c7d2876b5246cbaab49a07767061927", "repository": "git", "author": "John doe", "project": "test.git", "ref": "refs/heads/master", "email": "john@doe.com"}}
```

## Installation de gitpubsub client

La partie client a pour but d'être légère et facile à mettre en oeuvre. Un exemple est par ailleurs disponible dans le dépôt sous le nom [subscriber.sh](https://github.com/Starfight/gitpubsub/blob/master/subscriber.sh). 

Pour aller plus loin, j'ai créé également un service capable d'écouter et de mettre à jour plusieurs dépôts git grâce à **gitpubsub** : [gitpubsub-subscriber](https://apps.hackera.fr/gitea/gitpubsub/gitpubsub-subscriber).

L'outil est entièrement en bash et ne nécessite aucune dépendance. La configuration se fait via un fichier `config.ini` de ce type :

```
URL="http://localhost:2069/json"
BRANCH="master"
SCRIPT="script.sh"

[myproject]
BRANCH="test"
PATH="/srv/myproject"

[myproject2]
PROJECT="superproject"
SCRIPT="update.sh"
```

Le champ `URL` et le champ `PATH` pour chaque projet sont les seuls indispensables. Le comportement par défaut du script est d'écouter l'url de **gitpubsub** et de mettre à jour les dépôts git listés dans ce fichier dès qu'une notification de commit correspondant au dépôt sur la branche *master* est lue. On peut surcharger ce comportement globalement ou dans chaque dépôt, et ajouter l'exécution d'un script après mise à jour.

Une fois la configuration définie, on peut mettre en place le service [gitpubsub-subscriber.service](https://apps.hackera.fr/gitea/gitpubsub/gitpubsub-subscriber/src/branch/master/gitpubsub-subscriber.service) de la même façon que le service **gitpubsub** serveur.

Pour débugger les éventuels problèmes, on peut utiliser directement **journald** de la façon suivante :

```
$ journalctl -u gitpubsub-subscriber
```

## Conclusion et évolution

**Gitpubsub** permet d'avoir un moyen simple de maintenir automatiquement à jour des déploiements de dépôts git. Ce n'est pas à vocation d'être une solution universelle mais à l'image du principe KISS : une solution légère pour des petits projets. 

Le but pour moi est maintenant de pouvoir embarquer tout cela dans des paquets installables facilement, un pour la partie serveur et un pour la partie client.   
