Title: Comparatif de librairies javascript de graphique gratuites
Date: 2017-01-01 23:11
Slug: comparatif-3-librairies-graphique-javascript
Author: Nicolas Drufin
category: chart
Summary: Au cours de mon travail, on me demande régulièrement quel est la meilleure méthode de représenter des données graphiquement sur une page web. La question est légitime : il existe enormément de librairies javascript de graphique différentes. Dans cet article, nous allons tester 3 librairies javascript gratuites réputées faciles à prendre en main et indépendantes d'un quelconque framework.
Status: draft

Au cours de mon travail, on me demande régulièrement quel est la meilleure méthode de représenter des données graphiquement sur une page web. La question est légitime : il existe enormément de librairies javascript de graphique différentes. Néanmoins, on distinguera tout de même que celles-ci peuvent se regrouper selon 2 principes très différents sur l'aspect technique :

* **les librairies SVG** : celles-ci utilisent le dessin vectoriel pour représenter graphiquement des données, chaque trait, point, forme géométrique est alors intégré à la page comme des éléments du DOM, et c'est le navigateur qui se charge de dessiner les éléments
* **les libraries canvas** : celles-ci utilise l'élément du DOM `<canvas>` pour dessiner le graphique, toutes les instructions de dessin doivent être scriptées pour obtenir un rendu.

Les deux techniques n'ont pas le même intérêt et c'est ce qu'on tentera de déterminer ici. Dans cet article, nous allons tester 3 librairies javascript gratuites réputées faciles à prendre en main et indépendantes d'un quelconque framework. La facilité de prise en main considère que l'on n'a pas besoin de générer des graphiques depuis 0, comme ce qu'on peut avoir typiquement avec [Raphael](http://dmitrybaranovskiy.github.io/raphael/) ou [D3.js](https://d3js.org/), les librairies choisies intègrent donc un système de chargement de données et de paramétrage de modèles de graphiques. L'indépendance vis-à-vis du framework permet de se détacher du contexte technique qui peut conditionner un projet. C'est un choix discutable mais cela permet pour ma part une réutilisation dans des contextes indépendants. Enfin la gratuitée permet de faire bénéficier ces librairies à n'importe quel projet quelque soit son envergure ou sa maturité. Voici donc sans plus attendre les librairies qui seront testées :

* [C3.js](c3js.org) : une librairie basée sur le dessin vectoriel de [D3.js](https://d3js.org/)
* [Chartist](https://gionkunz.github.io/chartist-js/) : une librairie indépendante qui met en avant son design responsive avec l'utilisation du SVG
* [Chart.js](www.chartjs.org/) : une librairie open source basée sur le canvas HTML5

Le but premier ne sera pas de determiner un vainqueur mais bien de determiner pour quels usages sont destinées ces librairies à partir de la réalisation d'un cas pratique.

### Cas pratique

Le cas pratique utilisé pour ce compartif est de pouvoir afficher un graphique sous force de courbe à partir de 2 séries temporelles. Au fûr et à mesure des réussites, nous y rajouterons de nouvelles exigences pour tester les limites de ces librairies graphique :

1. Changement de style des points et de la courbe
2. Chargement de données aléatoires dynamiquement
3. Traçage d'axe horizontaux (moyenne, écart-type)
4. Sélection automatique de points

Pour chacun des points, nous testerons la praticité de la mise en place, mais aussi la performance et l'ergonomie du rendu.

### C3.js


### Chartist


### Chart.js