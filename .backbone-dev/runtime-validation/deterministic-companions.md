# Instructions et outils déterministes — branche active

2026-09-06. Brice rappelle explicitement que les outils déterministes adjoints à AGENTS.md font partie de la piste Backbone Know. Cette branche est active dès la préparation suivante ; elle n'est pas conditionnée à l'échec d'une autre campagne entière d'instructions seules. Le constat « faits déjà exposés » écarte un diagnostic automatique de panne de stockage, pas l'intérêt d'un contrôle mécanique des assertions et références.

G2 reste une proposition non gelée. Avant de lancer ses44 sessions, comparer les rôles possibles et matérialiser les vérifications déterministes pertinentes sur des fixtures privées. Aucun outil expérimental installé dans la factory ni ajouté silencieusement à rc.7 ; aucune ancienne évaluation modifiée.

## Frontière de responsabilité

AGENTS.md oriente vers le mandat, les sources et les outils disponibles. L'accord précise les obligations de conduite. Un outil constate des propriétés explicites et reproductibles ; l'agent interprète la portée, suit les références métier et restitue sa conclusion. Un succès mécanique ne constitue ni compréhension, ni complétude sémantique, ni autorisation. L'outil ne lance pas de modèle, ne répare pas de mémoire et ne décide pas quelle proposition adopter.

| Défaut / besoin | Mécanisme candidat | Réemploi existant et limite |
|---|---|---|
| Référence déclarée absente malgré fichier présent | Vérification explicite de chemins et candidats | inventory sait déjà rapporter présence/absence/ambiguïté ; commencer par ce réemploi avant nouvelle commande |
| Preuve attribuée à des octets différents ou référence devenue périmée | Révision SHA256 et ancre exacte, bornes UTF-8 | compare couvre identité de fichiers ; ancres Know apporteraient une granularité de passage. Pas preuve de genèse ou de vérité |
| Passage déplacé | Recherche exacte, puis proposition de relocalisation avec ambiguïtés conservées | Prototype Know disponible ; ne pas adopter son seuil fuzzy ni promouvoir le candidat automatiquement |
| Élément requis absent d'une sélection déclarée | Différence entre identifiants d'exigences déclarées et éléments référencés | Contrôle d'ensemble déterministe possible ; la qualité de l'extraction des exigences et le sens des liens restent à évaluer séparément |
| Prédécesseur mémoire perdu dans la restitution | Références de filiation explicites vérifiées, sans imposer de dossier | Vérifier ce qui est déclaré ; ne pas reconstruire une filiation à partir des seuls noms/mtime |

## Prochaine expérimentation à préfixer

1. Cartographier précisément ce que compare/inventory peuvent déjà vérifier sur les erreurs G1/D1 et ce qu'ils ne peuvent pas détecter. Réutiliser leurs sorties brutes sans fabriquer de preuve autonome agent.
2. Prototype privé minimal uniquement pour la différence manquante : contrôle de références/ancres ou couverture déclarée. Fixtures avec référence valide, absente, ambiguë, révision périmée, ancre invalide et exigence déclarée non couverte. Oracle écrit avant exécution, aucune réparation automatique, zéro appel modèle. Les résultats sont ceux d'un mécanisme, pas d'une reprise autonome.
3. Préfixer un diagnostic consommateur comparant le même contrat avec et sans le contrôle déterministe pertinent, documents et rôles identiques. Exposer les instructions d'utilisation nécessaires et les compter dans le traitement ; ne pas attribuer artificiellement tout l'effet au seul algorithme. Inclure temps, coûts de préparation, appels d'outil, erreurs détectées, fausses alertes et erreurs restantes.
4. Décision de rôle et de frontière à partir des preuves, puis gel métier/confirmations neufs. Si le produit évolue, nouvelle archive et requalification exacte. Aucune réduction des dix critères ni substitution de lecteur pour conclure.

Les algorithmes Know sont des prototypes et preuves à examiner, jamais une autorité V1. Un simple contrôle local peut être pertinent sans importer PostgreSQL, un moteur de contexte ou un service mémoire. Inversement, sa simplicité ne prouve pas son utilité : celle-ci doit apparaître dans les erreurs évitées ou détectées, avec des limites publiées.
