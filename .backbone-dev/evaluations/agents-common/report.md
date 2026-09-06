# AGENTS commun — première collecte close

Protocole gelé avant appels : freeze.json. Neuf passages, aucune relance dans ce gel.
Codex : 3/3 comportements conformes, zéro outil et mutation. Pi et DSH : 3/3 chacun
indisponibles au démarrage natif (SIGABRT), aucune requête observée. Mémoire non exécutée.

Le diagnostic après collecte, sans modèle, isole un défaut du conducteur : rediriger
stdout vers un fichier de la factory interdite en lecture provoque le même SIGABRT Node ;
rediriger vers le home autorisé réussit (post-collection-diagnostic-redirection.json).
Les sondes préalables capturaient des pipes et n'avaient pas vérifié cette composition.
L'indisponibilité vaut pour ce profil expérimental, pas pour les loaders Pi/DSH.

Une nouvelle version technique séparée est nécessaire : traces natives dans le home privé,
archivage par le conducteur après fin ; mêmes fixtures/oracles, nouveau préflight reproduisant
les redirections réelles, nouveau gel avant collecte. Cette première collecte reste intacte.
Aucune conclusion produit, aucun L2/installateur. Voir agents-common-v2 pour la suite.
