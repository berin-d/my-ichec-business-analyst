# Synthèse de cours : La gestion du contenu (_Scope Management_)

## 1. Idées essentielles ⭐

- ⭐ **Définition du périmètre (_Scope_)** : Le périmètre ou contenu (_scope_) définit les limites du projet : ce qui est inclus et ce qui en est exclu. Il garantit que le projet inclut tout le travail nécessaire, et **uniquement le travail nécessaire**, pour atteindre ses objectifs.
    
      
    
- ⭐ **Dérives du périmètre à proscrire** :
    
      
    - **Scope Creep** : Expansion non contrôlée du périmètre sans ajustement correspondant du budget, du délai ou des ressources.
        
          
        
    - **Gold Plating (Dorure)** : Pratique consistant à fournir des fonctionnalités ou une qualité supérieures à ce qui a été convenu. Bien que parfois jugée positive commercialement, c'est une mauvaise pratique en gestion de projet traditionnelle.
        
          
        
- ⭐ **Collecte des exigences (_Requirements Elicitation_)** : Les exigences constituent la pierre d'angle du projet. Elles sont recueillies par des analystes métier (_Business Analysts_) à partir de la Charte de projet et du Registre des parties prenantes. Elles doivent idéalement être formalisées, validées et associées à une ligne de référence (_baseline_).
    
      
    
- ⭐ **Tableau de suivi des exigences (_Requirements Traceability Matrix_)** : Outil permettant de relier chaque exigence métier initiale aux livrables et aux recettes de test (_test scripts_), garantissant l'alignement continu sur la valeur métier tout au long du cycle de vie du projet.
    
      
    
