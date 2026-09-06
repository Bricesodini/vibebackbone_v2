# Candidat local rc.2 — qualification mécanique

Archive exacte : SHA256 `220aed795dc8bca30f4b58f630bcf6f75e96fbd1cc28dad5b4cd4fb61b067ef7`. Six fichiers distribués uniquement. Product/ correspond à cette archive. **Qualification avec les trois harnesses encore à faire ; pas de RC finale acquise.**

Le noyau découle du [comparatif](../value-2026-09-06/report.md) : compare/inventory, aide autonome, consigne courte optionnelle de continuité, cycle de vie local attribuable. Aucun moteur d'exécution, schéma mémoire imposé, spécialiste installé ou troisième outil de continuité.

## Revue fraîche et correction

Le reviewer Codex neuf a examiné rc.1 en lecture seule et trouvé trois défauts par les chemins de code ; ses essais dynamiques ont échoué dans sa sandbox, limite qu'il déclare. L'évaluateur les a ensuite reproduits sur l'archive rc.1 : trois échecs attendus dans `../candidate-rc1/reproductions.txt`.

rc.2 corrige : empreinte initiale d'AGENTS pour retrait d'une installation interrompue avant son écriture ; journal du résultat attendu pour reprendre un retrait interrompu après remplacement AGENTS ; mode POSIX et ownership préexistants préservés par le remplacement (refus si changement d'ownership requis impossible). ACL étendues non qualifiées, explicitement limitées. Les nouveaux champs de reçu sont additifs ; un reçu ancien installé peut être mis à jour/retiré, les états pending de rc.1 sans empreinte initiale ne sont pas rétroactivement certifiés.

Le wrapper des mesures désactive aussi le cache bytecode à l'import, afin qu'une invocation sans `-B` n'ajoute pas de résidu `.vbb/__pycache__`. Aucune archive rc.1 écrasée ; le builder refuse désormais de remplacer une archive de même version avec d'autres octets.

## Vérifications réalisées

- 20 tests lifecycle sur l'archive extraite, dont les trois régressions de revue, plus 3 tests de frontière : tous passent.
- 20 oracles historiques de mesure exécutés sur le **module produit extrait** : tous passent, pas seulement sur l'ancien prototype.
- CLI réel : install/répétition/inspect/compare égal et différent/retrait/répétition ; mémoire et AGENTS utilisateur byte-identiques après retrait.
- Mise à jour **réelle rc.1 → rc.2**, puis mesure sans `-B` et retrait avec mémoire conservée : [résultat](real-upgrade.json).
- [Validation locale](local-validation.json) : membres archive, SHA, sorties CLI, égalité sources/archive. Pas de publication ou installation factory.

## Restant

Nouvelle mission exacte avec erreurs remédiables, canon spécialisé choisi, décision remplacée, retour tardif, transmission Git, outils et lecteur neuf ; trivial sur trois harnesses et reprise après retrait. Revue du candidat final (y compris éventuelles corrections et profils documentés), bornes natives et limites de fidélité. Le goal reste actif.
