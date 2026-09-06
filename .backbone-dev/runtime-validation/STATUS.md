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

## Point de reprise après sauvegarde contrôlée — 09:14 Europe/Paris

Sauvegarde initiale effectivement poussée sur `codex/public-runtime-validation`, SHA distant vérifié `c359aeec55895c91781c33acd3498aec7f9a1944`. 81 fichiers explicites, scan historique gitleaks zéro finding, 7 documents expurgés de chemins/endpoints privés ; provenance dans PUBLICATION.json de l'export. Le checkout factory possède maintenant origin autorisé, mais **ne pas pousser sa branche historique** : elle contient des traces privées. Réutiliser le dépôt d'export privé `public-export/`, recontrôler sélection et manifestes à chaque synchronisation. Les inventaires privés initiaux/exclusions sont intacts.

Deux sous-agents de fabrication ont réellement terminé, séparément : runtime_test_designer et public_backup_reviewer. Attentes natives du coordinateur pendant leurs exécutions ; aucun sous-agent consommateur testé encore. La revue a rejeté l'affirmation initiale de reconstruction gzip exacte : tar décompressé identique, gzip OS header original 0x13/rebuild 0xff. SHA rebuild `8d780e23add20e880a81b2fa8bce5c2e5f500e8a8b86130a3b924a12a6ee306c`, original rc.5 inchangé. README/PUBLICATION corrigés avant push, REPRODUCTION.json public. 27 tests lifecycle/frontière publics passent. Ne pas relancer le builder sur l'archive factory historique : il refuse une reconstruction différente ; traiter cette limite sans écraser un gel.

Playwright CLI disponible via wrapper installé, aucune dépendance ajoutée intentionnellement. Session `vbb-runtime-diagnostic` fermée ; serveur Python loopback 8765 arrêté (fin processus observée). Diagnostic mobile 390×844 : menu après Escape conserve aria-expanded=true, capture native privée inspectée. Première commande route a échoué car URL non défini dans le contexte CLI ; corrigée avant navigation, échec conservé dans la conversation. Cela n'est pas une réussite autonome worker. Réseau externe bloqué, erreur ressource attendue à distinguer des erreurs JS. Diagnostic complet multi-viewports/no-JS/reduced-motion/ancres reste à exécuter.

Avant poursuite : lire `test-design/PROPOSAL.md`, `missions/consumer-missions.md`, `oracles/private-oracles.md`, `oracles/coverage.md` sous dossier privé. Tout reste proposition, aucun gel ni confirmation consommée. Matérialiser fixtures et tests, diagnostic rendu complet puis préflight versions/compositions/protections (anciens profiles secrets nettoyés, ne pas relancer leurs prepare.py). Budget et matrice doivent être arrêtés avant workers. Utiliser le mécanisme natif séquentiel observable ; aucun modèle auxiliaire/titre concurrent. Le site n'a pas de Git : créer le premier historique uniquement dans copies d'essai.

Le contrôle de préservation après push confirme les cinq fichiers source et tous les fichiers factory non-Git préexistants inchangés. Inventaires, sorties scan/tests/build, revue refusée et correction, preuve push dans le dossier privé. Aucun prérequis réellement bloquant actuellement ; le goal reste actif, sans réduction du périmètre.

## Point courant après préparation native et navigateur

Lire [préparation runtime](runtime-preparation.md) et [frontières phase2](phase2-entry.md). Diagnostic rendu complet et conducteur consommateur disponibles ; dix copies Git isolées préparées, aucune mission worker lancée. Deux vrais essais DSH avec enfant natif ont terminé ; tous appels HTTP propres observés séquentiels, mais activité supplémentaire du serveur partagé non attribuée. G1/G2 conservés en échec de qualification de séquence. `native-preflight/SUSPENDED.json` bloque les collectes dépendantes ; ce n'est pas un processus vivant. Une question d'attribution est en attente auprès de Brice ; poursuivre tout travail indépendant.

Reprise privée : `native-preflight/REPORT.md`, `capability-g1/assessment.json`, `capability-g2/assessment.json`, `collection/capability-g2-dsh/meta.json`, `browser-harness/DIAGNOSTIC.md`, `campaign-g1/cells.json`, `prepare-fixtures.py`, `inject-fixture.py`. La campagne n'est PAS gelée. Scripts consommateurs sous consumer-assets, copies tests/docs protégées. Un seul test de préparation T1-N a tourné, preuve déplacée intacte sous native-preflight/consumer-baseline-* ; aucun avantage de preuve laissé dans la cellule. Préparer et contrôler workflow/injections, budgets et oracles avant lancement. Ne pas relancer G1/G2 comme s'ils étaient en attente ; fins natives/groupes/streams et secrets nettoyés sont vérifiés. Ne pas masquer le défaut d'attribution en remplaçant DSH par Codex.
