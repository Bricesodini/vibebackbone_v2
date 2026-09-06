# Validation runtime et entrée phase 2 — mandat actif

Mandat du 2026-09-06 adopté : ../handoffs/2026-09-06-runtime-validation-phase2.md.
Verdict actuel : **NOT_READY**, qualification en cours. Aucun critère du nouveau goal n'est satisfait par simple héritage de l'audit rc.5.

## Conservation et séparation

Inventaire initial privé : `[PRIVATE_CAMPAIGN]/factory-initial.json` (7176 entrées, 129718813 octets, métadonnées Git comprises), statut Git et patch des changements préexistants conservés à côté. Site original : cinq fichiers, snapshot privé vérifié octet pour octet. Aucun Git créé dans le source. Les traces, captures, source du brouillon et oracles sont exclus de publication par défaut.

L'historique local contient déjà des traces brutes : un push de cette branche publierait aussi ses ancêtres. La sauvegarde publique utilise un export Git séparé à historique initial propre, sans réécriture/suppression de l'historique privé ; provenance et manifeste explicites. Le distant fourni est accessible, sans références lors du premier ls-remote. Push non encore effectué.

## Travail commencé

Un vrai sous-agent concepteur de tests, contexte neuf, a terminé seul ; coordinateur en attente native pendant son exécution. Livrables privés sous `test-design/` : diagnostic, missions, oracles, couverture. Aucun worker consommateur lancé. Proposition non gelée : trois tâches x deux conditions puis deux confirmations x deux conditions ; routes entre les trois harnesses. Diagnostic rendu, budgets/profils effectifs et scripts exécutables restent à fixer avant gel.

La portée vise les routes exactes de la matrice, pas toutes les combinaisons tâche/harness. Les sessions fraîches Pi/DSH ne seront pas appelées sous-agents. La coordination de fabrication et la délégation consommateur auront des preuves séparées.

## Prochaines obligations

Consolider L0–L8 et R01–R12/S01–S20 ; sauvegarde publique sélectionnée et SHA distant vérifié ; diagnostic navigateur ; préflight des profils/permissions/séquence ; gel des tâches et confirmations ; collecte comparative ; corrections et nouveau gel si nécessaire ; qualification du paquet exact ; revue fraîche ; dossier phase 2. Toutes restent ouvertes tant que leurs preuves ne sont pas acquises. Aucun déploiement, installation factory ou méthode spécialisée autorisés par ce fichier.
