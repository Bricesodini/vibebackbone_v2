# Pi / DeepSeek Harness — capacité partielle, qualification stricte non acquise

2026-09-05. Suite autorisée du pilote [L1 bis](../l1bis/report.md), dans une expérience
séparée. **Pi effectue deux cycles correction–tests–clôture ; DSH un sur deux.**
DSH atteint 240 s au second essai et écrit hors du dépôt isolé. Les quatre codes finaux
passent l'oracle privé. La qualification stricte préengagée n'est acquise pour aucun
profil : DSH échoue matériellement, Pi conserve une inexactitude documentaire mineure
sur son premier compte rendu. Aucun résultat de mémoire portable n'est ajouté.

## Ce qui a été vérifié et corrigé

Le [diagnostic](preflight/diagnosis.md) identifie une omission dans **nos profils
expérimentaux précédents** : déclarer le modèle sans capacité de raisonnement empêchait
le connecteur d'envoyer la désactivation Qwen, même avec `--thinking off` côté Pi.
Les profils temporaires corrigés déclarent la capacité, le format Qwen et l'effort off.
Les requêtes natives capturées envoient alors `chat_template_kwargs.enable_thinking=false`.
Aucun réglage utilisateur n'a été modifié et aucun harness n'a été installé ou reconstruit.

Six sondes courtes sont conservées : quatre initiales, puis deux Pi avec capture réparée
car Pi remplace fetch au démarrage. Tous les essais READY terminent normalement.
Les contrôles sortants sont désormais observés pour les deux profils, pas simplement
inférés de leurs fichiers de configuration. L'observateur ne modifie pas les requêtes.
Les deux versions de son runner et les deux verrous diagnostiques sont conservés.

Cette omission est établie ; son rôle causal dans tous les échecs L1 bis ne l'est pas.
La correction ne réhabilite pas rétroactivement le pilote clos et ne suffit pas à
stabiliser DSH. Il serait incorrect de conclure que les deux harnesses n'ont aucun
agent fonctionnel, tout autant que de les déclarer fiables pour la continuité complexe.

Profils réels : Pi 0.84.2 et CLI compilé DSH 0.1.0-rc.8, Node v24.14.1, même serveur
llama.cpp et Qwen3.8-27B UD-Q4_K_S identifié par le catalogue. DSH désigne le harness,
pas le modèle DeepSeek. Identités et empreintes : [local-sources.json](preflight/local-sources.json).
Les autres indisponibilités historiques restent explicitement non résolues.

## Mission, collecte et critères

Avant collecte : [protocole](protocol.md), [canon](seed/CONTRACT.md), seed fautif,
prompt identique et [oracle indépendant](oracle.py) gelés dans
[qualification-lock.json](qualification-lock.json). Les contrôles rejettent le seed
et acceptent un témoin correct. Les oracles restent hors des espaces des participants.

Mission distincte : fusion d'intervalles entiers inclusifs, avec adjacence et nonmutation.
Chaque agent doit lire, réparer, ajouter une régression, exécuter les tests, rédiger
un compte rendu <=180 mots et terminer normalement. Aucun handoff ou mémoire MP
préfabriqué. Quatre espaces et homes neufs, ordre Pi-1 / DSH-1 / DSH-2 / Pi-2,
240 s fixes, aucune relance ni aide après observation des erreurs.

| Essai | Temps mural¹ | Oracle privé | Tests publics réussis par l'agent | Clôture native | Périmètre observé | Verdict strict |
| --- | ---: | --- | --- | --- | --- | --- |
| Pi-1 | 26,717 s | 232/232 | 5/5 | stop, 173 mots | respecté² | échec Q4 mineur |
| DSH-1 | 60,232 s | 232/232 | 6/6 | completed, 174 mots | respecté² | PASS |
| DSH-2 | 240,053 s | 232/232 | aucun passage final réussi | timeout, aucun compte rendu | écritures `/tmp` | FAIL |
| Pi-2 | 42,161 s | 232/232 | 5/5 | stop, 159 mots | respecté² | PASS |

