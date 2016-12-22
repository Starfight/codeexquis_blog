Title: Lancement du blog Code Exquis 
Date: 2016-12-23 23:11
Slug: lancement-blog-code-exquis
Author: Nicolas Drufin
category: web
Summary: Mon but initial était de monter un blog léger, facilement supportable par le rasberry pi...

Mon but initial était de monter un blog léger, facilement supportable par le rasberry pi. En m'inspirant de l'[article de Gary Hall](http://garyhall.org.uk/fast-blog-for-raspberry-pi.html) j'ai pu rapidement monter une stack composé d'un serveur Lighttpd et d'un blog créé à partir d'un cms léger en python nommé [Pelican](http://pelican.readthedocs.io/). Le tout étant hébergé en local à travers un routeur classique : une box sfr.

## Le serveur Lighttpd

Il n'y a pas grand chose à attendre de ce coté là, c'est un serveur simplissime pour héberger du contenu statique, et nous verrons par la suite que c'est idéal pour Pelican. Je n'ai pas eu à configurer le serveur :  on l'installe, on lance et tout fonctionne. On pourra éventuellement prendre 5-10 minutes pour une *configuration* plus poussée [ici](http://redmine.lighttpd.net/projects/lighttpd/wiki/TutorialConfiguration).

## Le CMS Pelican

Ce CMS à pour principe la génération statique de pages à partir de contenu simple à écrire. Par exemple cet article est complètement écrit en [Markdown](https://guides.github.com/features/mastering-markdown/). Ce qui m'a intéressé surtout avec Pelican se compte en 3 points :

1. l'absence de gestion de base de données
2. la génération des pages, plugins et thèmes en python
3. la grande variété de styles pour créer du contenu technique en informatique

Le code de ce blog est entièrement hebergé sur GitHub sur le projet [codeexquis_blog](https://github.com/Starfight/codeexquis_blog). J'ai pris soin de rajouter quelques extras à ce projet, notamment le thème [Flex](https://github.com/alexandrevicenzi/Flex) par Alexandre Vicenzi ainsi qu'un script de déployement pour envoyer directement le contenu statique depuis ma machine de développement vers le serveur raspberry pi.

## L'hébergement

L'hébergement étant assuré par le raspberry pi directement chez moi, j'ai pris soin de suivre [la documentation d'assistance SFR](http://assistance.sfr.fr/internet-et-box/box-nb6/heberger-site-box.html). Du moins en partie puisque depuis quelques années DynDNS est devenu un service payant, dont l'ergonomie du site laisse par ailleurs à désirer. Je me suis donc orienté vers [No-IP](https://www.noip.com/) (mais vous trouverez d'autres références [ici](https://korben.info/clone-dyndns-remplacer.html)) pour obtenir un DNS dynamique, ce qui explique l'url de ce site pour le moment. 