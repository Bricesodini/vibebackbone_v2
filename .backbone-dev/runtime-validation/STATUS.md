# Validation runtime et entrée phase 2 — mandat actif

Mandat du 2026-09-06 adopté : ../handoffs/2026-09-06-runtime-validation-phase2.md.
Verdict actuel : **NOT_READY**, qualification en cours. Aucun critère du nouveau goal n'est satisfait par simple héritage de l'audit rc.5.

## État courant après la paire T1 — 2026-09-06

**NOT_READY, goal actif.** Campagne G1 gelée avant collecte, rc.6 exacte `d7a4d305704ec180e6870c14000dd93b205bc9bc50fa4d4f1c452a4fc7ac7ff5`. Deux reconstructions identiques ; 47 tests mécaniques passent. Les états antérieurs ci-dessous sont historiques et ne remplacent pas ce point.

La limitation de séquence G1/G2 reste un échec conservé. G3 ajoute une observation passive des requêtes propres avec confinement OS interdisant le contournement ; le vrai enfant DSH a été exercé (7 requêtes, toutes closes et séquentielles). Cette preuve prospective permet de poursuivre sans attribuer artificiellement l'activité des autres clients du serveur partagé. Aucun runtime VBB ni configuration globale ajouté. L'ancien SUSPENDED.json n'est pas effacé ; collect-g3.py utilise son propre arrêt. Aucun blocage courant ni modèle actif au point de sauvegarde.

Six essais triviaux effectués : Codex-N exact ; Codex-V interrompu par capacité du modèle (échec environnement conservé, sans substitution) ; Pi/DSH rendent le bon titre avec format superflu dans les deux conditions. Pas de mémoire superflue créée. Ne pas résumer cela en six PASS.

T1-N et T1-V : parcours Codex worker → Pi revue → Codex reprise → DSH lecteur, huit sessions natives terminées. Six défauts initiaux corrigés, 52 PASS/0 FAIL/0 ERROR finaux dans chaque condition, PASS_WITH_COVERAGE_LIMITS. Reprises fidèles : D2/D1, Git non commité, preuves initiales/courantes, retour périmé et oracle tiers faux correctement distingués. Zéro réparation manuelle de mémoire, aucun remplacement de lecteur. Revue et reprise étaient préfixées et leurs coûts restent inclus. Code original et fichiers protégés vérifiés inchangés. Captures mobiles réellement inspectées. Aucun gain de coût ni avantage VBB démontré à ce stade.

Versions observées : Codex exécute le runner sous Node20.19.0, Pi sous Node24.14.1 ; même version par rôle entre N/V. Le gel mentionnait Node24 pour les hôtes Pi/DSH : variante shell conservée explicitement, pas réécrite. Chromium seul, polices bloquées, clic individuel Contact seul ; assertions adaptées et limites conservées. Les chevauchements du serveur partagé ne sont pas des chevauchements propres : captures Pi/DSH complètes, séquentielles et closes. Fin cloud interne non directement observable.

Prochain : T2-V diagnostic Pi (480s), injection D2 préfixée, reprise Pi (720s), retours, revue DSH (600s), remédiation Pi (600s), lecteur Codex (300s). Puis T2-N, T3-N/V, C1-V/N, C2-N/V, sans consommer les confirmations pour régler les prompts. Huit cellules restantes ; smokes de mesures, cycle de vie final exact, revue fraîche et verdict des dix critères restent ouverts. Frontières de phase2 préparées, aucune méthodologie installée.

Preuves privées : `[PRIVATE_CAMPAIGN]/campaign-g1/PROTOCOL.md`, freeze.json, assessments/T1-N.json et T1-V.json, lecteurs verbatim, native-preflight/collection/site-g1-T1-*, source-preservation-after-T1.json. Prochain lancement nommé site-g1-T2-V-worker, jamais une répétition T1 pour obtenir PASS. Dernière sauvegarde publique vérifiée avant ce point : `033c4495dccbd1d197943b48a848512d3ed2a5b2` sur codex/public-runtime-validation ; synchroniser les dérivés actuels depuis l'export propre, jamais l'historique factory.

## Historique conservé

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
