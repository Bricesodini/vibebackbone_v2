# Reprise du goal actif après FRET-62

Lire INDEX puis `.backbone-dev/evaluations/integrated-2026-09-06/STATUS.md` et `report.md`. Le goal long a été créé nativement et reste actif, sans budget demandé. Brice absent a adopté les autorisations conditionnelles produit/cycle de vie local ; ne pas redemander. Aucun goal complet ni blocage déclaré. Tous les travaux sont dans le checkout d'origine, non commités factory ; préserver le préexistant.

## Acquis et défauts à ne pas réinterpréter

Pi/DSH calibration passent, DSH profil privé désactive le titre et surfaces concurrentes ; dix passages terminés avec observation locale séquentielle. FRET-62 métier fonctionne et les deux outils sont réellement utilisés, Git transmis. Fidélité autonome échoue : Pi fausse archive A (copie après écrasement), DSH reconstruit sorties/temps et conserve mal des intermédiaires, lecteurs interprètent mal chronologie. Gel 4 reviewer Codex neuf restaure A depuis Git et allège mémoire ; dernier DSH retrouve A→B mais garde une imprécision sur anciens fichiers de flux. Voir `assessment.json` pour les mesures, `demo-assessment-erratum.md` pour l'erreur initiale de l'évaluateur. Pas de PASS global, pas de gain comparatif.

## Action suivante

Matérialiser puis figer `.backbone-dev/evaluations/value-2026-09-06/protocol-draft.md` : six passages Pi, deux cas neufs, N/C/T ordre fixé, équipement identique. Préparer aide outils autonome exacte ; celle copiée dans FRET-62 contenait des liens internes absents. Geler sources/profils/prompts/oracles avant appel. Les sources et conducteurs précédents sont réutilisables PAR COPIE dans une nouvelle tranche, pas en écrasant leurs gels. Après comparaison, décider noyau justifié et qualifier une mission neuve avec les corrections retenues, avant produit si conditions satisfaites. Ne pas répéter FRET-62 sans progrès ni surqualifier les corrections guidées.

## Exécution technique

Ancien runner `integrated-2026-09-06/runner.py` : homes neufs, sandbox-exec externe impératif, docs/AGENTS/tools protégés et factory illisible, stdout dans home puis archive, Git intégral. capture-fetch.mjs observe début/fin de streams et concurrence ; prime-pi-fetch.mjs nécessaire Pi. Server_activity observe [PRIVATE_MODEL_ENDPOINT]/slots sans annuler d'autres clients. DSH native compiled `[LOCAL_PATH]`.

**Templates privés nettoyés** par close.py : profiles.json contient des chemins historiques dont models.json/.credentials.yaml ne sont plus présents. Ne pas relancer les anciens conducteurs comme s'ils étaient prêts. Préparer de NOUVEAUX profils dans la nouvelle tranche à partir des configs expurgées et clé du provider [PRIVATE_PROVIDER] lue sans sortie dans ~/.dsh/.credentials.yaml ; aucune écriture globale. Ne pas relancer prepare.py de l'ancienne tranche : il écraserait des fichiers gelés. Refaire les contrôles sans modèle et la composition avant appels. Les homes des dix passages sont aussi nettoyés. Validation de clôture locale : gels intacts, globals intacts, zéro match des trois valeurs de secrets connues testées. 20 tests prototype passent, distribution explicite contient zéro fichier.

## Obligations restantes du goal

Bénéfice concret documenté, noyau utile retenu sans régression critique, mémoire portable réellement fidèle sur la portée annoncée, profils trois harnesses/versions et limites, produit minimal product/ seulement, coexistence spécialistes par fixtures, archive positive exacte, lifecycle install/répétition/update/retrait dans projets isolés en préservant données/divergences, revue candidat exact neuve disponible, documentation démarrage et restitution. Rien de cela n'est réputé accompli par la calibration. Aucune publication/push/global/factory install. Le goal reste actif jusqu'aux critères réels ou blocage persistant selon ses règles natives.
