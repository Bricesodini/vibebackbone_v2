# État courant de la conception VBB V2

Mémoire **interne de fabrication**, sans installation VBB sur l'agent concepteur.
V1 reste une source de preuves et d'idées, jamais une autorité pour V2.

## Reprendre maintenant

**Revue rc.5 et compatibilité trois harnesses effectuées :** [revue](evaluations/candidate-rc5-review/report.md), [exécution native exacte](evaluations/candidate-rc5-native/report.md). Aucun modèle actif, secrets nettoyés. [Audit intégral à terminer](evaluations/final-audit/requirements.md) avant clôture du goal.

**Candidat courant rc.5 :** [reprise](handoffs/2026-09-06-goal-progress-rc5.md), [rapport](evaluations/candidate-rc5/report.md). Revue rc.4 réussie sur conservation, deux P3 d’entrée corrigés/testés rc.5. Upgrades réels et retrait exact passent ; revue ciblée rc.5 et audit intégral encore requis.

**Candidat courant rc.4 :** [reprise](handoffs/2026-09-06-goal-progress-rc4.md), [rapport et vérifications](evaluations/candidate-rc4/report.md). Revue rc.3 a trouvé deux interruptions, corrigées/testées rc.4. Nouvelle revue, update réel et audit final encore requis.

**Dernier état :** [lecture après chronologie explicite](evaluations/parcel95-chronology/report.md). Pi/DSH récupèrent les faits essentiels après remédiation déclarée ; imprécisions résiduelles consignées. Profils produit, nouvel artefact exact et revue finale encore à faire.

**Revue de mémoire effectuée :** [bilan remédiation](evaluations/parcel95-remediation/report.md). Décompte corrigé, Pi termine, mais défauts résiduels de provenance/chronologie et portée de manifeste. Nouvelle remédiation ciblée requise ; goal actif.

**Dernière tranche :** [reprise PARCEL-95](handoffs/2026-09-06-goal-progress-parcel95.md), [bilan rc.2 avec harnesses](evaluations/qualification-rc2/report.md). Huit passages réalisés ; retrait exact réussi, fidélité du résumé échouée et lecteur Pi en timeout. Remédiation ciblée encore requise, goal actif.

**Suite active après comparatif :** [reprise rc.2](handoffs/2026-09-06-goal-progress-rc2.md). [six cellules et limites](evaluations/value-2026-09-06/report.md),
[décision noyau ciblé](decisions/2026-09-06-minimal-local-core.md),
[candidat rc.2 local testé mécaniquement](evaluations/candidate-rc2/report.md).
Qualification avec les harnesses et revue finale encore à faire ; goal non accompli.


**Goal long adopté et actif — 2026-09-06.** [Reprise après FRET-62](handoffs/2026-09-06-goal-progress-fret62.md). [État courant](evaluations/integrated-2026-09-06/STATUS.md).
[Qualification privée Pi puis DSH réussie sur calibration](evaluations/integrated-2026-09-06/capability-report.md).
[FRET-62 réalisé puis revu](evaluations/integrated-2026-09-06/report.md) : métier correct, fidélité autonome échouée ; meilleure récupération après revue fraîche, défaut résiduel lecteur. Comparatif et noyau produit encore à établir.
Autorisation conditionnelle produit/cycle de vie adoptée dans la tâche, aucune distribution acquise.


Pour une progression autonome plus longue : [mandat proposé de goal long](handoffs/2026-09-06-long-goal.md).
Ce mandat élargit le démonstrateur vers un candidat produit local ; il doit être repris
explicitement par Brice dans le lancement pour autoriser cette portée supplémentaire.


**Nouvelle session : [handoff du démonstrateur intégré](handoffs/2026-09-06-integrated-demonstrator.md).**
Préparé à la demande de Brice pour lancer la prochaine tranche ; prompt de reprise inclus.
Reprendre le checkout courant : les derniers artefacts ne sont pas encore commités.


