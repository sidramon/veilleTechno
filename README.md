<div align="center">

<br/>

**Simon Aucoin**

<br/><br/>

**Rapport de recherche**
  
**Veille technologique**

<br/><br/>

**Les IA de reconnaissance d'images**

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
  
Depuis plusieurs mois, on ne cesse d'entendre parler du progrès des IA (intelligences artificielles) en particulier dans les domaines créatifs tels que la création d'images. Parmi ces avancées, on retrouve des IA telles que **DALL-E** et **Midjourney**, qui permettent de générer des images réalistes et créatives de manière impressionnante. Au cœur de ces avancées se trouve la reconnaissance d'image, un élément essentiel de cette évolution. C'est dans ce contexte que mon projet portera sur l'utilisation d'un model de reconnaissance d'image. Ce rapport abordera l'historique des IA, la méthodologie de mon projet, les résultats obtenus, ainsi qu'un débat entre deux langages de programmation.

---

# Développement

## Historique

### Définition

L'intelligence artificielle ou couramment abrégé par « IA » consiste à utiliser certains procédés logiques tel que les réseaux de neurones pour permettre aux machines d'imiter une forme d'intelligence, comme la discussion, la classification et détection d'objets, la création artistique, la prise de décision, etc.

Présentement, on retrouve le traitement d'images et de vidéos dans divers domaines de l'intelligence artificielle. Par exemple, la vision par ordinateur est largement utilisée dans la reconnaissance faciale, la détection d'objets, l'analyse de scènes et la surveillance vidéo. Ces technologies permettent aux machines d'analyser et de comprendre visuellement leur environnement.

![OcarinaSpace](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/ocarinaSpace.png)
> Image d'un ocarina dans l'espace générée par https://www.craiyon.com/

### Histoire

L'idée d'intelligence artificielle apparait dans les années 1950 dans le livre du mathématicien Alan Turing _Computing Machinery and Intelligence_ où il propose la possibilité qu'une machine soit doté d'intelligence. De là provient l'idée du « test de Turing », ce test est une épreuve conçue pour évaluer la capacité d'une machine à présenter un comportement intelligent qui n'est pas discernable d'un vrai être humain. *« [. . .] un sujet interagit à l'aveugle avec un autre humain, puis avec une machine programmée pour formuler des réponses sensées. Si le sujet n'est pas capable de faire la différence, alors la machine a réussi le test et, selon l'auteur, peut véritablement être considérée comme « intelligente »  », https://www.futura-sciences.com/tech/definitions/informatique-intelligence-artificielle-555/*. Toutefois, bien que ce test soit un concept important dans le domaine de l'IA, il n'est pas considérer comme une mesure définitive de l'intelligence d'une machine, celle-ci s'étend au-delà d'une simple conversation. 

Dès 1958 l'idée de réseau de neurones est introduite par le psychologue américain Frank Rosenblatt comme étant le premier système artificiel capable d'apprendre par expérience. Suite à cela, de nombreux développements et avancées ont été réalisés dans le domaine de l'IA.

![imageRecognition](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/imageRecognition.jpg)

> Image du site https://azati.ai/image-detection-recognition-and-classification-with-machine-learning/

## Méthodologie

Mon programme utilise la caméra de l'ordinateur pour fournir une image au model de reconnaissance d'image pré-entraîné qui utilise son réseau de neurone de classification pour identifier l'objet qui se trouve sur l'image.

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

Le résultat final obtenu est très satisfaisant. L'IA parvient à identifier ce qui se trouve sur l'image avec un taux de réussite quasiment parfait. Sa seule limitation réside dans sa connaissance limitée à mille objets. Au départ on s'attendait utiliser un model qui englobe encore plus de choses comme les humains et les animaux, mais le model actuellement utilisé pour les objets retourne un résultat amplement suffisant.

