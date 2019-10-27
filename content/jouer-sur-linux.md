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

Néanmoins plusieurs choses ont commencé à me déplaire. Premièrement, le fait d'avoir basculé sur l'environnement de bureau Gnome m'a fait prendre conscience de la lourdeur de ce dernier. De plus celui-ci me plaisait moins sur le plan ergonomie et design, d'autant que mon pc avait beaucoup plus de mal avec les animations. Deuxièmement, le fait de devoir jongler entre snap et apt, même si snap est un parti pris qui peut être intéressant, rendait la gestion des installations plus complexes.

J'ai donc été voir les distributions concurrentes et je suis tombé sur [Pop!_OS](https://system76.com/pop) et [Manjaro](https://manjaro.org/). Avec le `screenfetch` vous savez déjà que je suis tombé sous le charme de Manjaro. L'avantage de cette dernière est qu'elle est dérivée d'un Arch Linux, permettant entre autre de bénéficier de [AUR](https://aur.archlinux.org/). Le deuxième avantage de dérivé de Arch à mon sens est de bénéficier de sa communauté, qui est de façon générale plus bidouilleuse que celle d'Ubuntu. Pour le DE, j'ai opté pour KDE, qui me faisait déjà de l'oeil il y a quelques années mais qui souffrait d'instabilités (KDE Plasma, magnifique mais souvent complètement freezé), c'est désormais de l'histoire ancienne avec celui-ci.

Pop!_OS n'est pas moins intéressante pour autant, mais je n'ai pas pris le temps de la tester davantage, elle semblait corriger des problèmes que j'avais rencontré sur Ubuntu, mais l'aspect découverte en moins puisqu'il s'agit encore d'une Debian. A noter également que Manjaro ne suit pas la fréquence de mise à jour de Arch Linux, ce qui peut déplaire les puristes mais ce qui permet également de s'assurer d'éventuels défauts ou régressions.

## Steam et Proton

Incontournable dans le domaine, la plateforme Steam a une bibliothèque de jeux bien fournie compatible Linux nativement. Je n'ai jamais fait spécialement attention à acheter des jeux compatibles auparavant, et j'ai actuellement 56 jeux sur 83 qui peuvent fonctionner nativement. C'est déjà un bon score mais on peut aller beaucoup plus loin avec [Proton](https://www.protondb.com/), qui permet de faire fonctionner des jeux compatible Windows sur Linux. 


## Wine pour la ligue des légendes 

Pour les jeux non nativement compatible qui ne rentrent pas dans le cadre Steam/Proton, il existe un dernier rempart contre les jeux Windows : Wine. Wine est connu depuis longtemps pour assurer au mieux la compatibilité des logiciels Windows, c'est également le cas pour certains jeux comme le célèbre MOBA League of Legends.

La manipulation dans ce cas est un peu plus délicate, on construit un environnement Windows virtuel où les programmes vont tourner dans une instance de Wine. Dans le cas de jeux qui évoluent constamment comme le MOBA de Riot, le code de Wine doit évoluer sans cesse à chaque mise à jour majeure, ce qui impose de parfois devoir compiler soit même le code source pour avoir la dernière version. C'est là que les dépôts AUR de Arch Linux prennent tous leur intérêt puisqu'il permettent de compiler des package à partir de dépôt Git. Une fois la version de Wine compatible récupérée et compilée, on émule l'installation Windows de League of Legends, puis on lance le jeu directement dans l'environnement.

Malgré le bricolage que cela impose, le jeu reste très stable pendant la durée de compatibilité entre 2 mises à jour du jeu. De manière très subjective, je n'ai eu aucun soucis de plantage du jeu sur Linux, ce qui n'était pas le cas sur Windows. L'inconvénient majeur, comme toujours, c'est que l'on est sur un jeu qui évolue sans support *officiel* de l'éditeur, ce qui signifie parfois avoir un temps d'attente entre la sortie de la mise à jour et le patch de Wine. Fort heureusement, la communauté est très réactive et généralement cela ne dure pas plus de quelques jours. A titre d'exemple, pour le passage en 2.19 d'octobre a été corrigé en 3 jours (à vérifier).

Tout cela parait trop compliqué ? Il existe une alternative quand on veut se passer de tout ça : Lutris. Le logiciel intègre des configurations d'environnement tout fait pour des jeux comme LoL.

## Les plateformes propriétaires : bêtes noires du jeu sur Linux

Le plus gros problème actuel auquel se confronte le jeu sur Linux sont les plateformes propriétaires des éditeurs. Face au succès de Steam et à certaines pratiques commerciales qui peuvent être discutables, de nombreux éditeurs ont voulu sortir leurs propres plateformes de jeux.

La plupart ne sont malheureusement pas compatible Linux, les meilleures comme GoG proposent des jeux Linux mais uniquement sur leur site web, les pires imposent Windows comme seul système d'exploitation compatible, en soutenant le monopole jusque dans leur communication marketing.

## L'avenir du jeu sur Linux

Tout comme on annonce tout les ans l'année du bureau Linux chez les utilisateurs, les rumeurs vont bon train pour dire que Stavia de Google va permettre de donner un coup de pouce aux jeux sur Linux, ou au contraire que la plateforme Xbox de Microsoft va l'enterrer. Ce qui est certain c'est que depuis la sortie de Shadow et son pc dans le cloud pour le jeu, cela va probablement exploser les prochaines années. Est-ce que les infrastructures sont prêtes pour ça ? Est-ce que le succès sera au rendez-vous ? C'est un autre débat, mais je m'accorde plus sur l'idée que ça n'aura pas forcément une grosse influence sur le jeu local sur Linux.

L'avenir se jouera plutôt en faveur de Linux si la communauté reste constante voire s'élargie. Et c'est le sens de mon message dans cet article : casser cette idée reçue qui persiste comme quoi Linux c'est sympa pour le développeur mais pas pour le joueur. D'autant plus que grâce à des initiatives comme Lutris, ce n'est plus uniquement à la portée du bidouilleur.

*[DE]: Desktop Environment
*[LoL]: League of Legends