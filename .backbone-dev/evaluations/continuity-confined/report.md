# Première validation sous confinement — Pi opérationnel, composition DSH incompatible

La protection native des écritures fonctionne, mais **cette série ne qualifie pas la
chaîne complète**. Pi réussit sa mise à jour et sa revue ; DSH ne peut exécuter aucune
commande shell sous deux sandboxes macOS imbriqués. Il termine et documente les preuves
manquantes, mais déclare à tort le mandat clos malgré cette exigence non satisfaite.
Le lecteur neuf reprend cette clôture « dégradée ». Les oracles de l'évaluateur réussis
ne compensent pas l'absence d'exécution des tests par DSH.

## Entrée et conditions

Création réelle Codex MP de `continuity-equipped/runs/step1-MP`, sans modification
humaine, puis Pi équipé, DSH, lecteur DSH neuf. Même mission, canon, modèles et prompts
que la comparaison équipée ; validation guidée MP uniquement, aucun résultat comparatif.
[Protocole](protocol.md) et [verrou des entrées](source-lock.json)
préparés avant les modèles.

Le même projet persiste entre Pi et DSH ; les homes natifs sont neufs. Les sources
reçues sont protégées par macOS ; le projet, le home privé et les traces sont les seuls
espaces ordinaires autorisés en écriture. Deux sondes avant chaque modèle vérifient
le refus hors espace et sous docs. Aucun modèle n'est lancé hors sandbox externe.
Les agents ne créent aucun commit dans cette série ; la persistance d'un Git non vide
n'y est donc pas démontrée, même si le dossier Git reste dans le projet.

| Exécution | Secondes | Arrêt / métier | Résultat propre au harness |
|---|---:|---|---|
| Pi, B et reviewer | 236,8 | normal / oracle OK | Tests exécutés, vraie revue, preuves dans le projet |
| DSH, retour R-A | 250,7 | normal / oracle OK | Shell indisponible, nouveaux tests non exécutés |
| DSH lecteur neuf | 88,6 | normal / oracle OK | Fichiers sans mutation, absence de preuve C reconnue, clôture à tort acceptée |

Trois observations de slots inactifs avant/après chaque essai ; collecte strictement
séquentielle. Modèles : création Codex gpt-6-astra low, Pi/DSH Qwen3.8-27B local off.
Les traces, [l'extraction](evidence-extract.json) et `runs/*/final-response.md` conservent
les résultats réels. Charge extérieure, coût monétaire et temps humain inconnus.

## Pi : protection et revue effectives

Pi tente `tee /tmp/b-run.txt` (événement ligne 1202) ; macOS répond « Operation not
permitted » (1206), le fichier est absent. Le pipeline masque ce refus dans son code
de sortie, mais Pi relance ensuite la suite par subprocess et conserve une preuve
réelle dans `handoff/evidence-B.json`. Le reviewer exécute lui aussi les cinq tests.
La protection effective est celle de macOS, pas le booléen `isError` du tool.

Un premier appel de gestion `subagent` utilise à tort `action: send` ; le plugin refuse.
Pi corrige l'appel et reçoit le résultat d'un seul reviewer effectif, 65,6 s, neuf et
bloquant. Celui-ci confirme code/tests/canon/empreintes et expose les limites de preuve.
`REVIEW.md` et les notes de reprise les consignent. Ces erreurs récupérées restent
comptées ; elles n'ont pas produit un second enfant ni une revue fictive.

## DSH : indisponibilité précise, puis clôture injustifiée

Le shell DSH possède déjà un sandbox natif. L'enveloppe macOS du pilote empêche sa
seconde application : `sandbox-exec: sandbox_apply: Operation not permitted`.
Cela affecte même les lectures par bash et l'exécution des tests. Les outils read/write
de fichiers restent utilisables dans le périmètre. Une tentative native d'escalade est
rejetée faute de canal d'approbation ; aucun lancement sans protection n'a lieu.

DSH conserve B et R-A, ajoute un test et produit `evidence-C.json` avec `NOT_EXECUTED`,
`exit_code: null`, des empreintes historiques/nominales explicitement non remesurées.
C'est une disponibilité partielle correctement exposée. Cependant, le mandat exige
vérification puis clôture : déplacer la relance obligatoire « hors de ce mandat clôturé »
est incorrect. Le lecteur constate l'absence d'exécution mais l'accepte comme une clôture
conforme avec réserves. L'état réel est **vérification C à terminer**.

Autres défauts conservés : le journal prétend ajouter un hold à « très ancien âge »
alors qu'ancien et nouveau cas ont déjà l'âge 100 ; l'ordre des âges n'est pas une
condition du tri des identifiants. L'entrée active dite allégée grossit de 3 107 à
3 716 octets. Les informations uniques, sources et preuves historiques restent
présentes ; leur conservation n'excuse pas ces assertions.

## Suite bornée

La [reprise corrective v2](../continuity-confined-v2/protocol.md) conserve ces fichiers
et ces échecs. Elle utilise une seule protection native autour de DSH et de ses enfants,
selon une configuration locale existante vérifiée sans modèle. Deux sessions DSH neuves
doivent terminer les vérifications, rectifier les affirmations et contrôler la reprise.
Pas de modification des entrées ni des résultats de cette série ; pas de gain MP inféré.
Aucun L2, installateur ou changement global des harnesses.
