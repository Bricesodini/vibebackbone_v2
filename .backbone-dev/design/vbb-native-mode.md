# Mode Vibe Backbone V2 — option de conception

Statut : idée proposée par Brice après la stratégie Pi → DSH, le 2026-09-05.
Aucune adoption d'architecture, implémentation L2, installation ou distribution autorisée
par cette note. Elle précise l'idée pour une décision ultérieure.

## Usage envisagé

L'utilisateur choisit un mode « Vibe Backbone V2 » dans un harness compatible. Dans DSH,
ce mode pourrait prendre la forme d'un profil natif qui assemble les capacités nécessaires
à la continuité : démarrage sur AGENTS, outils de travail, mémoire documentaire et
configuration des appels modèles. La developer preview et la composition par plugins
permettent d'étudier cette forme ; l'existence d'un mode qualifié reste à démontrer.

Le premier candidat peut être configuré depuis une référence Pi fonctionnelle selon la
[stratégie proposée](dsh-from-pi-reference.md), puis vérifié sur le vrai DSH. L'expérience
n'exige pas de construire dès maintenant un mode symétrique dans chaque harness.

## Répartition candidate

| Élément | Responsabilité |
|---|---|
| Accord commun VBB | Besoins de continuité, autorité des sources, obligations de transmission et limites |
| AGENTS du projet | Pointeurs et consignes adaptés au projet, respect de ses instructions existantes |
| Documents du projet | Mandat, canon, décisions, mémoire produite, preuves et historique conservé |
| Profil natif DSH « VBB V2 » | Composition des capacités et réglages nécessaires au besoin : loader, outils, appels auxiliaires, limites et retries |
| Protections natives | Permissions et confinement effectivement imposés et vérifiés sur l'environnement |
| Qualification interne | Versions, composition, capacités observées, écarts et indisponibilités explicites |

Le profil peut désactiver le titre LLM automatique et les appels concurrents inutiles,
fixer les limites/retries, conserver le loader AGENTS et fournir les outils nécessaires.
La séquence stricte est ici une contrainte explicite de Brice ; décider séparément si elle
est un réglage par défaut du futur produit ou une politique propre à un déploiement.
Un reviewer est configuré seulement si le mandat l'exige et si sa capacité est qualifiée.

Un mode actif ne vaut ni approbation métier, ni permission supérieure, ni preuve de
clôture. AGENTS ne remplace pas une sandbox. Les états « configuré », « vérifié sur ce
profil » et « contrôle indisponible » doivent rester distincts. Le mode ne doit pas
annoncer une conformité globale à partir de sa seule sélection.

## Questions de décision

- Le mode est-il un profil DSH natif entretenu par VBB, ou un exemple de configuration
  accompagné d'une qualification ? Examiner le coût d'entretien avant de choisir.
- Quel minimum de capacités mérite le nom VBB V2, et lesquelles restent optionnelles ?
- Comment adapter l'accord à un projet existant sans écraser son autorité ou ses règles ?
- Comment indiquer les versions compatibles, l'état de qualification et une régression
  après une mise à jour de DSH en developer preview ?
- Comment maintenir un accord commun avec des adaptations propres à Pi, Codex ou DSH,
  sans imposer l'architecture d'un harness aux autres ?

## Progression proposée

D'abord qualifier un profil DSH expérimental isolé, configuré depuis les capacités Pi
prouvées ; puis qualifier la création, l'actualisation et la reprise de mémoire. Ces
preuves permettront de décider ce que le mode apporte au-delà d'une configuration
ordinaire et quel coût il impose. Les opérations déterministes restent une tranche
séparée, actuellement au seul stade de protocole.

Si une décision produit retient ensuite ce mode, définir son contenu distribuable,
ses adaptations natives et ses vérifications à partir des besoins V2. Les scripts de
collecte, fixtures, oracles privés, traces et homes de la factory restent hors distribution.
Le concepteur n'active pas ce mode sur lui-même ; aucun installateur n'est nécessaire
pour étudier cette option.

## Documentation de référence du mode

Brice propose un `guide-dsh.md` dans le dépôt. Une première référence existe dans la
factory : [guide interne DSH](../operations/guide-dsh.md). Elle explique la composition,
la préparation depuis Pi, les capacités observées et leur qualification. Un futur guide
pour les projets consommateurs pourrait être pointé par AGENTS lorsque le travail passe
par DSH ; son contenu distribuable serait défini séparément, sans les artefacts internes.
Le guide documente le profil ; il ne l'installe pas et ne prouve pas son activation.