![Ocarina](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/ocarina.png)
![Water Bottle](https://github.com/sidramon/veilleTechno/blob/main/documentation/images/waterBottle.png)

## Débats

À ce jour, plusieurs langages de programmation sont reconnus pour leur pertinence dans le développement d'intelligence artificielle, mais il y en a deux qui sortent plus particulièrement du lot : le **Python** et le **Java**.

Pour sa facilité d'utilisation et ses bibliothèques clé en main, j'ai opté pour le **Python**, mais utilisé le **Java** aurait aussi été une option intéressante pour sa performance.

### Pourquoi Java ?

Java est un langage de programmation orienté objet couramment utilisé dans le domaine de la reconnaissance d'image. Ses principaux avantages sont :

1.  **Portabilité** : Java est un langage de programmation portable, il peut être exécutés sur différents systèmes d'exploitation sans nécessiter de modifications majeures.
    
2.  **Orienté objet** : Java est un langage orienté objet, ce qui permet d'organiser le code en classes et en objets, favorisant ainsi une conception modulaire et une réutilisation du code.
    
3.  **Grande communauté et bibliothèques** : Java bénéficie d'une vaste communauté de développeurs et d'une abondance de bibliothèques disponibles. Il existe des bibliothèques spécialisées dans le traitement d'images et la reconnaissance d'image en Java, tel que *OpenCV Java* qui offre des fonctionnalités avancées.
    
4.  **Performance** : Bien que Java ne soit pas aussi performant que certains langages de bas niveau tels que le C++, il offre des performances adéquates pour de nombreux cas d'utilisation de la reconnaissance d'image. De plus, grâce aux améliorations continues de la JVM et aux optimisations du compilateur Java, les performances des applications Java s'améliorent régulièrement.

### Pourquoi Python ?

Python est également un langage de programmation populaire et largement utilisé dans le domaine de la reconnaissance d'image. Ses principaux avantages sont :

1.  **Simplicité et lisibilité** : Python a été conçu pour être un langage facile à lire et à comprendre. Sa syntaxe simple et expressive permet aux développeurs d'écrire du code clair et concis, ce qui facilite la compréhension et la maintenance du code.
    
2.  **Large écosystème de bibliothèques** : Python dispose d'une vaste collection de bibliothèques spécialisées dans le traitement d'images et la reconnaissance d'images, telles que *OpenCV*, *scikit-image* et *TensorFlow*. Ces bibliothèques offrent des fonctionnalités avancées et des algorithmes clé en main.
    
3.  **Portabilité et compatibilité** : Python est un langage multiplateforme, ce qui signifie qu'il peut être exécuté sur divers systèmes d'exploitation tels que Windows, macOS et Linux. Il est également compatible avec de nombreux *frameworks* et outils de développement, ce qui facilite l'intégration de Python dans des projets existants.
    
4.  **Communauté active et support** : Python bénéficie d'une communauté active de développeurs qui contribuent constamment à son développement. Cette communauté fournit un support précieux sous la forme de documentation, de tutoriels, de forums de discussion et de packages open source, ce qui facilite l'apprentissage et la résolution des problèmes.

---

# Conclusion

  

---

# Médiagraphie

**Recherches**

*Contributeurs aux projets Wikimedia. (2023). Intelligence artificielle. _fr.wikipedia.org_. https://fr.wikipedia.org/wiki/Intelligence_artificielle*

*Du Web, S. V. (2021, October 4). _Quels langages de code utiliser pour l’IA ? | École IPI_. IPI École D’informatique. https://www.ipi-ecoles.com/langage-programmation-ia/*

*De Futura, L. R. (n.d.). _Intelligence artificielle : qu’est-ce que c’est ?_ Futura. https://www.futura-sciences.com/tech/definitions/informatique-intelligence-artificielle-555/*

*Juillet, R. (2022, October 31). _Quels sont les meilleurs langages de programmation d’IA en 2022 ?_ Bocasay. https://www.bocasay.com/fr/meilleurs-langages-programmation-ia-2022/*

*Contributeurs aux projets Wikimedia. (2023a). Réseau de neurones artificiels. _fr.wikipedia.org_. https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels*

*_Qu’est-ce que la Computer Vision ? | IBM_. (n.d.). https://www.ibm.com/fr-fr/topics/computer-vision#:~:text=La%20vision%20par%20ordinateur%20est,sur%20la%20base%20de%20ces*

**Développement**

*Shrimali, V., & Shrimali, V. (2023). Pre Trained Models for Image Classification - PyTorch. _LearnOpenCV – Learn OpenCV, PyTorch, Keras, Tensorflow With Examples and Tutorials_. https://learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/*

*A. (2021, November 22). Reconnaissance d’images en Python avec TensorFlow et Keras | Savage Rose. Savage Rose. [https://savagerose.org/fr/reconnaissance-dimages-en-python-avec-tensorflow-et-keras/](https://savagerose.org/fr/reconnaissance-dimages-en-python-avec-tensorflow-et-keras/)*

*TensorFlow. (n.d.). _TensorFlow_. https://www.tensorflow.org/?hl=fr*

*_PyTorch_. (n.d.). https://pytorch.org/*
