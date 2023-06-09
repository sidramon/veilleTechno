<div align="center">

<br/>

**Simon Aucoin**

<br/><br/>

**Rapport de recherche**
  
**Veille technologique**

<br/><br/>

**Les IA de reconnaissance d'image**

<br/><br/>

**Travail remis à**

**M. Nicolas Bourré**

<br/><br/>

**Cégep de Shawinigan**

**9 juin 2023**

</div>

---

# Table des matières
1. [Introduction](#Introduction)
2. [Développement](#Développement)

	2.1. [Historique](#Historique)
	
	2.2. [Méthodologie](#Méthodologie)
	
	2.3. [Résultats](#Résultats)
	
	2.4. [Débats](#Débats)
	
3. [Conclusion](#Conclusion)
4. [Médiagraphie](#Médiagraphie)

---

# Introduction
  
Depuis plusieurs mois, on ne cesse d'entendre parler du progrès des IA (intelligences artificielles) en particulier dans les domaines créatifs tels que la création d'images. Parmi ces avancées, on retrouve des IA telles que **DALL-E** et **Midjourney**, qui permettent de générer des images réalistes et créatives de manière impressionnante. Au cœur de ces avancées se trouve la reconnaissance d'image, un élément essentiel de cette évolution. C'est dans ce contexte que mon projet portera sur l'utilisation d'un modèle de reconnaissance d'image. Ce rapport abordera l'historique des IA, la méthodologie de mon projet, les résultats obtenus, ainsi qu'un débat entre deux langages de programmation.

---

# Développement

## Historique

### Définition

L'intelligence artificielle ou couramment abrégé par « IA » consiste à utiliser certains procédés logiques tel que les réseaux de neurones pour permettre aux machines d'imiter une forme d'intelligence, comme la discussion, la classification et détection d'objets, la création artistique, la prise de décision, etc.

Présentement, on retrouve le traitement d'images et de vidéos dans divers domaines de l'intelligence artificielle. Par exemple, la vision par ordinateur est largement utilisée dans la reconnaissance faciale, la détection d'objets, l'analyse de scènes et la surveillance vidéo. Ces technologies permettent aux machines d'analyser et de comprendre visuellement leur environnement.

![OcarinaSpace](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/ocarinaSpace.png)
> Image d'un ocarina dans l'espace générée par https://www.craiyon.com/

### Histoire

L'idée d'intelligence artificielle apparait dans les années 1950 dans le livre du mathématicien Alan Turing _Computing Machinery and Intelligence_ où il propose la possibilité qu'une machine soit doté d'intelligence. De là provient l'idée du « test de Turing », ce test est une épreuve conçue pour évaluer la capacité d'une machine à présenter un comportement intelligent qui n'est pas discernable d'un vrai être humain. *« [. . .] un sujet interagit à l'aveugle avec un autre humain, puis avec une machine programmée pour formuler des réponses sensées. Si le sujet n'est pas capable de faire la différence, alors la machine a réussi le test et, selon l'auteur, peut véritablement être considérée comme « intelligente »  », https://www.futura-sciences.com/tech/definitions/informatique-intelligence-artificielle-555/*. Toutefois, bien que ce test soit un concept important dans le domaine de l'IA, il n'est pas considéré comme une mesure définitive de l'intelligence d'une machine, celle-ci s'étend au-delà d'une simple conversation. 

Dès 1958 l'idée de réseau de neurones est introduite par le psychologue américain Frank Rosenblatt comme étant le premier système artificiel capable d'apprendre par expérience. Suite à cela, de nombreux développements et avancées ont été réalisés dans le domaine de l'IA tel qu'élaborer plus haut.

![imageRecognition](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/imageRecognition.jpg)

> Image du site https://azati.ai/image-detection-recognition-and-classification-with-machine-learning/

## Méthodologie

Mon programme utilise la caméra de l'ordinateur pour fournir une image au model de reconnaissance d'image pré-entraîné qui utilise son réseau de neurone de classification pour identifier l'objet qui se trouve sur l'image et afficher le résultat.
  
Lorsque le modèle reçoit une image à prédire, il effectue plusieurs étapes. Tout d'abord, l'image est prétraitée pour la mettre dans un format approprié pour le modèle, comme le redimensionnement et la normalisation. Ensuite, l'image est passée à travers le modèle qui applique les opérations de calcul nécessaires pour générer une prédiction. Enfin, la prédiction est renvoyée sous forme de probabilités pour chaque classe, indiquant la confiance du modèle dans sa prédiction pour chaque classe possible de l'image.

### Outils utilisés

-   **PyCharm :** un environnement de développement intégré (IDE) pour Python qui facilite l'écriture, le débogage et le test du code.

-   **Python :** un langage de programmation utilisé pour implémenter l'IA et interagir avec les bibliothèques nécessaires.

-   **PyTorch :** une bibliothèque d'apprentissage automatique (*deep learning*) en Python qui fournit des outils pour la création et l'entraînement de réseaux de neurones.

-   **ResNet-101 :** un modèle de réseau de neurones convolutif profond utilisé pour la classification d'images. Il est pré-entraîné sur de grands ensembles de données et peut être utilisé comme base pour d'autres tâches de vision par ordinateur.

### Concepts utilisés

-   **Traitement d'images :** l'ensemble des techniques et des algorithmes utilisés pour manipuler et analyser des images.

-   **Vision par ordinateur :** un domaine de l'intelligence artificielle qui se concentre sur l'acquisition, le traitement et l'analyse d'images et de vidéos pour permettre aux machines de comprendre et d'interagir avec leur environnement visuel.

-   **Réseau de neurones :** un modèle mathématique inspiré du fonctionnement du cerveau humain, utilisé en apprentissage automatique pour effectuer des tâches d'apprentissage, de classification et de prédiction.

-   **Classification d'images :** un type de tâche en vision par ordinateur où l'objectif est de prédire la classe ou la catégorie d'une image donnée. Dans ce projet, le modèle ResNet-101 est utilisé pour classifier les images provenant de la caméra en temps réel.

## Résultats

Le résultat final obtenu est très satisfaisant. L'IA parvient à identifier ce qui se trouve sur l'image avec un taux de réussite quasiment parfait. Sa seule limitation réside dans sa connaissance limitée à mille objets. Au départ on s'attendait à utiliser un model qui englobe encore plus de choses comme les humains et les animaux, mais le model actuellement utilisé pour les objets retourne un résultat amplement suffisant pour le contexte de la recherche.

![Ocarina](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/ocarina.png)
![Water Bottle](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/waterBottle.png)

## Débats


À ce jour, deux frameworks d'apprentissage automatique se distinguent dans le domaine de l'intelligence artificielle en **Python** : **PyTorch** et **TensorFlow**.

Il est important de noter que le choix entre PyTorch et TensorFlow dépend des besoins du projet. PyTorch est souvent privilégié pour sa convivialité en recherche et son flexibilité, tandis que TensorFlow est souvent préféré pour sa performance et son écosystème plus mature en entreprise.

Voici quelques points positifs et négatifs à prendre en compte lorsqu'on compare TensorFlow et PyTorch :

### TensorFlow :

**Points positifs :**

1.  **Adoption généralisée :** TensorFlow est l'une des bibliothèques les plus populaires pour l'apprentissage automatique et est utilisé par de nombreuses entreprises et chercheurs. Il possède une large communauté de développeurs et une grande quantité de ressources disponibles en ligne.
2.  **Déploiement efficace :** TensorFlow offre des outils pour déployer des modèles sur différentes plates-formes, y compris sur mobile (TensorFlow Lite) et sur le Web (TensorFlow.js). Il possède également TensorFlow Serving, qui facilite le déploiement des modèles en production.
3.  **TensorFlow Extended (TFX) :** TensorFlow dispose d'une suite d'outils appelée TensorFlow Extended qui facilite la création de pipelines de bout en bout pour la préparation des données, la formation, le déploiement et la maintenance des modèles d'apprentissage automatique.

**Points négatifs :**

1.  **Courbe d'apprentissage abrupte :** TensorFlow peut être plus difficile à apprendre et à utiliser pour les débutants. La syntaxe peut sembler complexe, et la mise en place de certaines fonctionnalités avancées peut nécessiter une compréhension approfondie du framework.
2.  **Moins convivial pour la recherche :** Bien que TensorFlow soit largement utilisé dans l'industrie, certains chercheurs trouvent que PyTorch est plus convivial pour la recherche en raison de sa syntaxe plus concise et de son mode de débogage plus intuitif.

### PyTorch :

**Points positifs :**

1.  **Programmation dynamique :** PyTorch utilise un graphique de calcul dynamique, ce qui signifie que les utilisateurs peuvent définir et modifier les graphiques computationnels à la volée. Cela facilite le débogage et le prototypage rapide, et offre une plus grande flexibilité lors de la création de modèles.
2.  **Compréhension intuitive :** La syntaxe de PyTorch est souvent considérée comme plus simple et plus intuitive, ce qui facilite la compréhension et l'apprentissage, en particulier pour les débutants en apprentissage automatique.
3.  **Communauté de recherche active :** PyTorch est devenu très populaire parmi la communauté de recherche en apprentissage automatique, ce qui en fait un choix attrayant pour les chercheurs. De nombreux travaux de recherche sont publiés avec du code PyTorch, et il existe une abondance de tutoriels et de ressources de recherche disponibles.

**Points négatifs :**

1.  **Déploiement plus complexe :** PyTorch a historiquement été considéré comme moins convivial pour le déploiement en production. Cependant, des efforts sont en cours pour faciliter le déploiement avec des outils tels que TorchServe.
2.  **Moins de support pour les plateformes mobiles :** Bien que PyTorch dispose de certaines options pour le déploiement sur mobile, comme PyTorch Mobile, TensorFlow offre une intégration plus étroite avec TensorFlow Lite, ce qui en fait un choix plus courant pour les applications mobiles.

---

# Conclusion
  
En conclusion, ce projet a exploré l'utilisation d'un modèle de reconnaissance d'un objet sur une image. Nous avons examiné l'historique des intelligences artificielles, en soulignant les progrès réalisés dans ce domaine au fil du temps. Ensuite, nous avons détaillé la méthodologie utilisée pour mener ce projet, en mettant en évidence les différentes étapes et les outils utilisés, pour en évaluer les résultat obtenus. 

La reconnaissance d'image est une discipline fascinante de l'intelligence artificielle, offrant la capacité aux machines de comprendre visuellement leur environnement. Grâce aux avancées technologiques, elle ouvre des perspectives prometteuses dans de nombreux domaines. J'espère en apprendre davantage pour expérimenter d'autres réseaux de neurones plus complexes dans la prise de décision et l'IA générative.

---

# Médiagraphie

**Recherches**

*Contributeurs aux projets Wikimedia. (2023). Intelligence artificielle. _fr.wikipedia.org_. https://fr.wikipedia.org/wiki/Intelligence_artificielle*

*Du Web, S. V. (2021, October 4). _Quels langages de code utiliser pour l’IA ? | École IPI_. IPI École D’informatique. https://www.ipi-ecoles.com/langage-programmation-ia/*

*De Futura, L. R. (n.d.). _Intelligence artificielle : qu’est-ce que c’est ?_ Futura. https://www.futura-sciences.com/tech/definitions/informatique-intelligence-artificielle-555/*

*Juillet, R. (2022, October 31). _Quels sont les meilleurs langages de programmation d’IA en 2022 ?_ Bocasay. https://www.bocasay.com/fr/meilleurs-langages-programmation-ia-2022/*

*Contributeurs aux projets Wikimedia. (2023a). Réseau de neurones artificiels. _fr.wikipedia.org_. https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels*

*_Qu’est-ce que la Computer Vision ? | IBM_. (n.d.). https://www.ibm.com/fr-fr/topics/computer-vision#:~:text=La%20vision%20par%20ordinateur%20est,sur%20la%20base%20de%20ces*

*Kurama, V. (2020). PyTorch vs. TensorFlow: Key Differences to Know for Deep Learning. _Built In_. https://builtin.com/data-science/pytorch-vs-tensorflow*

**Développement**

*Shrimali, V., & Shrimali, V. (2023). Pre Trained Models for Image Classification - PyTorch. _LearnOpenCV – Learn OpenCV, PyTorch, Keras, Tensorflow With Examples and Tutorials_. https://learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/*

*A. (2021, November 22). Reconnaissance d’images en Python avec TensorFlow et Keras | Savage Rose. Savage Rose. [https://savagerose.org/fr/reconnaissance-dimages-en-python-avec-tensorflow-et-keras/](https://savagerose.org/fr/reconnaissance-dimages-en-python-avec-tensorflow-et-keras/)*

*TensorFlow. (n.d.). _TensorFlow_. https://www.tensorflow.org/?hl=fr*

*_PyTorch_. (n.d.). https://pytorch.org/*
