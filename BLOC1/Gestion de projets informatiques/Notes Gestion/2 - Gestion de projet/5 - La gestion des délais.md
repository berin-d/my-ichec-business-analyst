
## 1. Idées essentielles ⭐

- ⭐ **Responsabilité du chef de projet** : La production d'un échéancier (_planning_) réaliste relève de la responsabilité exclusive du chef de projet. Un planning irréaliste ne doit jamais être accepté passivement ; le chef de projet doit dénoncer son infaisabilité et réajuster les contraintes.
    
      
    
- ⭐ **Non-négociabilité des charges (LoE)** : Les estimations d'effort/charge (_Level of Effort - LoE_) sont réalisées par des experts ou les exécutants et **ne se négocient pas**. Seuls le contenu (_scope_), l'ordonnancement, les ressources ou la méthodologie peuvent faire l'objet de négociations.
    
      
    
- ⭐ **Planification par vagues (_Rolling Wave Planning_)** : Technique d'élaboration progressive où le travail à court terme est planifié dans le détail, tandis que le travail à plus long terme est planifié à haut niveau.
    
      
    
- ⭐ **Méthode des précédences (PDM / AON)** : Technique de modélisation de réseau reliant des activités (nœuds) par 4 types de liens logiques : **Fin à Début (FS)** (le plus courant), **Fin à Fin (FF)**, **Début à Début (SS)**, et **Début à Fin (SF)** (très rare).
    
      
    
- ⭐ **Chemin critique (_Critical Path Method - CPM_)** ⭐ :
    
      
    - C'est la séquence d'activités qui représente **le plus long chemin** à travers le réseau et détermine la **durée minimale** du projet.
        
          
        
    - La **marge totale (_total float/slack_)** des activités situées sur le chemin critique est **égale à zéro**. Tout retard sur une activité critique décale immédiatement la date de fin du projet.
        
          
        
- ⭐ **Techniques d'optimisation et de compression** :
    
      
    - **Nivellement des ressources (_Resource Levelling_)** : Ajuste l'échéancier selon la disponibilité réelle des ressources (allonge souvent la durée globale).
        
          
        
    - **Compression des délais (_Crashing_)** : Ajout de ressources sur le chemin critique (augmente les coûts et les risques). _Loi de Brooks_ : « Ajouter des ressources humaines à un projet logiciel en retard le retarde encore plus. »
        
          
        
    - **Exécution accélérée (_Fast Tracking_)** : Réalisation en parallèle d'activités normalement séquentielles (augmente les risques de _rework_).
        
          
        
- ⭐ **Estimations absolues vs relatives (Agile)** :
    
      
    - **Absolues** : Exprimées en unités de temps réelles (heures, jours) pour des approches prédictives.
        
          
        
    - **Relatives (Agile)** : Exprimées en unités abstraites (**Story Points**, tailles de T-shirt) basées sur la complexité/effort comparé (ex. _Planning Poker_ / suite de Fibonacci). Elles permettent d'évaluer la **vélocité** de l'équipe sans s'engager sur une date ferme.
        
          
        

## 2. Concepts et définitions