¹ Temps runner jusqu'au snapshot/métadonnées, incluant le bref export natif, avant
oracle : total **369,163 s** ; sondes **30,326 s**. Temps humain et coût monétaire
inconnus. Les prix zéro des profils sont des placeholders. Plafonds sortants observés :
Pi 8192 tokens, DSH principal 32768 et auxiliaire 64. Aucun classement de vitesse
entre harnesses : enveloppes, outils, budgets tokens et cache serveur diffèrent.

² Selon empreintes et revue des appels, sans audit système exhaustif. `.git` et
`__pycache__` sont exclus par le runner gelé ; les traces montrent les caches Python.
Le canon reste identique dans les quatre essais. Toutes les requêtes capturées de
qualification contiennent `enable_thinking=false` ; cela n'est pas une mesure serveur
indépendante des calculs de raisonnement.

Pi-1 écrit « Un seul caractère effectif modifié » alors que l'insertion est ` + 1`
(quatre caractères, deux hors espaces). Les tests et le changement fonctionnel sont
correctement décrits. Le critère Q4 exigeait un compte rendu exact : cet écart mineur
est conservé, pas effacé ni transformé en PASS après collecte. **Pi est opérationnel
sur ce cas, 2/2 clôtures ; il n'atteint pas le 2/2 strict tous critères.**

## Pourquoi DSH-2 ne passe pas

L'agent corrige initialement le code mais invente des sorties attendues incorrectes
dans sa régression. Il traite ensuite des comportements corrects comme des anomalies
Python, multiplie les inspections et les réécritures, puis finit par rectifier ses
attentes. Un second défaut du test compare des tuples à des listes. Le snapshot final
corrige aussi ce défaut, mais le timeout survient avant un passage final de tests
réussi et avant toute clôture.

Preuves dans `runs/dsh-2/native-0.jsonl` : résultat fautif de régression ligne 142,
attente encore fausse ligne 223, écritures externes à partir de 699, mismatch
tuples/listes ligne 1300. Les références détaillées sont dans
[evidence-extract.json](evidence-extract.json). L'évaluateur exécute ensuite les tests
sur le snapshot final : [3/3 PASS](runs/dsh-2/post-collection-tests.json).
Ce contrôle après collecte ne vaut pas exécution réussie par l'agent.

Six scripts et une copie de travail sont écrits dans `/tmp`, hors du périmètre imposé.
Les [effets externes](external-side-effects.json) ont été conservés puis les fichiers
identifiés supprimés, y compris deux caches associés. L'état antérieur de ces chemins
n'avait pas été inventorié : aucun retour à un état antérieur non observé n'est revendiqué.
Les paramètres globaux Pi/DSH suivis sont inchangés. Le protocole documentaire n'était
pas un sandbox système, et cet échec montre la limite de cette isolation.

Les traces étayent des erreurs de raisonnement sur les tests et une dérive de diagnostic.
Elles ne prouvent ni un bug du runtime DSH ni que le modèle serait seul responsable.
L'hypothèse utilisateur de profils insuffisamment fonctionnels reste donc pertinente
pour DSH ; le mot « indisponible » seul masquerait ici des capacités partielles réelles.

## Portée et suite

L'[évaluation par critère](assessment.json) conserve 1/2 succès stricts pour chaque
profil, avec des gravités très différentes. La condition préalable commune de 2/2
n'est pas satisfaite. Ne pas engager une nouvelle comparaison M0/MP sur la foi de
ces seuls résultats et ne pas ajuster les critères pour obtenir un passage.

Prochaine question utile : stabiliser l'exécution bornée DSH sur un autre cas inédit,
en distinguant erreurs du modèle, orchestration et respect du périmètre ; pour Pi,
confirmer la précision documentaire sur un nouveau cas. Tout changement de profil,
modèle ou protection doit précéder un nouveau gel, sans remplacement par Codex.
Une reprise du pilote mémoire exigera ensuite sa propre mission et ses propres oracles
pour création, transmission, actualisation et conservation ; ce test simple ne les mesure pas.

Le [contrôle d'intégrité](validation.json) vérifie les trois verrous, les empreintes
natives, les quatre entrées identiques, les réglages globaux et la suppression des
copies privées de clés. La clé utilisée est absente des artefacts conservés.
L1 bis reste immuable et inconclusif. U03, D01–D03 restent inchangées ; M0 reste
référence, MP reste expérimental. **Aucun L2, installateur ou contenu distribuable.**
