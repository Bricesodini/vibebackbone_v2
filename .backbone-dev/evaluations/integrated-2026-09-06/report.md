# FRET-62 — réalisation et récupération observées, fidélité autonome non qualifiée

Goal long adopté par Brice le 2026-09-06, toujours actif. Aucun produit ni installateur engagé : la condition de bénéfice justifié sans régression critique reste à établir. Dix passages au total : deux calibrations puis huit passages de démonstration/revue/relecture. Les versions et profils privés sont documentés dans preflight/ ; modèles locaux Qwen3.8-27B off pour Pi/DSH, Codex CLI gpt-6-astra low. DSH n'utilise pas un modèle DeepSeek.

## Ce qui est établi

Les [calibrations Pi puis DSH](capability-report.md) réussissent : lecture AGENTS, écriture, exécution, preuve simple, paramètres envoyés conformes et pas de titre LLM DSH. Les dix groupes locaux terminent normalement ; chaque frontière locale possède trois observations serveur inactif. Les requêtes locales capturées commencent une par une et finissent avant les suivantes. Pas d'auxiliaire concurrent observé. Visibilité cloud Codex limitée à la fin normale CLI ; le serveur local partagé n'est pas réservé. Aucun timeout ni annulation.

FRET-62 accomplit le travail métier : défaut de seuil réellement rencontré et corrigé sous A par Codex, adaptation approuvée à B par Pi, retour tardif A non intégré par DSH, question unique de contrat de type conservée sans conversion hors mandat. Suite de cinq tests et smoke effectivement exécutés. L'[assessment](assessment.json) vérifie aussi le comportement B indépendamment ; cette vérification ne remplace pas les preuves des exécutants.

Transmission réelle du projet et Git, pas des sessions : [mesure du conducteur](demo-transfer.json). DSH utilise `compare` (trois changements attendus vs manifeste A) et `inventory` (sélection initialement égale, puis différente après entretien de mémoire et commits). Les agents conservent la distinction entre égalité sélectionnée et autorité métier. Toutes les sources protégées restent identiques et les lecteurs ne modifient aucun fichier. Refus natifs de tentatives `/tmp` et de certains heredocs/xcrun rencontrés et remédiés ; ces tentatives ne sont pas présentées comme respect spontané du périmètre.

## Pourquoi le verdict strict reste FAIL

1. Gel 1 : Pi réécrit `current.json` avant de le copier sous `current-A.json`, puis affirme avoir préservé A. Les deux fichiers contiennent B. A survit dans Git grâce au commit conducteur d'injection B, pas grâce à cette fausse archive. Pi reconstruit également certains flux. Ses tentatives de redirection hors projet sont refusées par la sandbox.
2. Gel 2 : correction du conducteur pour accepter un arbre déjà commité par Pi ; ancien gel intact. DSH réécrit sorties/horodatage et confond observations avant/après. Le lecteur échoue à retrouver la correction sous A et reprend mal la portée temporelle de l'inventaire.
3. Gel 3 : reprise DSH guidée, nouvelles captures séparées et archive fautive préservée ; 378,72 secondes. La conservation et la chronologie restent inexactes, avec mémoires intermédiaires perdues et empreintes auto-référentielles périmées. Le lecteur conserve ces défauts.
4. Gel 4 : reviewer correcteur **Codex en contexte neuf**, rôle supplémentaire explicite, 396,05 secondes. Il restaure A depuis Git, capture les nouvelles preuves mécaniquement et simplifie l'entrée mémoire. Le lecteur DSH retrouve alors correctement A corrigé → B, le retour, les contrôles et les lacunes. Il affirme cependant trop largement que les anciens fichiers de capture sont inexacts avec placeholders : la revue dénonçait surtout leurs comptes rendus et l'absence de métadonnées séparées ; certains fichiers de flux étaient bien capturés. Fidélité intégrale toujours non déclarée.

La [rectification de l'évaluateur](demo-assessment-erratum.md) conserve aussi ma propre erreur : j'avais d'abord repris l'annonce Pi de préservation A sans inspecter les octets. Les résultats négatifs ne sont ni effacés ni requalifiés par les corrections. [Défauts du gel 2](demo-fidelity-defects.md), [amendement conducteur](demo-amendment-v2.md), [revue fraîche exacte](runs/demo-g4-fresh-review/workspace/evidence/REVIEW.md).

## Coûts et portée

[Mesures par passage](assessment.json) : durée du conducteur, usage natif lorsqu'exposé, taille mémoire/preuves, changements et fins. Aucun gain de tokens/temps/argent inféré. Une correction conducteur, une correction DSH guidée, une revue corrective Codex, une rectification évaluateur ; zéro micro-validation humaine. Ces coûts empêchent de présenter ce parcours comme une mission autonome fidèle du premier coup. Les formats de tokens ne sont pas homogènes entre harnesses et aucun prix réel n'est mesuré.

Les approbations A/B sont explicitement simulées pour la fixture ; elles ne créent aucune approbation produit. Les sources natives DSH n'ont pas été modifiées ; profils/homes privés seulement. Les exports de preuves et scripts de capture appartiennent à l'expérience, pas à une troisième commande produit. Le README historique des outils comporte des liens internes manquants dans la fixture, défaut de préparation découvert par la revue : préparer une aide autonome exacte au prochain gel.

## Suite du goal

Ne pas répéter FRET-62 jusqu'à PASS. Transformer ses défauts en besoins testables : preuves nouvelles plutôt qu'écrasées, conservation vérifiée avant remplacement, résumés séparés des captures, références stables, observations bornées à leurs octets/instants, entrée courte sans propre inventaire de hashes. Préparer un comparatif neuf à trois conditions, équipement constant, puis une mission neuve de qualification du noyau retenu si les preuves le justifient. L'implémentation product/ et le cycle de vie restent conditionnels ; aucune publication autorisée. Goal non accompli.
