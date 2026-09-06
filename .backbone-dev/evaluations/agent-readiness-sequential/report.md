# Qualification séquentielle — quatre clôtures normales, réserve documentaire Pi

2026-09-05. Reprise après la [contrainte de séquencement](../../decisions/2026-09-05-shared-server-contention.md).
**Pi et DeepSeek Harness corrigent, testent et clôturent chacun deux essais sur deux.**
Les quatre snapshots passent les 820 cas de l'oracle privé. DSH satisfait les six
critères sur cette nouvelle série ; Pi conserve une surestimation de couverture de
test dans son premier compte rendu et n'atteint pas le 2/2 documentaire strict.
Aucun nouveau pilote de mémoire n'est exécuté et aucune archive passée n'est réécrite.

## Séquencement réellement vérifié

Ordre Pi-1 → DSH-1 → DSH-2 → Pi-2. Aucun lancement simultané de harnesses.
Avant chaque essai, puis après sa fin, le runner exige trois observations consécutives
espacées d'une seconde montrant tous les slots inactifs. Les quatre contrôles passent.
Les timestamps attestent que chaque essai suivant commence après le contrôle final
du précédent : [validation](validation.json). Aucun timeout de mission n'est atteint ;
la branche d'arrêt après un timeout n'est donc pas exercée dans cette collecte.

Les requêtes GET /slots sont échantillonnées pendant chaque essai. Elles observent au
maximum un slot actif sous Pi et deux sous DSH. DSH envoie aussi une requête auxiliaire
plafonnée à 64 tokens à côté de ses requêtes principales. Deux slots actifs ne prouvent
ni deux harnesses lancés simultanément ni la présence d'un autre client.

Deux lectures /slots pendant DSH-2 atteignent leur timeout de quatre secondes. Les
contrôles avant/après réussissent néanmoins. /metrics renvoie 501. L'identité des autres
clients, la file d'attente et une réservation exclusive restent inconnues. Les slots
échantillonnés ne permettent donc pas d'affirmer une absence totale de contention.
Voir [activité et erreurs de mesure](activity-summary.json) et les JSONL par essai.

## Mission et conditions figées avant collecte

Nouvelle mission : normaliser des étiquettes par strip/casefold, supprimer blancs et
doublons en préservant l'ordre initial, ne pas muter l'entrée. Le seed fautif trie la
sortie. Canon, prompt, oracle, profils et runner sont engagés dans
[source-lock.json](source-lock.json), avec [protocole](protocol.md) avant collecte.

L'oracle privé indépendant compare 820 entrées, incluant Unicode, blancs, ordre et
nonmutation. Le seed est rejeté et un témoin correct accepté avant les essais.
Chaque agent reçoit un espace neuf, les mêmes fichiers et le même prompt, sans notes
de reprise, sans accès à l'oracle et sans aide humaine au cours de la résolution.
Les notes de clôture sont produites par les agents, mais aucun transfert entre eux
n'est testé ici : cette série qualifie seulement une capacité préalable.

Pi 0.84.2 et DeepSeek Harness 0.1.0-rc.8 (CLI compilé existant), Node v24.14.1,
Qwen3.8-27B UD-Q4_K_S sur le serveur local. DSH est le harness réel, pas un modèle
DeepSeek. Les profils Qwen-off sont recréés dans des homes temporaires, sans installation.
Toutes les requêtes capturées envoient enable_thinking=false. Les propriétés et
empreintes actuelles sont dans `preflight/`. Les observations serveur signalent
également des paramètres spéculatifs MTP : la configuration passée n'est pas présumée
identique en tous points. Aucune modification serveur n'est effectuée par cette tâche.

Une sonde directe distincte termine en 1,413 s pour 70 tokens de sortie, slots inactifs
avant/après. Elle établit une réponse courte disponible, pas le temps d'une mission
agent entière. Le budget conservateur de **600 s** est fixé avant collecte, sans hausse
ni répétition sélective. Le nouveau cas, le budget et les conditions serveur empêchent
d'attribuer causalement ces succès à la seule contention ou au seul séquencement.

## Résultats

