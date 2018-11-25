Title: Mettre en place la signature DKIM avec Yunohost
Date: 2018-11-25 21:58
Slug: signature-dkim-avec-yunohost
Author: Nicolas Drufin
category: yunohost
Summary: Comment mettre en place la signature DKIM en tout simplicité ... 

À défaut d'avoir un serveur local digne de ce nom (et surtout d'un routeur fiable de mon FAI), je profite de mon VPS pour tester [Yunohost](https://yunohost.org), une solution d'auto-hébergement parée pour mener de front le combat contre les GAFAM.

Dans cet article, je vous fais grâce de mon combat quelque peu acharné pour comprendre l'intégration de la signature DKIM sur les courriels pour vous donner les informations qui m'ont manqué. 

## L'origine du problème 

Tout commence par un mail qui atterrit dans les spams et [une configuration du DNS coté Yunohost](https://yunohost.org/#/dns_config_fr) qui s'avère un peu avare en explications pour moi. Le problème se pose surtout pour l'enregistrement `mail._domainkey` qui nécessite une clé rsa à renseigner.

## Intégration DKIM façon Yunohost

Yunohost utilise [rspamd](https://www.rspamd.com/) pour son filtre anti-spam, mais aussi pour son module DKIM. Les clés sont générées automatiquement dans `/etc/dkim`. Pour chaque domaine, vous aurez deux fichiers :

* `example.com.mail.key` : la clé privée, à ne pas divulguer
* `example.com.mail.txt` : l'enregistrement DNS contenant la clé publique

## Enregistrement des entrées DNS chez OVH

Le contenu du fichier `example.com.mail.txt` est tout ce qu'on a besoin pour la suite. On peut directement copier/coller le contenu dans le *mode textuel* (attention à ne pas oublier le saut de ligne à la fin, la moulinette d'OVH peut vous retourner une erreur s'il est omis). On peut aussi faire la transcription en ajoutant une entrée de type **DKIM**.

## Test final

Une fois l'enregistrement effectué, on peut faire un test en envoyant un mail à l'adresse check-auth@verifier.port25.com. Si votre résultat ressemble à ça, c'est gagné : 
```
==========================================================
Summary of Results
==========================================================
SPF check:          pass
"iprev" check:      pass
DKIM check:         pass
SpamAssassin check: ham
```
