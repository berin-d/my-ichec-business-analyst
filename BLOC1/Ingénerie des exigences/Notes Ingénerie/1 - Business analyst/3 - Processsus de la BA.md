
## 1. Introduction & Principes généraux

> [!NOTE] Pas de processus universel
> Il n'existe pas de processus unique et systématique. Le choix du processus dépend des circonstances, du problème, des parties prenantes et des technologies.
>

![[Pasted image 20260928135327.jpg]]

----
## 2. Activités transversales et cadres

### A. Analyse du contexte (Business Context)

> [!example] Définition
> Le contexte rassemble les circonstances qui influencent ou expliquent le changement (valeurs de l'entreprise, structure, ressources, etc.).

> [!Summary]  Exemple : Private Banking
> Relation client privilégiée, peu de clients à haut revenu $\rightarrow$ Le coût du SI n'est pas déterminant, la qualité, la personnalisation et la flexibilité priment.

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

![[Pasted image 20260928135836.png]]

L'analyse stratégique s'effectue en amont des détails et est généralement menée par un **Business Analyst Senior**. Elle comprend **4 étapes clés** :

![[Pasted image 20260928140031.png]]

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