# Rc.5 — traitement structuré de deux entrées invalides

Archive exacte SHA256 `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`. Six fichiers produit ; anciens candidats conservés.

La revue fraîche de rc.4, en lecture seule, a vérifié les membres/octets de l'archive et exécuté sous Python 3.11.11 les 22 tests lifecycle, 3 frontière et 20 mesures. Aucun nouveau défaut de conservation établi. Deux P3 reproduits : chaîne JSON de chemin `\ud800` non encodable ; boucle symbolique de racine levant RuntimeError sous Python 3.11. Ces cas produisaient une traceback/code 1, contraire au contrat d'entrée invalide/code 2. Voir `../candidate-rc4-review/runs/01-review/stdout.jsonl` ; fin, inactivité, absence de mutation et nettoyage credential dans validation.json de cette revue.

Rc.5 valide l'encodabilité des chemins avec os.fsencode, convertit l'erreur en InputError, et convertit aussi RuntimeError de résolution de racine en InputError. Aucun changement de sémantique des sélections valides ni du cycle de vie. Deux nouvelles régressions CLI sur l'archive extraite exigent code 2, JSON exploitable et absence de traceback ; échouent sur rc.4, passent sur rc.5.

Vérification locale : 27 tests (22 lifecycle, 3 frontière, 2 entrées CLI), 20 mesures sur module extrait, CLI réel passent. Upgrades réels rc.2, rc.3 et rc.4 vers rc.5, répétition/inspection/retrait/répétition : tous préservent exactement AGENTS utilisateur, mémoire et données. Résultats détaillés dans real-upgrade.json. Pas d'installation factory, pas de publication.

Restant : revue ciblée des deux corrections sur rc.5 exact, puis audit complet des critères du mandat avec preuves primaires (les tests et les rapports ne suffisent pas seuls). Les profils restent expérimentaux et exposent la dépendance aux remédiations et les défauts narratifs observés. Goal non accompli.
