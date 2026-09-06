# Relecture du plan et reprise

Date : 2026-09-05. Relecture par l'auteur avec cas adverses documentaires ; **pas une revue par un second agent ou une qualification live**.

## Corrections et bornes retenues

| Question éprouvée | Résolution dans le plan |
|---|---|
| Un skill automatiquement sélectionné contredit-il l'engagement explicite ? | Métadonnées natives Pi/DSH/Codex précisées et qualification obligatoire par profil ; pas de simple promesse de prompt |
| Le ledger revient-il sous le nom de mémoire ? | Mémoire documentaire uniquement ; aucun dispatch/replay d'effets, pas de lease ou consensus distribué |
| Une date ou une compaction peut-elle créer du canon ? | Autorité, portée, source et fraîcheur séparées ; résumé dérivé ; aucune promotion automatique |
| Le contexte limité coupe-t-il les règles gênantes ? | Contraintes critiques obligatoires ; dépassement déclaré et chargement progressif, pas de troncature silencieuse |
| Un retour ancien ou double peut-il décider pour le projet ? | Base revision, contribution distincte, intégration par coordinateur et déduplication documentaire |
| Deux agents peuvent-ils éditer simultanément la mission ? | Hors profil supporté ; un coordinateur par mission, retours séparés ; pas de garantie de verrouillage contre les écritures directes |
| La sandbox est-elle supposée identique partout ? | Pi explicitement sans sandbox intégrée ; capacités qualifiées par environnement, DSH preview épinglé |
| Retirer VBB retire-t-il les décisions de l'utilisateur ? | Données projet conservées, contenu distribué seul retiré, divergences laissées en place |
| L'utilitaire doit-il déjà être installé pour installer VBB ? | Point d'entrée extrait utilisable par chemin ; aucune modification automatique du PATH |
| Le plan revient-il à migrer V1 ? | Aucun composant V1 sélectionné ; corpus d'incidents utilisé comme tests adverses seulement |

## Vérifications documentaires

Liens locaux, équilibre des blocs, intégrité des copies de sources et conservation des fichiers d'entrée vérifiés. Les sources V1 capturées sont comparées à leurs fichiers d'origine en lecture seule. Le registre de vérification est `verification.json` dans ce dossier. Les mesures historiques R2-05/R2-18 ont fait l'objet de recomptages bornés ; aucun test ou programme V1 n'a été lancé.

## Reprise pour la réalisation

Lire `implementation-plan.md`, puis les décisions D01–D03. Commencer par L0/L1. Ne pas relire les 17 sources V1 ou les historiques complets si la tranche ne les requiert pas. Utiliser les liens du cas pertinent pour retrouver une justification.

La prochaine réalisation doit conserver trois limites : factory non consommatrice, contrôle technique confié au harness, mémoire canonique par source/portée et non par récence. Les incertitudes restantes sont des objets de validation du plan, pas des raisons d'ajouter un runtime ou d'installer une méthode.

Aucun arbitrage d'architecture supplémentaire n'est actuellement requis. Une demande ultérieure de contrôle transactionnel des actions, d'écriture simultanée multi-coordinateur ou de service de mémoire global rouvrirait D01/D05/D07.
