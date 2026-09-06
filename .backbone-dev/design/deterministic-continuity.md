# Continuité : opérations déterministes candidates

Statut : **proposition de conception**, issue d'U03 et des essais natifs du 5 septembre
2026. Aucun contrat L2, outil produit ou installateur implémenté. Les scripts de collecte
restent des instruments internes d'évaluation. La [recherche croisée](../research/2026-09-05-deterministic-continuity/review.md)
expose les résultats et contre-preuves de Backbone-know, Vibe Backbone et mattpocock/skills.

## Responsabilités

[AGENTS.md](agents-entry-point.md) fournit une entrée stable : rôle des documents,
conditions de lecture, emplacement de reprise et commandes disponibles. Les documents
conservent le mandat, les décisions approuvées, l'état évolutif et les preuves. Une
procédure ou un skill aide l'agent à interpréter une demande et à examiner les écarts.
Les opérations déterministes calculent des faits bornés. Le harness conserve l'exécution,
les permissions, les modèles, les plugins et l'orchestration des agents.

La convention de mémoire ne doit donc pas devenir un ordonnanceur de harnesses, un
moteur de permissions ou un exécuteur universel de tests. L'approbation d'une décision
reste un fait à sourcer ; un hash, un schéma valide ou un fichier dans Git ne la crée pas.
Les instructions d'AGENTS.md ne constituent pas une protection native des écritures.

## Première priorité : deux erreurs réellement observées

| Opération candidate | Entrées explicites | Sortie bornée | Ce qu'elle ne démontre pas |
|---|---|---|---|
| Comparer des preuves à une baseline nommée | Révision ou manifeste identifié, chemins exacts, état courant | Identiques, modifiés, absents, absents de la baseline ; provenance de chaque comparaison | Approbation, vérité d'une note, exécution passée des tests |
| Inventorier une transmission | Racine autorisée, liste de fichiers et références nécessaires, destination ou inventaire reçu | Présence, taille, empreinte, différence ; référence Git résoluble ou indisponible | Exhaustivité sémantique de la liste, qualité du résumé, autorisation de poursuivre |

Le premier aurait empêché d'affirmer une comparaison de R-A à une baseline antérieure
à sa réception. Le second aurait signalé la référence Git perdue pendant le transport
et les preuves restées dans /tmp. Il faut distinguer un état observé maintenant et
une attestation historique : recalculer aujourd'hui ne prouve pas une mesure à C.
L'outil d'inventaire vérifie le transfert ; le transport effectif reste un choix du
projet ou du harness, sans synchroniseur VBB général.

## Candidats secondaires, seulement si le coût se justifie

- Vérifier les références locales : résolution, absence, ambiguïté, changement depuis
  une référence explicitement fournie. Ne pas confondre fichier trouvé et affirmation vraie.
- Produire une vue courte des résultats calculés avec pointeurs vers les détails.
  L'ordre et les libellés restent stables ; les faits non calculables sont signalés.
  Ne pas demander au LLM de paraphraser obligatoirement cette sortie.
- Vérifier la présence des preuves obligatoires déclarées pour la mission : source,
  commande native observée, résultat, fichiers associés, limites. Une preuve manquante
  empêche un verdict mécanique complet ; des preuves présentes ne valident ni leur
  interprétation métier ni la suffisance des tests.

Une fonction ne recherche pas seule « la bonne décision » par similarité ou récence.
L'agent sélectionne les références à partir du mandat et justifie l'autorité. Une
opération sur entrées structurées ne prouve pas un routeur fiable de langage naturel :
le holdout T12e de Backbone-know est une contre-preuve directe à cette généralisation.

## Forme minimale à expérimenter, sans figer L2

Lecture seule par défaut, racine et références explicites, ordre stable, sorties
idempotentes sur mêmes octets et mêmes entrées. Une projection lisible et une forme
machine doivent provenir du même résultat, sans deux récits entretenus séparément.
Toute sortie indique son périmètre, ses entrées et ce qui n'a pas été vérifié.
Absence, changement, ambiguïté, indisponibilité, non-applicable et inconnu doivent être
distinguables ; une erreur de calcul ne devient jamais une réussite vide.

Exemple de résultat attendu, illustratif et non contractuel : « 5 fichiers identiques à
la baseline A ; decision-B et approbation-B absents de cette baseline, comparés à leur
attestation B ; R-A mesuré actuellement, état à réception non prouvé ». Ce résultat
évite au modèle de reconstruire un programme d'empreintes et de lui inventer une portée.

La révision de couverture (« nouveau cas ou propriété déjà couverte ? »), les raisons
d'une décision et le traitement d'un retour tardif restent des jugements à confronter
aux sources. Un contrôle structurel ne peut pas qualifier automatiquement une clôture.
La conservation des erreurs historiques exige un rectificatif visible, sans effacer
les anciennes preuves. Une entrée courte pointe vers l'historique ; elle ne le détruit pas.

## Évaluation avant toute adoption

Préparer un petit protocole séparé, avec missions et oracles gelés avant collecte :
baseline absente, source ajoutée tardivement, preuve nominale, fichier modifié, référence
Git perdue, lien ambigu, ancienne décision conservée, information unique après clôture.
Inclure des cas nouveaux, pas seulement les défauts déjà montrés à l'agent. Aucun oracle
privé dans les entrées du modèle. Tester aussi limites et erreurs des opérations.

Comparer une pratique manuelle loyale à ces opérations, à AGENTS.md, équipement, accès
aux sources et exigences identiques. Ne pas attribuer à la mémoire l'effet d'un plugin
ou du chargement automatique. Solliciter Codex, Pi et DSH **séquentiellement**, avec
modèles/versions relevés et fin serveur vérifiée. Garder les indisponibilités comme
résultats ; aucune substitution par des sessions Codex.

Mesurer d'abord les erreurs évitées et introduites, la justesse de la reprise, la
conservation et les limites annoncées. Puis compter tokens d'entrée et de sortie,
appels/outils, volume de preuves lu, temps, interventions et coût d'entretien des
entrées structurées. Inclure la documentation de l'outil et ses erreurs/reprises dans
le coût total. Tokens de raisonnement, prix et temps humain indisponibles restent
inconnus. Les octets et le nombre d'appels ne mesurent pas directement le « crédit
cognitif ». Ne pas annoncer une économie sans mesure comparable.

Critère de suite proposé : aucune dégradation sur autorité, preuves et conservation,
réduction observée des erreurs mécaniques, puis bénéfice de coût net reproductible.
Le nombre de répétitions et le seuil de gain devront être arrêtés avant ce nouveau
pilote ; ce document n'autorise pas sa promotion en L2. M0 reste la référence tant que
le gain n'est pas démontré. Aucune ontologie complète, base de connaissance, RAG global,
installation de skills ou reprise du runtime V1 n'est nécessaire à cette proposition.

## Avancement U05 — prototype interne, sans adoption

À la demande de Brice d'enchaîner sur les outils, les deux opérations ont un
[prototype local](../experiments/deterministic-tools/README.md), avec oracles préalables,
20 tests réussis et exemples CLI. Les paramètres restent expérimentaux ; aucun L2.
La [comparaison agentique](../evaluations/deterministic-next/protocol.md) n'a pas commencé.
Le contre-exemple de la liste incomplète reste explicite, aucun gain de coût n'est déclaré.
