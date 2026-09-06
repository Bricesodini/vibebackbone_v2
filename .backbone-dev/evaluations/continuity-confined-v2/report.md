# Protection native compatible, vérification réelle, fidélité encore insuffisante

**La reprise technique réussit ; la qualification documentaire stricte échoue.**
DSH exécute effectivement les six tests puis conserve une preuve associée aux fichiers.
Le lecteur neuf retrouve B, R-A, les limites C et LANTERNE-42. Les deux agents conservent
cependant des assertions fausses sur la nouveauté d'un test et la portée des empreintes.

## Conditions et filiation

Reprise des fichiers réellement produits par la dernière session de
[continuity-confined](../continuity-confined/report.md), sans correction humaine des notes.
La mission et les sources restent celles du pilote Q-27. Deux sessions DSH neuves,
Qwen3.8-27B UD-Q4_K_S local off, exécutées séquentiellement avec trois observations
inactives avant/après. [Protocole](protocol.md), [entrées gelées](source-lock.json),
[extraction](evidence-extract.json), [validation mécanique](validation.json).

Le shell DSH est configuré avec `DSH_PERMISSION_MODE=danger-full-access` **sous une
protection externe macOS obligatoire**. L'enveloppe borne les droits effectifs de DSH
et de ses enfants. Aucun réglage global modifié, aucun lancement sans cette enveloppe.
La [sonde native v2 sans modèle](preflight/native-shell-probe-v2.json) établit l'exécution
interne et le refus d'écrire à l'extérieur. La première sonde est conservée avec son erreur
de nettoyage `ctx.dispose()` ; elle n'est pas une réussite complète.

| Session | Durée native | Résultat |
|---|---:|---|
| DSH, reprise D | 253,0 s | Arrêt normal ; six tests exécutés, deux passages ; oracle privé OK |
| DSH, lecteur neuf | 113,1 s | Arrêt normal ; six tests relancés ; oracle privé OK ; aucun fichier portable modifié |

## Ce que la reprise établit

`evidence-C.json` reste NOT_EXECUTED. La nouvelle `evidence-D.json` contient EXECUTED,
sortie 0, six tests et leurs sorties réelles, corroborées par les tool results natifs.
Les SHA de queue.py et test_queue.py correspondent aux fichiers reçus après C et transmis
au lecteur. D produit des mesures de sources protégées ; toutes sont inchangées selon
le conducteur indépendant. A/B/C et leurs preuves sont conservés sans réécriture.
Les homes et sessions natifs sont distincts ; la continuité passe par le projet.

## Ce que la reprise ne corrige pas

- Le journal D prétend une nouvelle couverture du hold très ancien, alors que B avait
  déjà un hold à l'âge 100 dans deux tests. L'ajout C est une combinaison supplémentaire.
  L'ordre des âges ne définit pas l'ordre de tri des identifiants.
- Les preuves D nomment une comparaison générale à `protected-before.json`, alors que
  cette baseline ne contient que cinq fichiers. B et son approbation arrivent plus tard ;
  R-A est reçu en C, avec empreinte nominale, puis mesuré effectivement en D. Ces sources
  ne peuvent pas être déclarées toutes comparées à la baseline initiale.
- Le lecteur accepte l'absence générale de contradiction et manque ces deux problèmes.
- La vue active passe de 3 716 à 3 903 octets : son allègement annoncé n'est pas observé.

La réussite du code et des contrôles système ne qualifie donc pas le récit. Le lecteur
ne dispose pas des traces natives privées ; sa capacité à prouver rétrospectivement
l'exécution reste bornée aux pièces portables. Git est conservé dans le projet, mais
aucun commit n'est créé dans cette série : transport d'un historique Git non vide non testé.

## Suite bornée et statut

La [dernière rectification documentaire](../continuity-reviewed/report.md) reçoit les
problèmes précis et la copie exacte du test B, reliée à sa preuve historique. Il s'agit
d'une intervention de revue après observation, pas d'un essai aveugle ni d'une nouvelle
comparaison M0/MP. Aucun gain mémoire inféré, aucune nouvelle qualification générale.
Les copies privées de clés sont retirées après toute la collecte ; réglages et identités
natifs inchangés vérifiés. Aucun L2, installateur ou fichier produit ajouté.