Prise de recul demandée par Brice : [proposition de recentrage après U05](plans/implementation-plan.md#proposition-de-recentrage-après-u05--2026-09-05).
Recommandation encore à arbitrer : candidat minimal → mission complète → valeur comparée
→ noyau produit. Aucun nouveau lot produit autorisé par cette proposition.


Dernière tranche : [U05 — deux outils prototypés](decisions/2026-09-05-deterministic-prototype-outcome.md),
[rapport local](experiments/deterministic-tools/report.md) et
[mode d'emploi](experiments/deterministic-tools/README.md). 20 tests passent, zéro appel modèle ;
comparaison agentique et gains encore non évalués.


[Handoff après qualification AGENTS](handoffs/2026-09-05-after-agents-qualification.md) :
réception observée sur trois harnesses, préalable strict de séquence DSH encore à qualifier.
Orientation de Brice : [configurer DSH depuis une référence Pi fonctionnelle](design/dsh-from-pi-reference.md),
en tenant compte de sa developer preview et de sa composition personnalisable.
Option produit à examiner ensuite : [mode natif Vibe Backbone V2](design/vbb-native-mode.md),
encore au stade de conception.
Référence pratique interne : [guide-dsh.md](operations/guide-dsh.md).
L’[ancien handoff](handoffs/2026-09-05-next-session.md) reste la proposition source.

0. [Bilan U04](decisions/2026-09-05-agents-entry-outcome.md),
   [rapport AGENTS](evaluations/agents-common-v2/report.md), puis
   [protocole déterministe seulement préparé](evaluations/deterministic-next/protocol.md).

1. [Bilan courant U03](decisions/2026-09-05-equipped-continuity-outcome.md).
2. [Besoin de mémoire entre harnesses](decisions/2026-09-05-cross-harness-memory.md),
   [conception](design/cross-harness-memory.md) et [plan du pilote](plans/cross-harness-memory-pilot.md).
3. [Paire M0/MP réellement équipée](evaluations/continuity-equipped/report.md), puis
   [résultat final après revue bornée](evaluations/continuity-reviewed/report.md).
4. [Mode opératoire interne](operations/cross-harness-continuity.md).
5. Propositions demandées pendant la collecte : [AGENTS.md commun](design/agents-entry-point.md),
   [opérations déterministes](design/deterministic-continuity.md) et
   [recherche Backbone-know / VBB / mattpocock](research/2026-09-05-deterministic-continuity/review.md).

## État et limites

U05 : les commandes internes `compare` et `inventory` existent et sont testées localement.
Elles mesurent des fichiers et références explicitement sélectionnés ; complétude du
mandat et autorité restent non vérifiées. Aucun contrat L2 ou outil distribué.


U04 : les neuf sondes de loader du second gel produisent les bons marqueurs sans outil ni
mutation ; réception native visible pour Pi/DSH, comportement compatible pour Codex.
**Qualification stricte non acquise** : le plugin de titre DSH lance une requête concurrente,
malgré l'ordre séquentiel des processus. Phase mémoire non exécutée ; aucun gain de
continuité établi. Premier gel conservé avec six indisponibilités dues au conducteur.
Les copies privées de clés sont nettoyées. Aucun nouveau modèle lancé après le constat.


L0 terminé ; L1 et L1 bis historiques exécutés et clos. Le nouveau pilote équipé
observe deux chaînes Codex → Pi → DeepSeek Harness → lecteur DSH neuf : création,
transmission, actualisation et conservation de documents réellement produits.
Pi bénéficie d'un reviewer réel via le paquet déjà présent ; aucun plugin global installé.
Codex utilise gpt-6-astra low ; Pi et DSH **Qwen3.8-27B local off**, pas un modèle DeepSeek.

Les huit essais de la paire terminent et passent les oracles métier, mais les deux
cycles échouent aux critères stricts : écritures externes, perte de Git par le conducteur,
inexactitudes de compte rendu ou de lecture. Les corrections séparées stabilisent la
protection native et l'exécution DSH. La dernière revue guidée corrige trois problèmes,
conserve exactement l'historique et permet leur reprise, avec une erreur résiduelle de
lecture. **Fonctionnement technique observé sur ce cas ; fidélité autonome complète
non qualifiée ; valeur ajoutée MP inconnue.** M0 reste une référence, pas une garantie.

Les questions AGENTS.md et outils déterministes sont documentées comme propositions,
sans adoption produit. Les loaders ne sont pas supposés identiques ; les contrôles
mécaniques ne créent ni approbation ni autorisation. Leurs gains restent à mesurer.
**L2, installateur et qualifications L3–L8 restent différés ; distribution vide.**

Contrainte persistante de Brice : **modèles strictement séquentiels, jamais parallèles**.
Après timeout, vérifier fin/annulation côté serveur avant le suivant ; si impossible,
suspendre et expliciter. Un serveur inactif observé n'est pas une réservation exclusive.
Une indisponibilité native reste un résultat ; aucune substitution par plusieurs Codex.

## Preuves et historique de conception

- Collectes récentes : [équipé](evaluations/continuity-equipped/report.md),
  [confinement initial et shell indisponible](evaluations/continuity-confined/report.md),
  [reprise DSH compatible](evaluations/continuity-confined-v2/report.md),
  [rectification et conservation](evaluations/continuity-reviewed/report.md).
- Pi : [inventaire des packages](research/2026-09-05-pi-equipment/review.md), puis équipement
  expérimental dans la collecte ci-dessus. L'inventaire antérieur n'est pas réécrit.
- Préalables : [qualification séquentielle](evaluations/agent-readiness-sequential/report.md),
  [suite ciblée](decisions/2026-09-05-sequential-readiness-outcome.md),
  [qualification initiale](evaluations/agent-readiness/report.md),
  [bilan initial](decisions/2026-09-05-agent-readiness-outcome.md),
  [contention partagée](decisions/2026-09-05-shared-server-contention.md).
- Pilotes clos : [L1 bis](evaluations/l1bis/report.md),
  [capacités initiales](evaluations/l1bis/preflight/capabilities.md),
  [bilan L1 bis](decisions/2026-09-05-l1bis-outcome.md),
  [L1](evaluations/l1/report.md), [bilan L1](decisions/2026-09-05-l1-outcome.md).
- Fondations : [plan](plans/implementation-plan.md), [architecture](design/architecture.md),
  [mémoire](design/memory.md), [décisions D01–D03](decisions/2026-09-05-scope-and-architecture.md),
  [audit V1](research/2026-09-05-implementation-planning/v1-audit.md),
  [harnesses](research/2026-09-05-implementation-planning/harnesses.md),
  [revue fondatrice](research/2026-09-05-foundational-review/README.md).

Les résultats antérieurs sont conservés sans requalification rétroactive. Charger les
seuls documents requis par la tranche ; les traces brutes ne sont pas le contexte de
démarrage. Le brief reste une entrée de conception. Les anciens « runtime V2 » et
roadmaps du dépôt vibebackbone sont legacy V1, pas le canon de cette factory.
