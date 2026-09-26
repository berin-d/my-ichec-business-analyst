Voici une synthèse complète et structurée du cours sur le **Processus de la Business Analysis (BA)** basée sur le document fourni.

# Synthèse : Le Processus de la Business Analysis

## 1. Introduction & Principes généraux

- **Pas de processus universel :** Il n'existe pas de processus unique et systématique. Le choix du processus dépend des circonstances, du problème, des parties prenantes et des technologies.
    
- **Dynamique réelle :** En pratique, les phases se superposent et comportent du parallélisme, des itérations et des allers-retours. Pour des raisons pédagogiques, le cours présente un **processus type linéaire et itératif par raffinements successifs**.
    
- **Structure globale (basée sur le BABOK) :**
    
    1. **Analyse du contexte (Business Context) :** Activité transversale haute.
        
    2. **Planification des activités de BA :** Tâche de fond assimilable à de la gestion de projet.
        
    3. **Les 4 grandes phases du processus :**
        
        - **Strategy Analysis** (Analyse stratégique)
            
        - **Requirements Analysis** (Analyse des exigences)
            
        - **Solution Design** (Conception de la solution)
            
        - **Solution Evaluation** (Évaluation de la solution)

----
## 2. Activités transversales et cadres

### A. Analyse du contexte (Business Context)

