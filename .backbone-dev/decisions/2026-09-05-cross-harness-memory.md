# U03 — Priorité : exploiter un même projet depuis plusieurs harnesses

Statut : besoin utilisateur explicite ; propositions d'expérimentation ci-dessous
à distinguer de ce besoin. Cette note complète D03 et la décision L1, sans modifier
les résultats figés du pilote. Source : précision de Brice dans la tâche de
réalisation, après la proposition de L1 bis.

## Besoin exprimé

Brice précise que la question centrale est l'exploitation de travaux de développement
par plusieurs harnesses : Codex, Pi et DeepSeek Harness. Malgré leurs mémoires de
session propres, le projet doit conserver une documentation canonique identifiable,
les éléments importants du travail et une mémoire exploitable des artefacts et des
sessions. Il demande d'intégrer ces points à VBB V2.

Le besoin de continuité entre outils est établi par l'usage souhaité ; il n'est pas
conditionné à la démonstration préalable d'une défaillance de Codex utilisé seul.
Ce qui reste hypothétique est la valeur du mécanisme VBB par rapport à des documents
projet ordinaires bien entretenus, partagés entre ces mêmes outils.

## Conséquence sur la lecture de L1

Le pilote L1 a comparé un skill généraliste à M0 sur un seul harness. Il n'a évalué
ni passage effectif entre harnesses, ni production progressive d'une mémoire projet.
Le retrait de ce candidat reste justifié à ce périmètre. Il ne tranche pas la valeur
d'une mémoire portable et ne retire pas ce besoin du produit envisagé.

La proposition précédente « éprouver M0 seul puis chercher une défaillance » est
réorientée : comparer M0 et une convention documentaire minimale sur un véritable
cycle de travail entre harnesses. M0 garde l'accès aux mêmes faits et aux moyens
ordinaires de documentation et de transfert du projet.

## Frontière maintenue

VBB peut organiser les références canoniques, l'état de mission, la provenance des
contributions et les preuves réutilisables. Les sessions brutes restent gérées par
les harnesses ; elles constituent des traces consultables, pas un canon commun.
L'information indispensable à une reprise doit être disponible dans les artefacts
portables, même si le journal natif d'origine n'est pas accessible au nouvel outil.

Aucun import exhaustif des conversations, stockage global, synchroniseur de sessions,
ou moteur d'exécution n'est décidé. Les modalités de travail entre copies/Git restent
celles du projet. La mémoire ne synchronise pas les fichiers ni les effets d'actions.

## Suite de conception

[Exploitation de la mémoire portable](../design/cross-harness-memory.md) précise le
cycle attendu. [L1 bis proposé](../plans/cross-harness-memory-pilot.md) cible cette
hypothèse. Ces documents sont internes ; aucun mécanisme n'est installé ni évalué
live par cette clarification. L2 et l'installateur restent différés. D01–D03 ne sont
pas rouverts : la précision porte sur la priorité et la preuve à rechercher.
