Title: Migration du blog vers le VPS hackera
Date: 2018-11-09 22:30
Slug: migration-blog-vps
Author: Nicolas Drufin
category: web
Summary: La nouvelle stack technique ...

Le blog n'a pas duré bien longtemps sur RaspberryPi, notamment parce que 
ce dernier a rapidement trouvé une autre utilité en devenant une station
domotique à part entière qui pourra faire l'objet d'un autre article.

La nouvelle stack technique est désormais la suivante.

## Le CMS Pelican

Celui ci ne change pas, toujours le même système de génération statique des 
articles.

## Le serveur Nginx

Petite nouveauté ici, on monte en gamme avec un [nginx](https://www.nginx.com/) 
qui sert désormais tous les sites du VPS. Niveau configuration, rien de bien 
compliqué : on redirige directement le paramètre `root` sur le dossier `output` 
généré automatiquement par Pelican.

On se fait aussi plaisir en passant le site en SSL avec le 
[certbot](https://certbot.eff.org/) de [Let's Encrypt](https://letsencrypt.org/).

## Hebergement OVH

Plus d'auto-hébergement ici, on veut de la disponibilité, donc direction un VPS 
OVH. Changement d'url également, puisque vous retrouvez ce blog sous le domaine 
(blog.hackera.fr)[https://blog.hackera.fr]. 

La prochaine étape de ce blog est de pouvoir automatiser la génération des articles 
directement sur l'écoute des commits entrants, peut être avec un gitpubsub.