- ⭐ **Techniques de priorisation** : Face aux contraintes de budget et de temps, il est indispensable de prioriser les exigences. La méthode **MoSCoW** (_Must_, _Should_, _Could_, _Won't_) et les **Priority Sliders** sont deux outils collaboratifs majeurs. En Agile, l'accent est mis sur le **Minimum Viable Product (MVP)** et le _Product Backlog_.
    
      
    
- ⭐ **Décomposition du contenu (_WBS_ vs Décomposition Agile)** :
    
      
    - **WBS (_Work Breakdown Structure_)** : Décomposition hiérarchique et exhaustive du travail en composants sous forme d'arbre. Les éléments du plus bas niveau sont les **lots de travail (_Work Packages_)**, eux-mêmes divisés en activités.
        
          
        
    - **Règle des 100 %** : La WBS doit couvrir la totalité du périmètre du projet, sans omission ni duplication (éléments mutuellement exclusifs).
        
          
        
    - **Décomposition Agile** : Structure hiérarchique équivalente organisée en **Thème (_Theme_)** $\rightarrow$ **Épopée (_Epic_)** $\rightarrow$ **Récit utilisateur (_User Story_)** $\rightarrow$ **Sous-tâches**.
        
          
        

## 2. Concepts et définitions

|**Concept**|**Définition académique / Précision**|
|---|---|
|**Gestion du contenu** (_Scope Management_) ⭐|Ensemble des processus garantissant que le projet inclut tout le travail requis, et uniquement le travail requis, pour réaliser les objectifs du projet.|
|**Exigence** (_Requirement_) ⭐|Condition ou propriété qui doit être présente dans un produit, service ou résultat pour satisfaire à un contrat ou à une spécification formelle.|
|**Scope Creep** ⭐|Expansion incontrôlée du périmètre du projet sans ajustement proportionnel des délais, des coûts ou des ressources.|
|**Gold Plating** (Dorure) ⭐|Pratique consistant à ajouter des extras ou une qualité supérieure non demandée par le client. Considéré comme une mauvaise pratique en gestion de projet traditionnelle.|
|**Matrice de traçabilité des exigences** (_Requirements Traceability Matrix_) ⭐|Tableau qui relie les exigences métier depuis leur origine jusqu'aux livrables et critères de test associés.|
|**Méthode MoSCoW** ⭐|Technique de priorisation catégorisant les exigences en : _Must have_, _Should have_, _Could/Can have_, et _Won't have (this time)_.|
|**Minimum Viable Product (MVP)** ⭐|Version minimale d'un produit ne comportant que les fonctionnalités essentielles permettant de livrer rapidement de la valeur et d'obtenir des retours utilisateurs.|
|**WBS** (_Work Breakdown Structure_) ⭐|Décomposition hiérarchique de la totalité du travail à exécuter par l'équipe projet pour réaliser les objectifs et créer les livrables requis.|
|**Lot de travail** (_Work Package_) ⭐|Composant du niveau le plus bas de la WBS. C'est l'unité de base pour planifier, estimer, suivre et maîtriser le travail.|
|**User Story** (Récit utilisateur) ⭐|Unité d'exigence atomique rédigée du point de vue de l'utilisateur final et développée au cours d'une itération (_sprint_).|

## 3. Développement du cours

### I. Les enjeux de la gestion du contenu (_Scope_)

Le contenu (_scope_) établit les frontières du projet. Il est généralement défini par un contrat ou un énoncé de travail (_Statement of Work_ - SoW).

  

```
                            ┌─────────────────────────┐
                            │    PERIMÈTRE DU PROJET  │
                            │  ("Tout le travail et   │
                            │   rien que le travail") │
                            └────────────┬────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
         [PIÈGE N°1 : SCOPE CREEP]                       [PIÈGE N°2 : GOLD PLATING]
   • Ajout incontrôlé de demandes                  • "Extras" non demandés offerts au client
   • Absence d'ajustement du budget/délais         • Risque de surcoût / non-réponse au besoin
   • Risque de dérive majeure du projet            • Mauvaise pratique en gestion prédictive
```

#### A. Les dérives majeures

1. **Scope Creep** : L'extension incontrôlée des limites du projet sans révision du budget, de l'échéancier ou des ressources.
    
      
    
2. **Gold Plating (Dorure)** : Tendance de l'équipe à fournir plus que ce qui a été demandé (ex. fonctionnalités en plus, niveau de performance supérieur). Bien que motivée par un souci de bien faire ou une fibre commerciale, la dorure est considérée comme une faute de gestion : elle consomme des ressources sans garantie que le client valorise cet « extra ».
    
      
    

#### B. La nature dynamique du contenu

Le contenu est affiné de manière itérative :

  

- L'équipe recueille d'abord les exigences.
    
      
    
- Elle construit ensuite l'échéancier et le budget.
    
      
    
- Si des contraintes budgétaires, temporelles ou des risques apparaissent, le chef de projet doit effectuer des arbitrages et adapter le contenu en accord avec le commanditaire (_sponsor_).
    
      
    

### II. La collecte et la traçabilité des exigences (_Requirements_)

#### A. Intrants et déroulement

Le processus de collecte repose principalement sur deux éléments :

  

1. **La Charte de projet** (_Project Charter_) / **Dossier de projet** (_Project Brief_) / Contrat.
    
      
    
2. **Le Registre des parties prenantes** (_Stakeholders Register_).
    
      
    

Les analystes métier (_Business Analysts_) interrogent les parties prenantes au moyen de diverses techniques (interviews, _brainstorming_, _focus groups_, prototypes, ateliers collaboratifs comme _Open Practice Library_).

  

#### B. Tableau de suivi des exigences (_Requirements Traceability Matrix_)

Dans les projets traditionnels, la traçabilité garantit qu'aucune exigence initiale ne soit oubliée au fil des étapes de développement.

  

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Exigence Métier │───►│ Architecture /  │───►│   Livrable /    │───►│ Recette de test │
│    (Business)   │    │    Conception   │    │   Composant     │    │  (Test Script)  |
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
  Ex: SLA de 99%          Ex: Architecture       Ex: Déploiement        Ex: Test de reprise
  disponibilité           haute disponibilité    sur 2 Data Centers     après sinistre
```

### III. Priorisation des exigences

Lorsque les ressources ou le temps sont limités, l'équipe ne peut pas satisfaire toutes les demandes des parties prenantes. Il devient nécessaire d'établir des priorités.

  

#### A. La méthode MoSCoW

```
┌────────────────────────────────────────────────────────────────────────┐
│                          MATRICE MoSCoW                                │
├───────────────────────────────────┬────────────────────────────────────┤
│ M - Must Have                     │ S - Should Have                    │
│ Exigences vitales sans lesquelles │ Exigences importantes, mais la     │
│ le projet ne peut pas aboutir.    │ solution reste viable sans elles.  │
├───────────────────────────────────┼────────────────────────────────────┤
│ C - Could Have (ou Can Have)      │ W - Won't Have (this time)         │
│ Fonctionnalités confort à valeur  │ Exigences hors périmètre pour la   │
│ ajoutée mais non essentielles.    │ phase ou l'itération actuelle.     │
└───────────────────────────────────┴────────────────────────────────────┘
```

Cette technique se prête particulièrement bien à l'Agile et aux approches soumises au **time boxing** (durée d'itération fixe) : si le temps manque à la fin du _sprint_, les éléments _Could Have_ sont reportés sans impacter la livraison du cœur de produit.

  

#### B. Autres techniques

- **Priority Sliders (Glissières de priorité)** : Outil visuel où chaque exigence est positionnée sur une glissière graduée pour hiérarchiser les éléments les uns par rapport aux autres.
    
      
    
- **MVP (Minimum Viable Product)** : En Agile, création de la version minimale livrable du produit pour valider rapidement les hypothèses auprès du marché.
    
      
    

### IV. La décomposition du contenu (_Scope Decomposition_)

#### A. La WBS (_Work Breakdown Structure_) en gestion prédictive

La WBS est la décomposition hiérarchique du travail global du projet.

  ![[Pasted image 20261003101122.jpg]]

![[wbs-decoupage-produit.png.webp]]

##### Règles de construction de la WBS :

1. ⭐ **La règle des 100 %** : La WBS couvre 100 % du périmètre du projet. La somme des éléments enfants doit être égale à 100 % de l'élément parent.
    
      
    
2. **Mutuelle exclusivité** : Aucune chevauchement ni duplication entre les composants d'un même niveau.
    
      
    
3. **Identifiant unique** : Chaque élément reçoit une numérotation codifiée (ex. 1.1.2.1).
    
      
    
4. **Lot de travail (_Work Package_)** : Le niveau le plus bas de la WBS. Il sert de base pour estimer les coûts, planifier les activités et mesurer l'avancement. Les lots de travail se décomposent ensuite en **activités**.
    
      
    

#### B. La décomposition hiérarchique en approche Agile

En Agile, la structuration du travail suit un schéma similaire dans le _Product Backlog_ :

  

```
                        ┌──────────────────────────────┐
                        │      THÈME (Theme)           │ Ex: Réduction empreinte carbone
                        └──────────────┬───────────────┘
                                       │
                        ┌──────────────▼───────────────┐
                        │      ÉPOPÉE (Epic)           │ Ex: Dématérialisation factures
                        └──────────────┬───────────────┘
                                       │
                        ┌──────────────▼───────────────┐
                        │   RÉCIT USER (User Story)    │ Ex: En tant qu'utilisateur, je...
                        └──────────────┬───────────────┘
                                       │
                        ┌──────────────▼───────────────┐
                        │     SOUS-TÂCHES (Tasks)      │ Ex: Créer la table SQL
                        └──────────────────────────────┘
```

#### C. Comparaison entre décomposition Prédictive et Agile

| **Caractéristique**      | **Approche Prédictive (WBS)**        | **Approche Agile (Backlog)**             |
| ------------------------ | ------------------------------------ | ---------------------------------------- |
| **Unité de haut niveau** | Livrable principal / Phase           | Thème (_Theme_) / Épopée (_Epic_)        |
| **Unité de bas niveau**  | Lot de travail (_Work Package_)      | Récit utilisateur (_User Story_)         |
| **Niveau d'exécution**   | Activités                            | Sous-tâches du _Sprint_                  |
| **Orientation**          | Livrables et tâches techniques       | Valeur délivrée à l'utilisateur final    |
| **Stabilité**            | Stable une fois validé en _baseline_ | Évolutif et émergent (_Product Backlog_) |
|                          |                                      |                                          |

----

## 4. Points importants à retenir

#### Partie I & II — Périmètre et Exigences

> [!NOTE] À retenir
> 1. La gestion du contenu vise à réaliser l'intégralité du travail prévu, et **rien que ce travail**.
>>
> 2. Le _Scope Creep_ (dérive incontrôlée) et le _Gold Plating_ (ajout d'extras non demandés) sont deux erreurs majeures de gestion de projet.
>>
> 3. Le tableau de suivi des exigences relie les besoins métiers initiaux aux livrables et tests finaux pour éviter tout oubli.


#### Partie III & IV — Priorisation et WBS

> [!NOTE] À retenir
> 1. La méthode MoSCoW classe les exigences (_Must_, _Should_, _Could_, _Won't_) pour adapter la livraison aux contraintes de temps.
>>
> 2. La WBS décompose le projet de haut en bas jusqu'au niveau des **lots de travail (_Work Packages_)**.
>>
> 3. La **règle des 100 %** impose que la WBS couvre la totalité du périmètre sans omissions ni doublons.
>> 
> 4. L'équivalent de la WBS en Agile est la décomposition **Thème $\rightarrow$ Épopée (_Epic_) $\rightarrow$ Récit (_User Story_) $\rightarrow$ Sous-tâches**.
  
----
## 5. Liens entre les notions

```
[Charte de Projet / Contrat] + [Registre des Parties Prenantes]
                             │
                             ▼
                [Collecte des Exigences]
                             │
                             ▼
              [Priorisation (MoSCoW / Sliders)]
                             │
                             ▼
    [Tableau de suivi des exigences (Traceability Matrix)]
                             │
               ┌─────────────┴─────────────┐
               ▼                           ▼
      [Décomposition WBS]       [Décomposition Agile]
               │                           │
               ▼                           ▼
    [Lots de travail (Work Packages)] [Récits utilisateurs (User Stories)]
               │                           │
               ▼                           ▼
          [Activités]               [Sous-tâches / Sprints]
```

## 6. Pièges et confusions fréquentes

|**Notion A**|**Notion B**|**Différence clé à ne pas confondre**|
|---|---|---|
|**Scope Creep**|**Gold Plating**|Le **Scope Creep** provient d'exigences externes ajoutées de manière incontrôlée sans ajustement de budget. Le **Gold Plating** vient de l'équipe projet qui offre volontairement des extras non demandés.|
|**Lot de travail (_Work Package_)**|**Activité**|Le **Work Package** est le composant le plus bas de la WBS (un résultat ou livrable mesurable). L'**activité** est l'action ou la tâche technique nécessaire pour réaliser ce Work Package.|
|**Épopée (_Epic_)**|**Récit utilisateur (_User Story_)**|Une **Epic** est un gros bloc d'exigences trop volumineux pour être réalisé dans un seul _sprint_. Une **User Story** est une unité atomique d'exigence réalisable lors d'un seul _sprint_.|
|**WBS (PMI)**|**PBS (PRINCE2)**|La **WBS** (_Work Breakdown Structure_) décompose le travail et les livrables. La **PBS** (_Product Breakdown Structure_) décompose d'abord les produits/résultats du projet avant de définir les tâches.|

## 7. Synthèse finale (ultra-condensée)

La gestion du contenu (_scope_) garantit que le projet réalise **tout le travail nécessaire, et seulement celui-ci**.

  

1. **Cadrage et Dérives** : Le périmètre est fixé par les exigences. Il faut impérativement lutter contre le **Scope Creep** (ajouts incontrôlés du client) et le **Gold Plating** (extras offerts par l'équipe).
    
      
    
2. **Exigences et Traçabilité** : Recueillies auprès des parties prenantes, les exigences sont répertoriées dans un **tableau de suivi** pour lier besoins métiers, livrables et recettes de test.
    
      
    
3. **Priorisation** : La méthode **MoSCoW** (_Must_, _Should_, _Could_, _Won't_) permet d'arbitrer les exigences sous contraintes de budget ou de temps.
    
      
    
4. **Décomposition** :
    
      
    - En prédictif : Utilisation d'une **WBS** respectant la **règle des 100 %**, découpée jusqu'aux **lots de travail (_Work Packages_)**.
        
          
        
    - En agile : Décomposition du _Product Backlog_ en **Thèmes $\rightarrow$ Épopées $\rightarrow$ User Stories $\rightarrow$ Tâches**.
        
          
        

## Questions de révision

### Niveau 1 — Compréhension

1. **Définition** : Quelle est la règle d'or de la gestion du contenu (_scope_) selon le PMBOK ?
    
      
    
2. **Distinction** : Expliquez la différence entre le _Scope Creep_ et le _Gold Plating_.
    
      
    
3. **Acronyme** : Que signifient les lettres de la méthode de priorisation MoSCoW ?
    
      
    
4. **Structure** : Qu'est-ce qu'un lot de travail (_Work Package_) dans une WBS et à quel niveau de l'arborescence se situe-t-il ?
    
      
    
5. **Règle fondamentale** : En quoi consiste la « règle des 100 % » dans l'élaboration d'une WBS ?
    
      
    

### Niveau 2 — Application

1. **Exercice d'analyse** : Un développeur décide d'ajouter spontanément une fonction de recherche avancée dans une application web parce que cela ne lui a pris que deux heures et qu'il pense que le client va adorer. De quelle dérive s'agit-il et pourquoi est-ce considéré comme une faute en gestion de projet traditionnelle ?
    
      
    
2. **Mise en situation (MoSCoW)** : Dans le cadre d'un projet soumis à un _time box_ strict de 2 semaines, l'équipe s'aperçoit qu'elle n'aura pas le temps de tout développer. Sur quel type d'exigences de la classification MoSCoW l'équipe doit-elle couper en priorité ?
    
      
    
3. **Correspondance des structures** : Établissez la correspondance entre les niveaux d'une décomposition WBS traditionnelle et les niveaux d'une décomposition Agile (_Product Backlog_).
    
      
    

### Niveau 3 — Réflexion / Examen

1. **Cas pratique / Traçabilité** : Expliquez comment l'utilisation d'une matrice de traçabilité des exigences (_Requirements Traceability Matrix_) permet d'éviter l'échec d'un projet informatique lors de la phase de recette utilisateur (_acceptance testing_).
    
      
    
2. **Question de comparaison** : Comparez la gestion du périmètre dans une approche prédictive (basée sur la WBS et la _baseline_) et dans une approche Agile (basée sur le _Product Backlog_ et le MVP). Quels sont les avantages et inconvénients de chaque approche en matière de gestion du changement ?