# Précision utilisateur — charge concurrente du serveur partagé

2026-09-05. Complément d'interprétation au [rapport de qualification Pi / DSH](../evaluations/agent-readiness/report.md)
et au [pilote L1 bis](../evaluations/l1bis/report.md), après la précision de Brice :
« il peut etre plus long si on le solicite en meme temps ».

La qualification a lancé ses essais de harness successivement. Cela ne garantit pas
l'exclusivité du serveur Qwen : d'autres clients pouvaient le solliciter et DSH émet
aussi des requêtes auxiliaires. La charge globale, l'attente en file et le temps GPU
par requête n'ont pas été mesurés. Une contention externe est donc une hypothèse
possible, ni confirmée ni exclue. Le temps mural ne doit pas être assimilé au seul
temps de travail du modèle pour cette mission.

Le timeout atteste seulement l'absence de clôture dans le budget mural et les conditions
observées. Il ne suffit pas à attribuer une lenteur ou un manque de fiabilité au harness,
ni à conclure que son agent est non fonctionnel. La formulation précédente « fiabilité
DSH encore insuffisante » doit être comprise comme une qualification non acquise dans
ces conditions, et non comme un diagnostic causal sur DSH.

Les autres constats restent distincts : attentes de tests erronées, écritures hors
périmètre, compte rendu absent à l'arrêt. La contention possible ne les efface pas et
ne transforme pas un essai en PASS. Aucun budget ni critère passé n'est changé ;
les archives scellées et leurs résultats restent intacts. Ce complément n'établit
aucune nouvelle valeur comparative de MP contre M0.

## Contrainte explicite de Brice : exécution séquentielle

Brice précise : « il ne faut pas lancer en meme temps mais de manière séquencier
pas parralèle ». Ne jamais lancer plusieurs essais de harness en parallèle. Attendre
la fin complète de l’essai courant avant le suivant. Après timeout ou interruption,
vérifier aussi la fin ou l’annulation effective de sa requête côté serveur : tuer le
processus client ne prouve pas à lui seul que le serveur a cessé de générer. Si cet
état ne peut pas être vérifié, le signaler et suspendre le lancement suivant plutôt
que présumer une absence de chevauchement. Cette règle porte sur les essais pilotés ;
les appels auxiliaires internes au harness et les autres clients du serveur doivent
être documentés séparément, sans prétendre les avoir contrôlés.

Pour la prochaine collecte :

- Continuer à sérialiser les essais ; vérifier si le serveur peut être réservé ou
  documenter explicitement les sollicitations concurrentes observables.
- Relever, si disponibles, charge, requêtes/slots actifs, attente, temps de génération
  et tokens ; conserver UNKNOWN pour toute mesure inaccessible.
- Calibrer le budget avant la collecte sur une sonde distincte dans les conditions
  annoncées. En présence de contention constatée, marquer l'essai concerné comme
  confondu par la charge pour l'interprétation temporelle ; toute répétition doit
  être une nouvelle exécution identifiée, sans remplacer la trace précédente.
- Distinguer attente serveur, limite de sortie, erreur d'outil, raisonnement erroné
  et respect du périmètre. Aucune hausse de délai a posteriori pour obtenir un PASS.

Aucune nouvelle exécution, réservation ou modification du serveur n'est effectuée
par cette précision documentaire. U03, la frontière VBB/harnesses et l'exclusion de
L2 et de l'installateur restent inchangées.
