# Vibe Backbone V2 — candidat local rc.5

Factory de conception, jamais un projet consommateur. V1 reste une source de preuves, pas une autorité. Aucun produit installé ici.

## Reprendre maintenant

**Nouvelle session demandée :** [validation runtime avec sous-agents sur le site brouillon, puis entrée en phase 2](handoffs/2026-09-06-runtime-validation-phase2.md). Nouveau mandat à lancer avec le prompt du handoff ; l’ancien goal rc.5 ne valide pas ce nouveau périmètre. Remote public fourni, aucune synchronisation effectuée lors de la préparation.

Le candidat minimal local est construit et son audit de qualification est satisfait dans une portée expérimentale explicite.

- [Livraison et essai local](handoffs/2026-09-06-local-candidate-delivery.md).
- [Audit exigence par exigence](evaluations/final-audit/verdict.md), [contrôles consolidés](evaluations/final-audit/checks.json).
- [Archive rc.5](releases/vbb-0.1.0-rc.5.tar.gz), SHA256 `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`.
- [Qualification mécanique](evaluations/candidate-rc5/report.md), [revue ciblée](evaluations/candidate-rc5-review/report.md), [trois harnesses sur rc.5](evaluations/candidate-rc5-native/report.md).

## Portée et réserves

Deux mesures en lecture seule, accord court optionnel, mémoire ordinaire et cycle de vie local réversible. Exécution/permissions/sessions natives. Les outils ne certifient ni autorité, ni mandat, ni complétude. Aucun moteur modèle, aucune méthode spécialisée installée, aucun global/push/publication.

Les erreurs des lectures locales restent conservées. Une reprise fidèle est prouvée après remédiations déclarées, pas une autonomie universelle sans revue. [Lecture indépendante finale](evaluations/final-memory-reader/report.md). Le [comparatif](evaluations/value-2026-09-06/report.md) justifie une utilité instrumentale bornée, aucune économie globale de temps/tokens.

Tous les travaux restent dans ce checkout, y compris les modifications préexistantes non commitées. Préserver les archives/gels et preuves échouées. L'adoption sur projets réels ou publication demanderait une portée nouvelle.

## Conception et historique

[Mandat adopté](handoffs/2026-09-06-long-goal.md), [décision noyau minimal](decisions/2026-09-06-minimal-local-core.md), [plan](plans/implementation-plan.md).

[PARCEL-95 et ses remédiations](handoffs/2026-09-06-goal-progress-parcel95.md), [évolution rc.5](handoffs/2026-09-06-goal-progress-rc5.md).

[L'ancien INDEX intégral](INDEX-before-final-audit.md) conserve les pointeurs historiques ; ses états « à faire » sont datés de leurs tranches et ne remplacent pas le présent audit.