- Le contexte rassemble les circonstances qui influencent ou expliquent le changement (valeurs de l'entreprise, structure, ressources, etc.).
    
- **Exemple illustratif (Secteur bancaire) :**
    
    - _Private Banking :_ Relation client privilégiée, peu de clients à haut revenu $\rightarrow$ Le coût du SI n'est pas déterminant, la qualité, la personnalisation et la flexibilité priment.
        
    - _Retail Banking :_ Banque grand public, grands volumes, transactions multiples $\rightarrow$ Le facteur coût est prédominant, le SI s'appuie sur des processus standards.

### B. Planification des activités de Business Analysis

- **Rôle :** Cadre et encadre le travail des parties prenantes tout au long du projet.
    
- **Contenu principal :**
    
    - Identification du problème/opportunité, définition des objectifs et de la valeur attendue.
        
    - Identification des tâches, des délais, des coûts et des livrables (ex: _Business Analysis Plan_, _Stakeholder Engagement Plan_).
        
    - **Choix des approches/outils :**
        
        - _Approche prédictive (classique) :_ Linéaire, exigences définies en amont, planification détaillée.
            
        - _Approche adaptative (agile) :_ Itérative, intégration continue du changement.
            
    - **Facteurs de choix d'approche :** Taille et complexité du projet, profil et disponibilité des parties prenantes, volatilité des exigences, contraintes de délai.

----
## 3. Phase 1 : Strategy Analysis (Analyse Stratégique)

L'analyse stratégique s'effectue en amont des détails et est généralement menée par un **Business Analyst Senior**. Elle comprend **4 étapes clés** :

1. **Analyze Current State (Situation _As-Is_) :**
    
    - Description de l'état actuel de l'entreprise (structure, culture, processus actuels via BPMN, indicateurs KPI actuels).
        
    - Description des besoins/problèmes à un niveau macroscopique.
        
    - _Livrables clés :_ `Current State Description`, `Business Requirement`.
        
    - _Techniques :_ Business Model Canvas, PEST, etc.
        
2. **Define Future State (Situation _To-Be_) :**
    
    - Définition des buts, des objectifs à atteindre (ex: cibles KPI) et des valeurs attendues (_Potential Value_).
        
    - Identification des capacités, infrastructures et ressources requises.
        
3. **Risk Analysis (Analyse des risques) :**
    
    - Évaluation des risques liés au changement.
        
    - Définition des stratégies et contre-mesures pour réduire la probabilité de survenance et l'impact des risques.
        
4. **Define Change Strategy (Stratégie de changement / _Gap Analysis_) :**
    
    - Analyse de l'écart (_Gap Analysis_) entre l'état actuel (_As-Is_) et l'état futur (_To-Be_).
	    
        
    - Évaluation des solutions selon des critères (coût, délai, impact, niveau de risque, faisabilité) via une grille ou matrice d'évaluation pour sélectionner la meilleure option.
        
    - _Livrables clés :_ 
	    - `Solution Scope`
	    - `Change Strategy Document -> Approche pour piloter le changement`.

---
### Analyse as is

> Exemple : Une administration régionale gère des dossier de demandes de primes à la rénovation durable d'un bâtiment.

#### Contexte
- Description des processus en place : BPMN
- Mesurer la performance : indicateur de performance comme KPI, délai moyen du traitement

#### Problème
- Délai trop long dans la prise de décision du montant pour l'octroi d'une prime.
- Mécontentement des différentes partie prenante.

Ce qui motive le changement, c'est la résolution de ce **Problème**.

---
### Analyse to be

> Fixation d'objectifs afin de résoudre le problème identité en amont
 
- Réduction du temps moyen un traitement à 3 mois
- Augmentation du niveau de satisfaction à 20%

---
### Gap analysis

> Comment migrer d'une situation "as is" vers "to be". Avec l'identification des facteurs limitants

- Manque d'automatisation des processus
- Nombre d'intervenant trop nombreux
- Motivation et formation du personnel irrégulières

> Identification des solutions possibles (bridging the gap)

- Automatisation de aches encore manuelles
- Optimisation via la réduction du nombre d'intervenants
- Plan de formation et de motivation du personnel


![[Pasted image 20260919120629.png]]

-----
## 4. Phase 2 : Requirements Analysis (Analyse des Exigences)

- **Cœur du métier du Business Analyst :** Constituer un ensemble précis, complet et cohérent d'exigences pour la solution retenue.
    
- **Niveau de détail :** Passage du niveau macroscopique au niveau d'ingénierie détaillée des exigences.
    
- **Alignement :** Chaque exigence doit être motivée par la valeur qu'elle apporte aux parties prenantes.
    
- _Livrable clé :_ `System Requirement Specification` (SRS) / Liste d'exigences (sous forme de _User Stories_, etc.).

----
## 5. Phase 3 : Solution Design (Conception de la Solution)

- **Objectif :** Spécifier en détail la solution proposée et son fonctionnement.
    
- **Raffinement itératif :** Intègre l'analyse des exigences pour définir précisément comment le système va résoudre le problème.
    
- **Composants du livrable `Solution Design Document` (SDD) :**
    
    1. _Introduction & Périmètre :_ Mission, rôles/parties prenantes identifiées nominativement.
        
    2. _Exigences détaillées :_ Expression des besoins métier (ex: _User Stories_).
        
    3. _Description de la solution :_
        
        - Modélisation des processus futurs (ex: diagrammes d'activités, BPMN).
            
        - Spécification des formulaires, champs et règles métier.
            
        - Définition de la portée (_Scope_ : ce que la solution fait vs ce qui est hors périmètre).
            
        - Jalons et planification des tâches de réalisation.
            
    4. _Plan de test :_ Cas de tests et réponses attendues du système.
        

------
## 6. Phase 4 : Solution Evaluation (Évaluation de la Solution)

- **Objectif :** S'assurer que la solution déployée ou proposée répond aux objectifs fixés dans le _To-Be_ et satisfait les besoins des parties prenantes.
    
- **Activités de test :** Planification, création et exécution des cas de tests.
    
- **Assurance qualité continue :** La vérification et la validation ne se font pas uniquement à la fin du projet ("One shot"), mais s'étendent tout au long du cycle pour valider la qualité et la compréhension des produits intermédiaires et des exigences.

-----

## 7. Exemple d'application concret : Optimisation du traitement des PAE (Programme d'Études Annuel)

|**Phase**|**Application au cas PAE**|
|---|---|
|**Situation _As-Is_**|Téléchargement de formulaires, envois d'e-mails, encodages multiples sur Excel par le secrétariat, transmission manuelle au responsable de programme. _Problèmes :_ Délais longs, intermédiaires superflus, risques d'erreurs.|
|**Situation _To-Be_**|Réduction des délais de traitement, augmentation de la satisfaction, suppression des ré-encodages manuels.|
|**Gap Analysis & Solution**|Intégration dans le système centralisé informatisé existant. L'étudiant encode directement sa demande, le responsable valide en ligne, les intermédiaires (secrétariat) et les échanges e-mail/Excel sont supprimés.|
|**Périmètre (_Scope_)**|_In Scope :_ Modifications de PAE standards. _Out of Scope :_ Étudiants en échange / cours Erasmus hors institution.|

----
## 8. Profils et Compétences (BABOK)

- **Senior BA :** Prise en charge des phases amont à forte dimension stratégique, à savoir la **Planification** et la **Strategy Analysis**.
    
- **Junior BA :** Prise en charge des phases de réalisation et de suivi opérationnel, soit la **Requirements Analysis**, le **Solution Design** et la **Solution Evaluation**.