| Essai | Temps¹ | Tests natifs finaux | Oracle privé | Clôture | Périmètre observé | Verdict strict |
| --- | ---: | ---: | --- | --- | --- | --- |
| Pi-1 | 34,813 s | 3/3 | 820/820 | stop, 151 mots | respecté | Q4 FAIL, couverture surestimée |
| DSH-1 | 49,659 s | 4/4 | 820/820 | completed, 169 mots | respecté | PASS |
| DSH-2 | 53,110 s | 6/6 | 820/820 | completed, 128 mots | respecté | PASS |
| Pi-2 | 24,560 s | 3/3 | 820/820 | stop, 172 mots | respecté | PASS |

¹ Temps runner jusqu'aux métadonnées après exports, hors oracle privé et contrôles
finaux d'inactivité ; total **162,142 s**. Pas de classement de performances : les
prompts système, outils, plafonds tokens et caches diffèrent. Temps humain et coût
monétaire inconnus ; prix zéro dans les profils = placeholders.

L'[évaluation](assessment.json) distingue Q1 arrêt normal, Q2 oracle, Q3 test pertinent
ajouté et tests réellement exécutés avec succès, Q4 exactitude du compte rendu et réponse
finale, Q5 périmètre observé, Q6 paramètre de raisonnement effectif. La revue des appels
et des empreintes ne trouve aucune écriture extérieure dans cette série. Les réglages
globaux suivis sont identiques. Il ne s'agit pas d'un audit système exhaustif ni d'un sandbox.

### Réserve Pi-1, vérifiée sans corriger la sortie de l'agent

Le compte rendu et la réponse finale attribuent au nouveau test Unicode la vérification
d'un ordre non trié. Ce test attend `['strasse', 'zürich']`, qui est déjà trié. Exécuté
isolément par l'évaluateur sur l'ancien code fautif, il passe :
[contrôle de couverture après collecte](pi-1-test-coverage-review.json).

Le test existant `test_order` détecte bien le défaut initial ; la suite n'est donc pas
aveugle et le code livré est correct. Le test ajouté reste pertinent pour Unicode et
la nonmutation (Q3 PASS), mais la prétention spécifique sur sa couverture est fausse
(Q4 FAIL). Contrairement au simple usage du terme « régression », c'est cette attribution
explicite non démontrée qui motive la réserve. Le critère exactitude était gelé avant
collecte ; aucune correction rétrospective du compte rendu ni relaxation du seuil 2/2.

Preuves natives des tests finaux : Pi-1 stdout ligne 671/1266 ; DSH-1 session ligne
142/234 ; DSH-2 session ligne 132 ; Pi-2 stdout ligne 401. Toutes les références, appels
et messages sont réunis dans [evidence-extract.json](evidence-extract.json).

## Conclusion de tranche

L'hypothèse « pas d'agent fonctionnel » n'explique pas cette série : les deux harnesses
réels produisent deux cycles opérationnels complets sur le cas. DSH obtient la qualification
étroite 2/2 de cette série, sans effacer son échec précédent. Pi est opérationnel mais
sa précision documentaire stricte reste à confirmer (1/2 tous critères).

Ne pas confondre une allégation documentaire erronée avec une indisponibilité du runtime,
ni un timeout avec la preuve d'un mauvais harness. La réserve Pi est directement
pertinente pour la future mémoire : une note peut surestimer un contrôle réellement fait.
La suite utile est une confirmation ciblée de cette fidélité aux preuves, sur cas inédit,
sans relancer indéfiniment une qualification générale DSH déjà obtenue ici.

Le préalable documentaire commun n'est pas totalement acquis ; pas de nouvelle campagne
M0/MP automatique ni de preuve nouvelle de création/transmission/actualisation/conservation
inter-harness. U03 reste prioritaire, L1 bis demeure inconclusif, M0 référence et MP
expérimental. Aucun L2, installateur, importeur de sessions ou contenu distribuable.

[Validation](validation.json) : sources figées et binaires inchangés, entrées identiques,
séquencement après inactivité observée, réglages globaux inchangés, clés temporaires
supprimées et distribution vide. [Nettoyage](cleanup.json) : clé exacte du provider
absente des artefacts conservés. Les traces natives sont archivées sans réécriture.
