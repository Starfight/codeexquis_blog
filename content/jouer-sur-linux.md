Title: Jouer sur Linux
Date: 2019-08-21 23:35
Slug: jouer-sur-linux
Author: Nicolas Drufin
category: game
Summary: Avec l'achat d'un nouveau pc en avril, je suis passé au tout Linux pour la première fois. Plus de dual-boot Windows pour jouer ou procrastiner, l'occasion de revenir sur ces 4 derniers mois où je n'ai pas arrêté le gaming.

Mon vieux triple coeur AMD se faisant vieux après ses 10 ans de loyaux services, j'ai décidé d'investir dans un pc gamer moyenne gamme, tout en restant dans le thème AMD. Pour la configuration, je suis allé piocher dans https://pcpartpicker.com/, voici un apercu du `screenfetch` ci-dessous :
```
 ██████████████████  ████████     ndrufin@nightfall
 ██████████████████  ████████     OS: Manjaro 18.0.4 Illyria
 ██████████████████  ████████     Kernel: x86_64 Linux 4.19.62-1-MANJARO
 ██████████████████  ████████     Uptime: 2h 44m
 ████████            ████████     Packages: 1246
 ████████  ████████  ████████     Shell: bash 5.0.7
 ████████  ████████  ████████     Resolution: 1920x1080
 ████████  ████████  ████████     DE: KDE 5.60.0 / Plasma 5.16.3
 ████████  ████████  ████████     WM: KWin
 ████████  ████████  ████████     GTK Theme: Adwaita [GTK2/3]
 ████████  ████████  ████████     Icon Theme: breeze
 ████████  ████████  ████████     Font: Noto Sans Regular
 ████████  ████████  ████████     CPU: AMD Ryzen 5 2600 Six-Core @ 12x 3.4GHz
 ████████  ████████  ████████     GPU: Radeon RX 580 Series (POLARIS10, DRM 3.27.0, 4.19.62-1-MANJARO, LLVM 8.0.1)
                                  RAM: 3217MiB / 16035MiB
```

Le choix AMD versus Intel révèle parfois de la religion pour certains puristes. Pour moi, je trouve AMD largement suffisant pour du moyenne gamme et Intel trop cher pour ce que j'en ferai. Néanmoins j'approuve l'utilisation de processeurs Intel dans des pc portables ou dans des serveurs.

## Le choix de l'OS

Sur mon ancien pc, j'avais opté pour Ubuntu. C'était la distribution que j'utilisais au travail, cela me permettait de me former en travaillant et d'avoir du support auprès de mes collègues si besoin. Installée en LTS 16.04, je suis passé en 18.04 quelques mois après sa sortie. 

Néanmoins plusieurs choses ont commencé à me déplaire. Premièrement, le fait d'avoir basculé sur Gnome m'a fait prendre conscience de la lourdeur du DE. De plus celui-ci me plaisait moins ergonomiquement et visuellement, d'autant que mon pc avait beaucoup plus de mal avec les animations. Deuxièmement, le fait de devoir jongler entre snap et apt, même si je ne considère que chacun à un sens, rendait la gestion des installations plus complexes.

J'ai donc été voir les distributions concurrentes et je suis tombé sur [Pop!_OS](https://system76.com/pop) et [Manjaro](https://manjaro.org/). Avec le `screenfetch` vous savez déjà que je suis tombé sous le charme de Manjaro. L'avantage de cette dernière est qu'elle est dérivée d'un Arch Linux, permettant entre autre de bénéficier de [AUR](https://aur.archlinux.org/). Le deuxième avantage de dérivé de Arch à mon sens est de bénéficier de sa communauté, qui est de façon générale plus bidouilleuse que celle d'Ubuntu. Pour le DE, j'ai opté pour KDE, qui me faisait dééjà de l'oeil il y a quelques années mais qui souffrait d'instabilités (KDE Plasma, magnifique mais souvent complètement freezé), c'est désormais de l'histoire ancienne avec celui-ci.

Pop!_OS n'est pas moins intéressante pour autant, mais je n'ai pas pris le temps de la tester davantage, elle semblait corriger des problèmes que j'avais rencontré sur Ubuntu, mais l'aspect découverte en moins puisqu'il s'agit encore d'une Debian.  

## Steam et Proton

Incontournable dans le domaine, la plateforme Steam a une bibliothèque de jeux bien fournie compatible Linux nativement. Je n'ai jamais fait spécialement attention à acheter des jeux compatibles auparavant, et j'ai actuellement 56 jeux sur 83 qui peuvent fonctionner nativement. C'est déjà un bon score mais on peut aller beaucoup plus loin avec [Proton](https://www.protondb.com/), qui permet de faire fonctionner des jeux compatible Windows sur Linux. 

*[DE]: Desktop Environment