|**Concept**|**Définition académique / Précision**|
|---|---|
|**Gestion des délais** (_Schedule Management_) ⭐|Processus requis pour garantir l'achèvement du projet dans les temps impartis.|
|**Effort / Charge** (_Level of Effort - LoE_) ⭐|Quantité de travail (ex. personnes/jours, heures) nécessaire pour accomplir une tâche, indépendamment du calendrier.|
|**Durée** (_Duration_) ⭐|Nombre de périodes de travail (jours calendaires/ouvrés) nécessaires pour exécuter une tâche, en tenant compte de la disponibilité des ressources.|
|**Jalon** (_Milestone_) ⭐|Événement ou moment clé du projet dont la **durée est strictement nulle** (ex. signature d'un contrat, mise en production).|
|**Planification par vagues** (_Rolling Wave Planning_) ⭐|Forme de planification progressive où le futur proche est détaillé et le futur lointain reste défini dans ses grandes lignes.|
|**Chemin critique** (_Critical Path_) ⭐|Séquence d'activités conditionnant la date de fin du projet. Chemin le plus long du réseau, avec une marge totale nulle ($Float = 0$).|
|**Marge totale** (_Total Float / Slack_) ⭐|Retard maximal qu'une activité peut subir sans repousser la date d'achèvement du projet ($Late\ Start - Early\ Start$).|
|**Marge libre** (_Free Float_) ⭐|Retard maximal qu'une activité peut subir sans repousser la date de début au plus tôt (_Early Start_) de ses successeurs immédiats.|
|**Story Points** (Points de récit) ⭐|Unité de mesure abstraite employée en Agile pour exprimer l'effort ou la complexité relative d'une _User Story_.|
|**Vélocité** (_Velocity_) ⭐|Métrique Agile indiquant le nombre moyen de _Story Points_ complétés par une équipe au cours d'une itération (_Sprint_).|

## 3. Développement du cours

### I. Les principes fondamentaux de la planification

#### A. Le réalisme de l'échéancier

Un échéancier irréaliste imposé par la hiérarchie ne dégage pas le chef de projet de sa responsabilité. Il doit :

  

1. Construire une ligne du temps techniquement et physiquement réaliste.
    
      
    
2. Ne **jamais négocier l'estimation de charge/effort (_LoE_)** fournie par les experts métier.
    
      
    
3. Négocier uniquement le **contenu (_scope_)**, l'**ordonnancement**, ou le **niveau de ressources**.
    
      
    

#### B. Planification par vagues (_Rolling Wave Planning_)

La précision absolue dès le jour 1 est illusoire. L'élaboration progressive s'impose :

  

```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│     FUTUR PROCHE (Iteratif / Détaillé) │     FUTUR LOINTAIN (Haut Niveau)      │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ • Découpage fin des activités         │ • Jalons macro                        │
│ • Affectation précise des ressources  │ • Estimation globale                  │
│ • Planning précis au jour / semaine   │ • Grandes phases fonctionnelles       │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

### II. L'ordonnancement des activités (Méthode des Précédences - PDM)

Les lots de travail (_Work Packages_) de la WBS sont décomposés en **activités**. Ces activités sont ordonnancées dans un diagramme en réseau (_Activity on Node_ - AON).

  

```
┌───────────────────────────┐                ┌───────────────────────────┐
│   Activité Prédécesseur   │───────────────►│    Activité Successeur    │
└───────────────────────────┘                └───────────────────────────┘
```

#### A. Les 4 types de liaisons logiques

1. **Fin à Début (Finish-to-Start - FS)** ⭐ _(Le plus fréquent)_ : L'activité B ne peut débuter que si A est terminée.
    
      
    
2. **Fin à Fin (Finish-to-Finish - FF)** : L'activité B ne peut se terminer que si A est terminée.
    
      
    
3. **Début à Début (Start-to-Start - SS)** : L'activité B ne peut débuter que si A a démarré.
    
      
    
4. **Début à Fin (Start-to-Finish - SF)** _(Très rare)_ : L'activité B ne peut se terminer que si A a démarré.
    
      
    

#### B. Les 4 types de dépendances (Contraintes)

- **Obligatoire** : Physiques, techniques ou légales (ex. couler les fondations avant de monter les murs).
    
      
    
- **Optionnelle (Préconisée)** : Règles de l'art / _Best practices_ (ex. faire un prototype avant de développer).
    
      
    
- **Externe** : Dépend d'un tiers hors projet (ex. obtention d'un permis d'urbanisme).
    
      
    
- **Interne** : Sous le contrôle de l'équipe projet (ex. dresser les tables avant d'accueillir les invités).
    
      
    

#### C. Avances et Retards (_Leads and Lags_)

- **Décalage de retard (_Lag_) [+$]** : Délai d'attente imposé (ex. séchage de la peinture pendant 2 jours avant la seconde couche).
    
      
    
- **Décalage d'avance (_Lead_) [-$]** : Chevauchement anticipé (ex. démarrer la rédaction de la documentation 5 jours avant la fin du codage).
    
      
    

### III. Techniques d'estimation de charge et de durée

#### A. Distinction clé : Charge vs Durée

$$\text{Durée} = \frac{\text{Charge (Effort en Hommes/Jours)}}{\text{Nombre de Ressources} \times \text{Disponibilité}}$$

> **Exemple** : Une charge de 10 personnes/jours attribuée à un expert disponible à mi-temps (50 %) donne une durée calendaire de 20 jours.
> 
>   

#### B. Méthodes d'estimation traditionnelles

1. **Jugement d'expert & Technique Delphi / Delphi Wideband** : Démarche itérative et anonyme supervisée par un modérateur pour faire converger des avis d'experts divergents vers un consensus.
    
      
    
2. **Estimation par analogie** : Comparaison rapide et peu coûteuse avec un projet antérieur similaire (peu précise).
    
      
    
3. **Estimation paramétrique** : Calcul mathématique basé sur des données historiques et des paramètres (ex. $25\text{ m de câble/heure} \times 125\text{ m} = 5\text{ heures}$).
    
      
    
4. **Estimation ascendante (_Bottom-Up_)** : Estimation fine de chaque activité de bas niveau puis agrégation globale.
    
      
    
5. **Estimation à 3 points (PERT)** ⭐ : Prend en compte l'incertitude en calculant la charge attendue ($t_E$) à partir de 3 valeurs : Optimiste ($t_O$), Plus probable ($t_M$), Pessimiste ($t_P$).
    
      
    

$$\text{Distribution Triangulaire : } t_E = \frac{t_O + t_M + t_P}{3}$$

$$\text{Distribution Bêta (PERT classique) : } t_E = \frac{t_O + 4t_M + t_P}{6}$$

#### C. Provisions pour risques

- **Provision pour aléas (_Contingency Reserve_)** : Couvre les risques connus (_known-unknowns_). Inclus dans l'échéancier de référence et gérée par le chef de projet.
    
      
    
- **Provision pour imprévus (_Management Reserve_)** : Couvre les risques inconnus (_unknown-unknowns_). Non incluse dans la ligne de référence.
    
      
    

### IV. La Méthode du Chemin Critique (_CPM_) et Optimisation

#### A. Calcul du chemin critique et des marges

Pour chaque activité, 4 dates sont calculées par balayage du réseau :

  

- **ES** (_Early Start_) : Début au plus tôt.
    
      
    
- **EF** (_Early Finish_) : Fin au plus tôt ($EF = ES + \text{Durée}$).
    
      
    
- **LS** (_Late Start_) : Début au plus tard.
    
      
    
- **LF** (_Late Finish_) : Fin au plus tard ($LF = LS + \text{Durée}$).
    
      
    

$$\text{Marge Totale (Total Float)} = LS - ES \quad \text{ou} \quad LF - EF$$

```
   [ Chemin 1 : A (5j) -> B (5j) -> D (10j) ] = 20 jours  (Marge = 10j)
   [ Chemin 2 : A (5j) -> C (15j) -> D (10j) ] = 30 jours  <-- CHEMIN CRITIQUE (Marge = 0)
```

#### B. Techniques d'optimisation du planning

```
                               ┌──────────────────────────────────────────────┐
                               │   OPTIMISATION DE L'ÉCHÉANCIER (PLANNING)    │
                               └──────────────────────┬───────────────────────┘
                                                      │
             ┌────────────────────────────────────────┼────────────────────────────────────────┐
             ▼                                        ▼                                        ▼
   NIVELLEMENT DES RESSOURCES                COMPRESSION (Crashing)                  FAST TRACKING
   • Ajuste selon disponibilités             • Ajout de ressources / H.S.            • Parallélisation de tâches
   • Évite le surmenage                      • Risque : Hausse des coûts/risques     • Risque : Rework / Erreurs
   • ALLONGE la durée globale                • Loi de Brooks (projets logiciels)    • S'applique au chemin critique
```

- **Loi de Brooks** : « Ajouter des ressources humaines à un projet logiciel en retard ne fait que le retarder davantage » (en raison du coût de communication et de formation des nouveaux arrivants).
    
      
    

#### C. Simulations et modèles

- **Analyse Scénarique (_What-if_)** : Évaluation de l'impact de risques spécifiques ("Que se passe-t-il si le fournisseur a 2 semaines de retard ?").
    
      
    
- **Simulation de Monte-Carlo** : Calcul statistique de milliers de scénarios probabilistes pour déterminer les chances d'achever le projet à une date donnée (ex. 90 % de chances de finir avant le 28 mai).
    
      
    

### V. Présentation et Suivi du Planning

#### A. Formats de restitution

1. **Diagramme de Gantt (_Bar Chart_)** : Vue standard représentant les tâches en barres temporelles (idéal pour le suivi d'équipe).
    
      
    
2. **Diagramme de Jalons (_Milestone Chart_)** : Vue synthétique haute direction ne présentant que les événements majeurs ($Durée = 0$).
    
      
    
3. **Diagramme de Réseau (_Network Diagram_)** : Présentation purement logique des dépendances sans échelle de temps.
    
      
    

#### B. Maîtrise de l'échéancier

Le suivi repose sur la comparaison continue à une **Date de Statut (_Status Date / Data Date_)** entre :

  

$$\text{Échéancier de Référence (Schedule Baseline)} \quad \text{vs} \quad \text{Avancement Réel (Actual Progress)}$$

### VI. Estimations relatives et Approches Agiles

#### A. Principes de l'estimation relative

Plutôt que d'estimer en heures (absolu), Agile estime l'effort comparatif via des **Story Points** (unités abstraites).

  

- Basée sur des suites d'intervalles croissants (ex. **Fibonacci** : 1, 2, 3, 5, 8, 13, 20, 40, 100) ou des tailles de vêtements (XS, S, M, L, XL).
    
      
    
- Les écarts grands entre chiffres élevés traduisent l'incertitude et incitent à découper les gros blocs (_Epics_).
    
      
    

#### B. Le Planning Poker (Variation de Delphi Wideband)

1. Présentation de la _User Story_ par le _Product Owner_.
    
      
    
2. Discussion rapide par l'équipe de développement.
    
      
    
3. Vote **simultané et anonyme** avec des cartes de la suite Fibonacci.
    
      
    
4. Explication des écarts par les évaluateurs des valeurs **extrêmes** (plus haute et plus basse).
    
      
    
5. Ré-estimation itérative jusqu'à l'obtention d'un consensus.
    
      
    

#### C. Intérêt et Vélocité

- **Avantage** : Évite les débats stériles sur les heures, élimine la fausse promesse d'une date de livraison ferme, s'adapte rapidement aux changements.
    
      
    
- **Vélocité** : Somme des _Story Points_ livrés au cours d'un _Sprint_. Permet de prédire le rythme de croisière de l'équipe sans imposer de contrainte arbitraire.
    
      
    

## 4. Points importants à retenir

#### Partie I à III — Cadrage & Réseau

**À retenir :**

  

1. L'estimation d'effort/charge (_LoE_) fournie par les experts ne se négocie pas.
    
      
    
2. Le réseau d'activités s'appuie principalement sur des liaisons **Fin à Début (FS)**.
    
      
    
3. Les jalons (_milestones_) ont une **durée nulle** ($Durée = 0$).
    
      
    
4. La formule PERT Bêta pondère la valeur la plus probable : $t_E = (t_O + 4t_M + t_P) / 6$.
    
      
    

#### Partie IV à VI — Chemin Critique, Optimisation & Agile

**À retenir :**

  

1. Le **chemin critique** est le chemin le plus long du réseau ; sa marge totale est nulle ($Float = 0$).
    
      
    
2. Le **nivellement des ressources** allonge souvent la durée globale du projet.
    
      
    
3. Le **Crashing** (ajout de ressources) et le **Fast Tracking** (parallélisation) réduisent les délais mais augmentent coûts et risques.
    
      
    
4. Selon la **Loi de Brooks**, ajouter des développeurs à un projet logiciel en retard aggrave le retard.
    
      
    
5. L'estimation relative Agile (**Story Points / Planning Poker**) mesure l'effort comparatif et permet de calculer la **vélocité**.
    
      
    

## 5. Liens entre les notions

```
[Lots de travail (WBS)] ──► [Décomposition en Activités]
                                    │
                                    ▼
                     [Ordonnancement PDM (FS, FF, SS, SF)]
                                    │
                                    ▼
               [Estimations des Durées (PERT / Delphi / Paramétrique)]
                                    │
                                    ▼
                    [Calcul du CHEMIN CRITIQUE (Marge = 0)]
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
[Nivellement Ressources]   [Compression (Crashing)]    [Chevauchement (Fast Track)]
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    ▼
                      [ÉCHÉANCIER DE RÉFÉRENCE (Baseline)]
                                    │
                                    ▼ (En cours d'exécution)
                 [Suivi vs Date de Statut (Status Date)]
```

## 6. Pièges et confusions fréquentes

|**Notion A**|**Notion B**|**Différence clé à ne pas confondre**|
|---|---|---|
|**Charge / Effort (LoE)**|**Durée**|La **charge** est la somme de travail en H/J (ex. 10 jours-homme). La **durée** est le temps calendaire nécessaire pour l'exécuter selon les ressources affectées (ex. 5 jours calendaires à 2 personnes).|
|**Marge Totale (_Total Float_)**|**Marge Libre (_Free Float_)**|La **marge totale** est le retard possible d'une tâche sans décaler la **fin du projet**. La **marge libre** est le retard possible sans décaler le **début au plus tôt des successeurs**.|
|**Crashing**|**Fast Tracking**|Le **Crashing** ajoute des ressources (hausse des coûts). Le **Fast Tracking** parallélise des tâches habituellement séquentielles (hausse des risques de réfection/rework).|
|**Provision pour aléas (_Contingency_)**|**Provision pour imprévus (_Management_)**|La **provision pour aléas** couvre les risques connus (_known-unknowns_) et fait partie de la _baseline_. La **provision pour imprévus** couvre les risques inconnus (_unknown-unknowns_) et est hors _baseline_.|
|**Estimation Absolue**|**Estimation Relative**|L'estimation **absolue** donne une métrique temporelle directe (heures, jours). L'estimation **relative** (Story Points) compare la complexité d'une tâche par rapport à une autre.|

## 7. Synthèse finale (ultra-condensée)

La gestion des délais exige rigueur technique et réalisme :

  

1. **Élaboration** : Les activités issues de la WBS sont ordonnancées (méthode PDM) avec des dépendances (majoritairement Fin à Début - FS) et des décalages (_Leads/Lags_).
    
      
    
2. **Estimations** : La charge (_LoE_) ne se négocie pas. Elle est estimée via des avis d'experts (Delphi), des modèles (paramétriques, PERT à 3 points) ou des comparaisons.
    
      
    
3. **Chemin Critique & Optimisation** :
    
      
    - Le **chemin critique** ($Marge = 0$) conditionne la durée minimale.
        
          
        
    - L'optimisation s'effectue par **nivellement** (limites de ressources), **Crashing** (ajout de ressources) ou **Fast Tracking** (parallélisation), en gardant en tête la **Loi de Brooks**.
        
          
        
4. **Restitution & Suivi** : Présentation sous forme de **Gantt** ou **Jalons**, et suivi régulier de la situation réelle par rapport à la **Ligne de Référence (_Baseline_)** à une **Date de Statut**.
    
      
    
5. **Approche Agile** : Utilisation d'**estimations relatives** en **Story Points** via le **Planning Poker** pour calculer la **vélocité** de l'équipe sans créer de fausses promesses calendaires.
    
      
    

## Questions de révision

### Niveau 1 — Compréhension

1. **Règle managériale** : Pourquoi les estimations de charge/effort (_LoE_) ne doivent-elles pas faire l'objet d'une négociation avec le client ou le sponsor ?
    
      
    
2. **Définition** : Qu'est-ce que le chemin critique d'un projet et quelle est la valeur de sa marge totale ?
    
      
    
3. **Typologie** : Citez et définissez brièvement les 4 types de liaisons logiques dans la méthode des précédences (PDM).
    
      
    
4. **Calcul PERT** : Quelle est la formule de la durée estimée ($t_E$) selon la distribution Bêta de PERT ?
    
      
    
5. **Loi célèbre** : Énoncez la Loi de Brooks et expliquez son impact sur la technique du _Crashing_.
    
      
    

### Niveau 2 — Application

1. **Calcul de charge et durée** : Une activité nécessite un effort estimé à 15 jours/homme. Vous y affectez 2 développeurs travaillant à 50 % de leur temps. Quelle sera la durée calendaire minimale de cette activité ?
    
      
    
2. **Calcul de réseau (CPM)** : Soit une séquence de deux tâches $A$ (durée = 4 jours) et $B$ (durée = 6 jours) liées par une relation Fin à Début avec un décalage de retard (_Lag_) de 2 jours. Si $A$ commence au jour 0, quelle est la date de fin au plus tôt ($EF$) de $B$ ?
    
      
    
3. **Exercice PERT** : Pour une activité, l'estimation optimiste est de 4 jours, la plus probable de 7 jours et la pessimiste de 16 jours. Calculez la durée estimée selon la distribution Bêta.
    
      
    

### Niveau 3 — Réflexion / Examen

1. **Analyse comparative d'optimisation** : Un projet prend du retard sur son chemin critique. Comparez l'utilisation du _Crashing_ et du _Fast Tracking_ en termes d'impacts sur les coûts, la qualité et les risques.
    
      
    
2. **Cas pratique Agile vs Prédictif** : Expliquez pourquoi l'utilisation des _Story Points_ et du _Planning Poker_ prévient le piège des dates d'échéance prématurées par rapport aux estimations traditionnelles en jours/hommes.
    
      
    
3. **Mise en situation d'examen** : Lors d'une réunion de suivi à la date de statut, le chef de projet constate qu'une activité n'appartenant pas au chemin critique a subi un retard de 3 jours. Doit-il immédiatement reculer la date de livraison finale du projet auprès du sponsor ? Justifiez votre réponse en mobilisant les concepts de marge totale et de marge libre.