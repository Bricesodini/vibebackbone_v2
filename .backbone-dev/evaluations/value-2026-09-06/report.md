# Comparatif exploratoire — deux outils justifiés, cadre documentaire non démontré

Six passages Pi 0.84.2 / Qwen3.8-27B off, exactement l'ordre et le budget du [protocole](protocol-draft.md), [gel préalable](freeze.json). Aucun retry ni passage ajouté. Toutes les cellules finissent normalement ; requêtes séquentielles terminées, trois observations serveur inactif aux frontières. Tous les octets d'entrée, y compris Git source, restent inchangés. Les protections refusent cependant des tentatives d'écriture de rapports dans docs/ en F-N, T-C et T-T ; ce ne sont pas des refus anticipés par les agents.

## Qualité observée

| Cas / condition | Résultat technique et mémoire | Défauts / limites |
|---|---|---|
| F / native | Douze chemins correctement classés ; approbation courante et absence d'autorité du hash préservées ; non-enregistrement distinct du passé inconnu | Formulation contradictoire « vérification de l'absence de fichier manquant » malgré zone-06 explicitement manquant ; demande de confirmation du refus de Nina inutile pour clore le diagnostic ; aucune mutation métier |
| F / convention | Même classification exacte ; note et rapport plus courts | Aucun bénéfice de qualité clairement isolé contre native ; preuves résumées dans rapport, pas de capture brute prétendue |
| F / convention+outils | compare réellement appelé ; sortie conservée octet pour octet et reproductible ; tous statuts/interprétations essentiels corrects | Confirmation de l'écartement de Nina encore proposée ; pas de gain d'autorité démontré |
| T / native | Différence r04, absence r08, Git manquant et contrat hors sélection retrouvés ; règle lithium conservée | Affirme 7 égalités tout en listant 8 ; dit « ambiguïté de localisation levée par l'égalité de contenu » puis demande le chemin officiel : contradiction. Date 2025 au lieu de 2026. Note propose des corrections hors des trois dossiers sans rappeler qu'elles demandent un autre mandat |
| T / convention | Huit égalités et défauts r04/r08/Git/contrat corrects ; règle unique conservée | Présence des deux candidats décrite, ambiguïté non traitée explicitement. Fichier « preuves » créé par write : réordonne ls-tree et omet ses modes, ajoute des commentaires malgré annonce de sorties exactes séparées. Note recommande restauration/correction sans réserver l'autorisation d'une mission suivante |
| T / convention+outils | inventory réellement appelé, code 2 traité comme mesure Git indisponible ; 8 égaux, r04/r08, ambiguïté, Git et contrat correctement exposés ; sortie exacte reproductible | Rapport affirme que l'omission du contrat par la sélection « explique son absence » : causalité non prouvée. Rapport précise que la restauration n'est pas autorisée dans ce mandat, mais la note seule devrait mieux conserver cette frontière |

Aucune condition n'a restauré de fichier ou perdu la règle unique. Les trois conditions retrouvent le fait métier omis parce que le **mandat**, identique, le demandait : aucun mérite de complétude sémantique attribué à inventory. N/C ont accès à Git et au hachage et les utilisent réellement ; la baseline n'a pas été privée de moyens. Deux candidats à contenu identique ne désignent pas un chemin unique ; les outils rendent cette limite explicite sans choisir une autorité.

Le bénéfice concret des deux instruments est borné : sorties structurées exactes conservées/reproductibles dans les deux cellules équipées, classification exhaustive et ambiguïté conservée dans le cas T. Les résumés agent restent faillibles, y compris avec outils. La convention seule ne corrige pas systématiquement la fidélité et peut augmenter fortement le volume rédigé. Aucun succès statistique ni garantie générale, aucune qualification complète de mémoire autonome.

## Mesures comparables dans cette collecte

[Mesures et contrôles mécaniques](metrics.json), [script d'évaluation](assess.py). Tokens `totalTokens` = usages natifs incluant cacheRead, pas tokens facturés ; valeurs absolues et définitions natives conservées. Coût financier inconnu (les zéros du provider local ne sont pas un prix mesuré).

| Cas / condition | Secondes | Requêtes | Tokens totaux natifs | Octets note | Autres sorties |
|---|---:|---:|---:|---:|---:|
| F / N | 141,34 | 14 | 95 778 | 2 159 | 6 615 |
| F / C | 94,61 | 9 | 63 119 | 1 480 | 5 470 |
| F / T | 79,53 | 9 | 63 954 | 1 383 | 10 727 |
| T / N | 111,56 | 11 | 91 064 | 2 641 | 6 050 |
| T / C | 206,28 | 13 | 201 551 | 2 102 | 10 009 |
| T / T | 132,11 | 13 | 153 900 | 1 873 | 11 447 |

F équipé est plus rapide ici que native mais ses tokens sont légèrement supérieurs à convention seule. T équipé est plus lent et consomme plus de tokens que native, malgré de meilleurs constats sur compte/ambiguïté. Les sorties JSON accroissent le stockage documentaire. On ne revendique donc **aucune économie globale**. Une seule réalisation par condition, deux cas, ordre partiellement inversé, cache et génération non contrôlés statistiquement. Le temps de création humaine des manifestes n'a pas été mesuré : coût inconnu, pas zéro. `prepare-measure.json` mesure uniquement l'exécution du script de préparation.

## Décision permise par ces preuves

Poursuivre L2 **ciblé** sur compare/inventory, avec leurs limites explicites, une aide autonome et un cycle de vie local. Aucun troisième outil de continuité, schéma de mémoire imposé, service, moteur ou compétence de fermeture automatique. Conserver seulement une courte consigne optionnelle de continuité répondant au besoin utilisateur, comme proposition à qualifier sur le candidat exact ; son bénéfice propre n'est pas acquis. Une sortie native standard de test/capture reste une preuve projet, pas une nouvelle API VBB.

Les régressions critiques du démonstrateur ne sont pas résolues par ce comparatif diagnostique. Une nouvelle mission de bout en bout sur le candidat exact doit encore qualifier la conservation, l'autorité et la reprise ; les défauts de note empêchent d'annoncer une autonomie fidèle complète. L'autorisation conditionnelle du mandat permet de construire ce candidat local pour le qualifier ; elle ne permet ni publication ni déclaration de RC finale prématurée.
