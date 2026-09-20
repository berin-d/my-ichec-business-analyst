
## 1. Définir l'exigence (vs Besoin et But)

- Une exigence est l'énoncé d'une capacité que le futur système doit posséder pour répondre à un objectif, ou d'une contrainte qu'il doit impérativement respecter.
    
- Elle se distingue nettement du "besoin" (qui est une attente encore informelle et imprécise) et du "but" (qui est une notion de haut niveau souvent trop vague).
    
- Pour être exploitable, une exigence doit être documentée, concrète et techniquement implémentable avec les technologies disponibles.


----
## 2. Le "Quoi" contre le "Comment"

- L'ingénierie des exigences se concentre sur le domaine d'application et le "Quoi" : elle définit les effets du système sur son environnement et les attentes des utilisateurs.
    
- C'est un travail porté généralement par le "Business Analyst", dont la mission est de "construire le bon système" (_Building the Right System_).
    
- À l'inverse, l'ingénierie logicielle (la conception et l'implémentation) se focalise sur le "Comment" : la structure interne et les choix technologiques de la solution.
    
- Ce volet est géré par l'équipe technique (architectes, développeurs) dont le but est de "bien construire le système" (_Building the System Right_) en assurant fiabilité et qualité du code.


---
## 3. La taxonomie des exigences (Les 4 niveaux)

> les exigences s'articulent selon une hiérarchie précise, maintenue par des mécanismes de traçabilité :

- **Les exigences du domaine :** Ce sont les énoncés prescriptifs liés aux processus métiers et objectifs de l'entreprise (ex: un professeur emprunte 3 livres maximum).
    
- **Les propriétés du domaine :** Ce sont des énoncés descriptifs qui restent vrais en toute circonstance, indépendamment du système (ex: un livre ne peut être prêté à deux personnes simultanément).
    
- **Les exigences utilisateurs :** Elles décrivent le comportement externe attendu du logiciel (ex: le système doit permettre d'enregistrer 3 prêts pour un professeur).
    
- **Les spécifications techniques :** Elles traduisent ces attentes en termes de fonctionnement interne (tables, bases de données, routines).


----
## 4. Exigences Fonctionnelles vs Non-Fonctionnelles

- **Fonctionnelles :** Elles décrivent une fonctionnalité liée aux processus d'affaires et au traitement des données.
    
- **Non-fonctionnelles :** Elles définissent des contraintes ou qualités globales du système (sécurité, performance, ergonomie, maintenabilité).
    
- Il est crucial de ne pas négliger les exigences non-fonctionnelles au début du projet ; par exemple, une mauvaise ergonomie sur un premier prototype peut amener les utilisateurs à percevoir l'application comme défaillante et bloquer leur adhésion.


---
### Questions de réflexion

1. **Gérer la traçabilité :** Lorsqu'une règle métier fondamentale évolue (une _exigence du domaine_), comment un Business Analyst et un Architecte Technique peuvent-ils s'assurer que toutes les _spécifications techniques_ correspondantes sont mises à jour sans en oublier ?
    
2. **Priorisation :** Si un projet a un budget très restreint, comment arbitrer entre le développement de nouvelles _exigences fonctionnelles_ et le respect strict d'_exigences non fonctionnelles_ (comme la performance ou l'ergonomie parfaite) ?
    
3. **Le rôle du Business Analyst :** Face à un client qui exprime un simple "besoin" très flou (ex: "Je veux que le système soit plus rapide"), quelles techniques d'investigation le Business Analyst doit-il utiliser pour transformer ce besoin informel en une véritable "exigence non-fonctionnelle" quantifiable et implémentable ?


----

## Outils et sources concrètes

- Référence et modélisation
Source : [iiba.org/standards-and-resources/babok/](https://www.google.com/search?q=https://www.iiba.org/standards-and-resources/babok/&utm_source=gemini)
Outils associés : [Lucidchart](https://www.lucidchart.com?utm_source=gemini) ou [Draw.io](https://app.diagrams.net/?utm_source=gemini)

- Outils de gestion du cycle de vie des exigences
Lien : [atlassian.com/software/confluence](https://www.atlassian.com/software/confluence?utm_source=gemini)
Lien : [ibm.com/products/requirements-management](https://www.ibm.com/products/requirements-management?utm_source=gemini)