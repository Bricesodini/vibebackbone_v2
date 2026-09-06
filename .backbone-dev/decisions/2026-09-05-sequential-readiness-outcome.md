# Suite séquentielle — DSH qualifié sur cas simple, fidélité documentaire Pi à confirmer

2026-09-05. [Rapport](../evaluations/agent-readiness-sequential/report.md),
[protocole gelé](../evaluations/agent-readiness-sequential/protocol.md),
[évaluation](../evaluations/agent-readiness-sequential/assessment.json).

Quatre essais successifs sur un cas inédit ; tous corrigent, testent et clôturent
normalement. Trois observations de slots entièrement inactifs avant et après chaque
essai, timestamps contrôlés entre essais. Budget 600 s fixé avant collecte, aucun
timeout de mission. La charge externe reste inconnue : /metrics indisponible, deux
lectures /slots expirées pendant DSH-2, appels auxiliaires internes DSH observés.
Aucune conclusion causale sur la contention passée.

DSH satisfait 2/2 tous critères sur ce cas simple. Pi accomplit 2/2 cycles opérationnels,
mais 1/2 strict : le premier compte rendu surestime la capacité du test ajouté à détecter
un tri. Ce test passe l'ancien code fautif ; le test existant détecte néanmoins le bug.
Le code final et la suite passent les contrôles. Réserve documentaire spécifique,
pas panne de Pi, ni absence d'agent fonctionnel.

Suite : confirmer la fidélité documentaire Pi aux preuves sur une mission ciblée
inédite, en conservant les critères et l'observation séquentielle. Ne pas relancer
une qualification générale DSH sans nouvelle raison. Une future campagne mémoire
reste distincte et devra évaluer son cycle complet ; elle n'est pas exécutée ici.
Les séries historiques restent closes et intactes, et L1 bis inconclusif.

Aucune promotion MP, aucune preuve de suffisance générale M0, aucun L2 ou installateur.
Profils candidats uniquement dans l'expérience. Réglages globaux inchangés, copies de
clés retirées, manifest de distribution vide. Les deux harnesses utilisent Qwen3.8-27B
UD-Q4_K_S ; aucune substitution par plusieurs sessions Codex.
