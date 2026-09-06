# Décisions de cadrage et d'architecture — 2026-09-05

Mémoire interne. Ce registre n'est pas une politique appliquée à l'agent de conception.

## U01 — Autorisation de poursuivre jusqu'au plan complet

**Statut : décision utilisateur explicite.** Brice demande de continuer vers « un plan complet pour la mise en œuvre de vibebackbone v2 » et de ne revenir que pour des questions d'architecture. Dans le contexte de la clôture de phase 1, cela autorise l'audit V1 précédemment préparé et la conception du plan. Cela ne demande pas d'installer le produit, de modifier V1 ou de mettre en œuvre V2 dans cette session.

La phase 1 conserve son statut historique `V1_INSPECTED = NO`. La phase actuelle a inspecté V1 en lecture seule. Le chemin identifié est `[LOCAL_PATH]`.

## D01 — Cadre léger, contrôles natifs

**Statut : décision d'architecture utilisateur explicite.** À la question opposant cadre léger et contrôle technique de chaque action par VBB, Brice a choisi : **« Cadre léger, contrôles natifs des harnesses »**.

Conséquences :

- VBB aide à conserver mandat, décisions, mémoire utile et preuves.
- L'exécution, les permissions, le scheduling et les sessions restent chez les harnesses.
- Aucun registre de transactions d'actions, arbitre de chaque tool call, reprise automatique d'effets après crash, scheduler ou boucle d'agent centrale dans VBB.
- Un utilitaire local de préparation, d'inspection et de validation documentaire reste compatible avec ce choix ; il ne pilote pas l'exécution du travail.
- Aucune équivalence des garanties de sécurité entre harnesses n'est présumée.

Motifs : réponse utilisateur ; chevauchements externes ; coût des anciennes expériences de contrôle d'action observé dans V16. Cette décision n'est pas la conclusion d'un benchmark comparatif du futur V2.

Réouverture uniquement si un cas d'usage exige réellement une garantie transactionnelle absente du harness et de l'infrastructure. Ce serait alors un autre périmètre architectural à arbitrer, pas une extension discrète du noyau.

## D02 — Codex, Pi et DeepSeek Harness dans l'étude et le plan

**Statut : exigence utilisateur explicite.** Brice demande d'élargir la comparaison à Pi et DeepSeek Harness. Les trois sont donc des cibles de qualification prévues. « Prévu » n'est pas « support déjà validé » ; chaque profil aura ses versions et capacités testées.

## D03 — Mémoire durable, sélective et provenance du canon

**Statut : exigence utilisateur explicite.** Brice demande d'évaluer et formaliser la mémoire de session interagents, sans noyer les agents et en identifiant canonique et legacy.

Le besoin est retenu. La solution détaillée dans [memory.md](../design/memory.md) est une proposition de conception : mémoire projet portable, chargement progressif, références vers le canon choisi, résultats d'agents séparés, intégration contrôlée et invalidation explicite. Aucune mémoire native globale n'a été lue, importée ou modifiée pour réaliser ce travail.

## Choix délégués retenus pour le plan

**Statut : décisions de conception proposées par l'agent dans le mandat de planification**, non promues en règles produit validées.

| ID | Choix | Justification / condition de révision |
|---|---|---|
| D04 | Un point d'entrée VBB, activation explicite pour la mission ; adoption persistante projet optionnelle | Éviter les fausses activations V09 ; conserver l'autonomie une fois mission autorisée |
| D05 | Artefacts projet ordinaires, pas de base globale de mémoire ni de moteur vectoriel | Besoin interagents portable ; POC possible sans service supplémentaire |
| D06 | Référencer les specs et décisions existantes ; aucun canon parallèle de leur contenu | Conflits de couches et dérive V03/V14 ; spécialiste ne devient pas autorité par sa présence |
| D07 | Un rédacteur d'intégration par mission, retours distincts par agent | Prévenir les écrasements ; pas de protocole distribué de consensus |
| D08 | Premier transport commun par skill projet direct ; pas de plugin exécutable nécessaire au MVP | Chemin commun documenté pour les trois harnesses ; conserver les wrappers natifs comme option tardive |
| D09 | Outillage léger Python 3.11+, JSON UTF-8, validation JSON Schema avec dépendance épinglée | Pas de parsing Markdown ad hoc ni de Node service ; versions exactes verrouillées dans L2 |
| D10 | Installation locale au projet uniquement, sans modification globale ou hook automatique | Réduire le périmètre de propriété et le coût de retrait |
| D11 | Qualification comportementale et documentaire ; aucune certification universelle ou A0/A1/A2 | V05/V07/V11/V12 montrent les limites des labels et oracles |
| D12 | Réévaluer la valeur après pilote, retirer tout mécanisme sans bénéfice | Préserver l'alternative native M0 de la revue fondatrice |

Les références Vxx sont résolues dans [l'audit V1](../research/2026-09-05-implementation-planning/v1-audit.md). Ces choix rendent le plan concret ; une ambiguïté d'implémentation courante se résout dans la tranche, sans transformer chaque ligne en demande d'approbation.

## U02 — GO réalisation L0 puis L1

2026-09-05, instruction explicite de Brice dans la tâche de réalisation :
« Exécute d’abord L0, puis L1, en gardant M0 comme baseline loyale et en
considérant la valeur réelle du cadre comme une hypothèse à démontrer, pas
comme un acquis. » Frontière confirmée : VBB garde mandat, continuité, mémoire
et preuves ; les harnesses gardent exécution, permissions et isolation.
L2 et l'installateur ne sont pas à anticiper sans justification par L1.
Les détails d'implémentation peuvent s'adapter aux preuves ; seule une
contradiction structurelle insoluble dans le modèle justifie une réouverture.
Cette transcription conserve l'autorisation de cette tâche, sans autoapplication.
