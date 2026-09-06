# Préparation runtime et diagnostic natif — 2026-09-06

Statut : **NOT_READY**, aucun worker métier ni passage de confirmation exécuté. Les données ci-dessous changent les prochains travaux ; elles ne remplacent pas la campagne.

## Diagnostic rendu

Node 24.14.1, Playwright 1.62.1, Chromium 151.0.7922.34, DPR1, locale fr-FR, timezone Europe/Paris. Sept largeurs 320/390/720/721/980/981/1440. Requêtes navigateur bloquées hors origine loopback ; Google Fonts bloqué et erreurs ressources distinguées des exceptions JS.

Diagnostic corrigé : 55 assertions PASS, 38 FAIL, aucune erreur conducteur ; pas 93 scénarios indépendants. Menu : nom accessible inchangé, Escape et reset responsive défaillants. Cartes et llms : destinations génériques. Sans JS : 50 éléments reveal invisibles aux deux largeurs inspectées, navigation mobile inaccessible. Aucun overflow document observé aux sept largeurs, aucune exception JS. Captures réellement inspectées. Premier essai de préparation ERROR conservé : scroll smooth empêchait le conducteur d'attendre correctement les reveals ; correction de conducteur avant gel, aucun défaut worker imputé.

Les tests consommateurs par tâche sont préparés, sans exposer les autres confirmations. Le script T1 a été exécuté sous sandbox externe : 46 PASS, 6 FAIL attendus sur code initial, 0 ERROR. Contrôles nouveaux de Tab menu fermé et position contact passent. Preuve de préparation déplacée intacte hors copie pour ne pas avantager la baseline. Les autres interfaces doivent encore être validées avant le gel complet.

## Préflight natif

Codex embarqué 0.153.4 (PATH 0.147.0 distinct), Pi 0.84.2, DSH 0.1.0-rc.8 compilé. Qwen local UD-Q4_K_S explicitement observé dans catalogue, thinking off effectivement envoyé. Homes neufs, globals conservés. Sandbox externe : lectures source/factory/oracles/secrets globaux refusées ; Node/Python/Git et navigateur loopback autorisés dans copie ; docs/tests/AGENTS/.vbb protégés et lecteur lecture seule. Les premières erreurs de résolution metadata ancêtres sont conservées ; autorisation metadata littérale corrigée sans ouvrir lecture des répertoires privés.

Pi n'offre pas de sous-agent natif dans la composition installée. DSH expose réellement spawn au premier plan ; pool outils limité à 1, arrière-plan et auxiliaires de titre désactivés, composition effective vérifiée. Codex dispose de multi_agent mais sa parité de séquence interne n'est pas prouvée ; sessions CLI consommateurs prévues sans cette fonction, sous-agents factory documentés séparément. Ce choix avant collecte protège le contexte worker et n'est pas un substitut silencieux aux capacités natives.

## Deux gels de diagnostic de délégation DSH

G1 : une vraie session enfant native, origine subagent et profondeur1, retour collecté avant reprise parent. Résultat du fichier vérifié. Sept streams instrumentés séquentiels et terminés, groupe fini, trois idle finaux, copie inchangée, secrets temporaires retirés. Cependant deux slots serveur simultanés : gel non qualifié pour la séquence serveur.

G2 : une seule nouvelle tentative préfixée, même tâche/modèle ; instrumentation complétée par diagnostics HTTP undici, sans modification des requêtes ni ordonnanceur. Sept requêtes HTTP correspondant aux sept fetch, toutes séquentielles/terminées. Deux sessions natives terminées, titres fallback sans appel titre enregistré. Un petit appel serveur supplémentaire reste non attribué. Peut provenir d'un autre client ou comportement serveur ; aucune de ces causes n'est affirmée. Gel conservé `FAIL_SERVER_SEQUENCE_ATTRIBUTION_UNRESOLVED`.

Les deux fins sont prouvées : aucun processus de ces collectes à attendre. La collecte dépendante est suspendue, pas le goal. Aucun tiers annulé, aucun nouveau lancement identique pour obtenir PASS. Question d'attribution adressée à Brice ; scripts/fixtures/frontières phase2 poursuivis indépendamment. Il faut résoudre l'attribution ou établir un environnement observable avant de consommer les confirmations.

## Copies et suite

Dix cellules indépendantes préparées, chacune avec Git initial réellement créé depuis snapshot privé ; cinq installations VBB depuis l'archive historique exacte, cinq baseline natives. Code source original et code initial de chaque copie vérifiés identiques. Missions, décisions simulées, sources choisies/non choisies, tests et injections sont séparés des oracles privés. Injection D2 après diagnostic prévue pour T2/C2 ; aucune réparation de mémoire par évaluateur. La campagne reste non gelée : scripts/versions/budgets/oracles doivent être contrôlés ensemble avant workers.

Les rapports, scripts, freezes, captures, requêtes et copies restent sous le dossier privé de campagne. Ce rapport dérivé est publiable ; aucune source site, capture ou trace brute n'y est reproduite. Frontières phase 2 : [contrats préparés](phase2-entry.md), sans méthodologie installée.
