# Qualification Pi / DSH — capacités partielles, préalable strict non satisfait

Date : 2026-09-05. Suite de [L1 bis](2026-09-05-l1bis-outcome.md), après autorisation
de poursuivre. [Rapport et preuves](../evaluations/agent-readiness/report.md),
[critères gelés](../evaluations/agent-readiness/protocol.md),
[évaluation](../evaluations/agent-readiness/assessment.json).

Une erreur de configuration expérimentale est identifiée : les profils précédents
n'envoyaient pas la désactivation de raisonnement Qwen. Les nouveaux profils temporaires
l'envoient effectivement, observé sur les requêtes natives ; aucun réglage utilisateur
n'est modifié. Cela ne démontre pas la cause unique des échecs du pilote passé.

Quatre essais sur une mission distincte : Pi corrige, teste et clôture deux fois ;
DSH une fois, puis se perd dans des diagnostics, écrit hors dépôt et atteint 240 s.
Les quatre codes finaux passent l'oracle indépendant. Le second DSH n'a pas de passage
final de tests réussi dans sa session ni de clôture. Son état corrigé après collecte
ne peut remplacer ces obligations. Les agents sont donc partiellement fonctionnels,
avec une qualification DSH non acquise dans les conditions observées. La charge
concurrente du serveur n’a pas été mesurée : voir la [précision utilisateur sur la
contention](2026-09-05-shared-server-contention.md). Le timeout seul ne diagnostique
pas un défaut de fiabilité du harness.

Le préalable strict 2/2 tous critères n'est satisfait par aucun profil : Pi a une
inexactitude documentaire mineure sur un essai, DSH un échec matériel sur deux.
Conserver ces gravités distinctes. Ne pas transformer les critères après collecte
et ne pas appeler cette mission simple une qualification de mémoire inter-harness.

## Décision de suite

- Maintenir L1 bis clos et sa comparaison MP/M0 inconclusive ; ne pas la réécrire à
  la lumière des nouveaux profils. Aucune nouvelle campagne mémoire lancée ici.
- Avant reprise, confirmer Pi sur la précision documentaire et stabiliser DSH sur
  un autre cas borné inédit avec clôture et respect du périmètre. Distinguer erreurs
  de modèle, orchestration et protections effectives, sans attribuer tout au harness.
- Utiliser les réglages effectifs observés comme candidats expérimentaux uniquement ;
  chaque nouvelle série doit vérifier disponibilité, profils, sources et oracles.
- DSH utilise ici Qwen3.8-27B UD-Q4_K_S, tout comme Pi, et non un modèle DeepSeek.
  Le CLI compilé existant est le véritable harness DSH, aucune substitution Codex.
- Préserver U03, D01–D03, M0 comme référence et MP expérimental. Aucun L2,
  installateur, synchroniseur ou contenu VBB appliqué à la factory.

Les écritures externes DSH sont documentées, leurs artefacts identifiés conservés
puis nettoyés ; état antérieur de ces chemins inconnu. Les réglages globaux suivis
restent identiques. Copies de clés temporaires supprimées, manifest de distribution vide.
