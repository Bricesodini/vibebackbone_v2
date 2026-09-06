# Remédiation PARCEL-95 après retrait — résultat mixte

Trois passages préfixés réalisés : Codex revue/remédiation 173,5 s ; Pi lecteur 102,59 s ; DSH lecteur 170,13 s. Tous terminent normalement. Fins locales, observations serveur et streams séquentiels confirmés. Produit absent de la copie d'essai ; aucune installation. Freeze, globals et recherche des trois secrets connus passent ; clés privées nettoyées.

## Progrès prouvés

L'objet invalide de l'ancien lecteur Pi résultait d'une recopie hybride : préfixe d'initial-A et suffixe d'un autre objet. Les objets et fichiers réels étaient présents. La consigne de reprise après erreur et de références révision:chemin accompagne ce nouveau gel ; Pi termine cette fois sans boucle. Ce résultat unique n'établit pas une causalité isolée : mémoire et consigne ont changé ensemble.

Codex retrouve et corrige le faux décompte B (2 échecs, non 6), préserve les deux notes avant remplacement, recompte les captures et exécute le reporter avec une nouvelle capture 9/9. Il retire la dépendance de CONTINUE au lien produit absent, distingue contrôle actuel et mesures historiques. Captures anciennes, code, sources, objets et références Git intacts. `.git/index` a changé pendant la revue ; ses entrées `git ls-files --stage` sont exactement identiques, seules les métadonnées d’index diffèrent. Copies des prédécesseurs exactes. Les deux lecteurs ne modifient aucun octet, Git compris ([assessment](assessment.json)).

## Limites qui empêchent le PASS strict

Pi retrouve la source choisie, B, les décomptes, le fait Orion, les mesures historiques et le retrait. Mais sa section « défaut initial corrigé avant B » décrit surtout la transition B ; ailleurs il identifie correctement le code initial `n // 8`. Il affirme en fin de réponse que l'état post-remédiation est « protégé par le manifeste SHA-256 » alors que le manifeste est antérieur aux modifications et ne protège rien activement. La portée exacte n'est donc pas fidèlement exposée partout.

DSH recompte correctement les captures mais affirme faussement que le prédécesseur initial est `184f636:parcel.py` avec `(n + 7) // 8`, au lieu de `aaa5bf4:parcel.py` avec `n // 8`. Il présente alors une formule correcte comme le défaut et répète une égalité au mauvais commit comme vérifiée. C'est une erreur de provenance et de chronologie importante, malgré les bons décomptes. Il confond aussi le reporter de tests avec les outils compare/inventory dans l'explication de leur non-réexécution. Anciennes traces conservées, pas de qualification rétroactive.

La mémoire revue corrige le nombre mais ne rend pas explicite dans son entrée courte la transition **floor/8 initial → ceil/8 corrigé → ceil/6 sous B** ; le lecteur doit la reconstruire par plusieurs sources. C'est une piste de remédiation, pas une excuse ni une preuve de causalité.

## Suite

Conserver ce gel. Préparer une chronologie concise et vérifiable à partir des captures et des vrais commits, sans deuxième canon métier, ni copies manuelles de hashes, ni nouveau mécanisme produit. Préserver les notes remplacées et annoncer la provenance de cette remédiation de l'évaluateur. Nouveau gel de lectures courtes avec mêmes faits obligatoires ; limiter la redondance de réponse ne réduit pas les critères de vérité. Ne pas répéter les mêmes essais sans correction.

Revue fraîche du produit rc.2 et documentation finale demeurent des travaux indépendants. Les succès mécaniques du produit n'effacent pas ces défauts de lecture. Goal actif.
