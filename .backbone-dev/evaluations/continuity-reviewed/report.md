# Rectification conservée et relue ; fidélité globale encore non qualifiée

**Les trois corrections ciblées passent la reprise par un lecteur neuf. Le verdict
strict global reste FAIL**, car ce lecteur produit un faux constat d'absence de date.
La collecte s'arrête ici conformément à la borne annoncée ; pas de nouvelle relance
pour obtenir artificiellement un résultat entièrement vert.

## Intervention explicite, fichiers d'origine conservés

Cette série reprend le projet réel de [la reprise DSH v2](../continuity-confined-v2/report.md),
issu du travail Codex puis Pi équipé. La revue de l'évaluateur énonce trois problèmes
observés : couverture déjà existante, baseline d'empreintes incomplète, clôture avant
vérification obligatoire. Une copie exacte du test B produit par Pi est ajoutée dans
history/, avec SHA égal à celui d'evidence-B. Aucun compte rendu préfabriqué n'est fourni.
DSH doit vérifier les problèmes, écrire son rectificatif et son entrée, puis un DSH neuf
reçoit le prompt lecteur inchangé. Les résultats ne mesurent donc pas une détection
autonome des erreurs ou un gain comparatif de MP.

[Protocole](protocol.md), [verrou avant modèles](source-lock.json),
[origine du test B](history-source.json), [extraction native](evidence-extract.json),
[contrôles mécaniques](validation.json), [conservation exacte](document-conservation-check.json).
Deux sessions DSH 0.1.0-rc.8 / Qwen3.8-27B local off, homes neufs, même projet, protection
macOS externe et shell DSH compatible. Trois observations serveur inactives avant/après,
aucun lancement de modèle parallèle. Les durées natives sont 284,1 s et 142,2 s ;
elles excluent les contrôles périphériques du conducteur. Charge extérieure inconnue.

## Corrections et conservation observées

1. DSH vérifie le SHA de la copie B avant de s'en servir. Il constate le hold à l'âge 100
   déjà exclu dans deux tests ; le test C est un nouvel exemple combiné, non une propriété
   d'âge nouvellement couverte. Le tri porte sur les identifiants.
2. Il distingue les cinq fichiers de la baseline A des sources B attestées à réception
   et de R-A nominal en C puis effectivement mesuré en D. La mesure D ne prouve pas une
   mesure à réception C. Les anciens champs excessifs restent historiques et sont bornés
   par le rectificatif ; leurs valeurs ne sont pas réécrites.
3. Il situe la satisfaction de la vérification obligatoire en D : C reste NOT_EXECUTED,
   D contient l'exécution réelle des six tests. Aucun test n'est relancé pour cette pure
   correction documentaire, et les deux nouveaux agents le déclarent explicitement.

Exactement trois fichiers changent : ajout de `handoff/RECTIFICATIF.md`, copie identique
de l'ancienne entrée dans `handoff/REPRISE-D.md`, réécriture de `handoff/REPRISE.md`.
Code, tests, décisions, sources et journaux/preuves historiques restent identiques.
La nouvelle entrée pointe prioritairement vers le rectificatif. Elle passe de 3 903 à
2 161 octets, mais dépasse la cible indicative d'environ 1 500 ; cette limite est avouée.
L'archive augmente : l'allègement du démarrage n'est pas une économie de stockage.

Le [lecteur neuf](runs/step4-MP/final-response.md) retrouve mandat, B/14 jours/N-B-27,
A remplacée, P-2 non approuvée, Ivo/base A/retour tardif, rejet des 7 jours, combinaison
de tests retenue, vérification réellement achevée en D et suivi **LANTERNE-42 hors Q-27**.
Il retrouve les trois rectifications et situe REVIEW.md à l'étape B, sans lui attribuer
une revue des étapes ultérieures. Il ne modifie aucun fichier portable.

## Échec résiduel, sans correction des sorties

Au §2, le lecteur cite correctement la date d'approbation A du 5 septembre 2026. Au §8,
il prétend que le document ne contient « aucune date » et qu'elle n'est pas sourcée.
Or la première ligne de [decision-A.md](runs/step4-MP/workspace/docs/decision-A.md)
contient explicitement `approuvée 2026-09-05`. Son diagnostic d'absence de preuve est
faux et contradictoire avec sa propre réponse. Cette erreur ne modifie pas le canon
retenu, mais interdit un PASS de fidélité documentaire complète.

Autres limites : l'expression « immuabilité par empreintes » des notes ne décrit pas
une interdiction de modifier ; une empreinte permet une comparaison. Git n'a aucun
commit dans cette branche. Les formulations « attestations B/C » du rectificatif exigent
sa réserve explicite : C n'apporte pas une mesure effective de R-A. Une relecture courte
ne doit pas perdre cette limite. Les preuves natives complètes de l'évaluateur restent
hors contexte du lecteur ; ses réserves sur la revalidation historique sont légitimes.

## Conclusion bornée

Création Codex, actualisation Pi avec vraie revue, réconciliation et vérification DSH,
rectification puis conservation en DSH neuf ont été observées sur des fichiers réellement
produits, sans dépendance aux sessions. Le fonctionnement technique est établi sur ce
cas et cette machine, après corrections de profils et revue explicite. **L'autonomie
fiable du cycle complet et la supériorité de MP sur M0 ne sont pas démontrées.**

Les contrôles mécaniques passent, les copies temporaires de clés sont retirées, les
réglages globaux restent identiques et la distribution reste vide. Voir le
[mode opératoire interne](../../operations/cross-harness-continuity.md) et les
[propositions de conception](../../design/deterministic-continuity.md). Aucun L2 ni
installateur ; aucune installation de VBB sur l'agent concepteur.
