# Continuité réelle avec Pi équipé — résultat exploratoire

Les deux chaînes Codex → Pi → DeepSeek Harness → lecteur DSH neuf ont terminé.
La création, la transmission, l'actualisation et la conservation des informations
métier sont observées dans les deux variantes. **Aucun cycle ne satisfait toutefois
tous les critères stricts** : des écritures hors espace et des erreurs documentaires
subsistent. La valeur ajoutée propre de MP reste inconnue. Le cycle complet est
désormais observable ; cela ne transforme pas les anciens essais inconclusifs en succès.

## Capacités réellement utilisées

Codex CLI 0.153.0-alpha.5 avec **gpt-6-astra, low** ; Pi 0.84.2 et DeepSeek Harness
compilé 0.1.0-rc.8 avec **Qwen3.8-27B UD-Q4_K_S local, off**. DeepSeek désigne ici le
harness, pas un modèle DeepSeek. Profils privés temporaires ; réglages globaux inchangés.
Toutes les requêtes Qwen capturées sérialisent `enable_thinking: false`.

Pi utilise le paquet déjà installé **pi-subagents 0.42.1**, explicitement chargé,
avec un reviewer spécialisé, neuf, bloquant, outils read/bash et raisonnement off.
Pas d'installation globale, de mémoire Hippo, de nouveau paquet ou de méthode VBB.
Le premier essai de configuration a échoué (`extensions: []` interprété comme chemin) ;
la seconde sonde a réellement exécuté le reviewer et corrigé une affirmation excessive.
Les deux sont conservés sous `probes/`, avec leurs propres gels d'entrées.

## Comparaison loyale et chaîne de preuves

Lire [le protocole figé](protocol.md), [les oracles](reader-oracle.json) et
[le verrou avant collecte](source-lock.json). Même seed, sources, mission, modèles,
équipement et obligation de revue dans M0 et MP. M0 peut produire toutes les notes
nécessaires ; MP ajoute seulement la convention documentaire. Aucun handoff parfait
préfabriqué : les documents naissent dans les exécutions Codex puis sont entretenus
par Pi et DSH. Les artefacts privés des harnesses ne sont pas transmis.

Mission Q-27 : sélection pure de candidats, A approuvée à 7 jours ; B approuvée à
14 jours remplace A. P-2 propose 3 jours sans approbation. R-A d'Ivo, basé sur A,
propose de revenir à 7 et apporte des tests ainsi que LANTERNE-42, à conserver hors
du mandat clos. Les oracles métier privés couvrent 121 cas ; les témoins distinguent
7, 14 et 3. L'oracle lecteur ne récompense aucun nom de fichier ou format particulier.

| Étape réelle | M0 : secondes / résultat | MP : secondes / résultat |
|---|---|---|
| Codex crée A et sa transmission | 115,0 / normal, oracle OK | 102,0 / normal, oracle OK |
| Pi applique B et obtient sa revue | 406,2 / normal, oracle OK, écritures externes | 204,3 / normal, oracle OK, écritures externes |
| DSH traite R-A et clôture | 265,2 / normal, oracle OK, écritures externes | 268,7 / normal, oracle OK, justification de test erronée |
| Lecteur DSH neuf | 124,1 / sans mutation, faits essentiels retrouvés | 72,5 / sans mutation, faits essentiels retrouvés, confusion sur la revue |

Les [métriques](metrics.json), [événements extraits avec lignes sources](evidence-extract.json)
et `runs/*/final-response.md` permettent de distinguer le récit de l'agent des observations.
Huit fins normales, huit oracles réussis, sources reçues inchangées, six transferts de
fichiers exacts. Trois observations de slots inactifs avant et après chaque essai ;
aucun essai parallèle. La charge externe et la file d'attente restent inconnues.

## Cycle de mémoire observé

- **Création** : Codex produit `transmission/PI.md` et une preuve A pour M0 ; une entrée,
  un journal A et des preuves pour MP. Les deux préservent le mandat ouvert, A approuvée
  et P-2 sans autorité.
- **Transmission et actualisation** : Pi lit les vrais fichiers reçus, applique B au
  code et aux tests, exécute les tests et produit de nouvelles preuves. A reste une
  preuve historique. Un reviewer réel s'exécute dans chaque branche (65,8 et 64,7 s).
  Dans M0, il fait corriger « 7 tests » en « 6 » et préciser les limites du relevé
  avant/après ; dans MP, il fait résoudre la référence au fichier de revue absent.
- **Intégration** : les deux DSH rejettent le retour à 7, gardent Ivo et sa base A,
  conservent les apports utiles et LANTERNE-42. B reste effectif, oracle réussi.
- **Conservation** : les vues actives passent de 6 039 à 5 322 octets dans M0 et de
  2 400 à 2 091 dans MP. Journaux, décisions, preuves historiques et information unique
  restent accessibles. Les deux lecteurs ne modifient aucun fichier portable et
  retrouvent le mandat clos, B, A remplacée, P-2 non approuvée et le suivi hors Q-27.

## Écarts qui empêchent la qualification stricte

1. **Écritures hors espace** : Pi M0 écrit `/tmp/etape2.before.txt`, `etape2.after.txt`
   et `final.txt` ; Pi MP écrit `after-before.json`, `after-after.json`, `test-out.txt` ;
   DSH M0 écrit `avant.txt`, `apres.txt`, `run3.txt`. Voir les appels natifs Pi lignes
   920/1451/7879 et 967, DSH M0 ligne 582. Les preuves correspondantes ont été capturées
   dans `external-evidence/`, puis seules les copies reconnues ont été retirées.
   Leur état antérieur est inconnu ; aucune garantie rétrospective d'absence d'écrasement
   ou d'exposition temporaire entre branches. Le reviewer n'a pas détecté ces effets :
   une revue de documents n'est pas un contrôle technique des écritures.
2. **Git omis par le transfert expérimental** : DSH M0 crée réellement `50a7979`, puis
   l'archive cite `git log` et `git diff`. Le lecteur reçoit les fichiers sans `.git` et
   constate honnêtement l'absence du commit. C'est une perte introduite par le conducteur
   du pilote, pas une preuve d'inaptitude de M0. Le bundle récupéré après collecte est
   conservé comme preuve de l'évaluateur, sans modifier l'entrée du lecteur.
3. **Justification erronée dans MP** : `handoff/retour-R-A.md` prétend que le hold ancien
   n'était pas couvert, tout en décrivant le cas existant d'âge 100, `hold=True`. L'ajout
   d'un cas d'âge 20 est réel mais ne comble pas l'absence alléguée. Le lecteur ne
   relève pas cette contradiction. Le code demeure correct ; le compte rendu ne l'est
   pas entièrement.
4. **Confusion du lecteur MP sur la revue** : il cite plusieurs fois `REVU.md`, absent,
   et finit par dire que seule une revue DSH existe et que la revue Pi n'est pas conservée.
   `handoff/REVIEW.md` documente pourtant la revue Pi réelle. La disponibilité des faits
   dans les fichiers ne garantit pas leur restitution fidèle.
5. **Surinterprétations du lecteur M0** : il présente l'absence d'empreinte du fichier
   de preuve dans ce fichier lui-même comme une lacune, sans exigence du mandat en ce
   sens. Le commit absent est un constat fondé ; toutes ses autres critiques ne sont
   pas des défauts établis. Les approbations synthétiques constituent bien le canon
   prévu de cette mission ; aucune signature externe n'était attendue.

## Coûts et conclusion de conception

Temps mural cumulé : M0 910,7 s, MP 647,5 s, revue incluse. Une seule paire, ordre fixe,
production différente, erreurs différentes et serveur non réservé : **aucun gain de
performance attribuable à MP**. La mesure partielle des notes Markdown exclut les
preuves JSON/texte et certaines notes sous contributions ; elle n'est pas un score de
mémoire totale. Temps humain, phases de rédaction/reconstruction isolées et coût
monétaire restent inconnus. Les traces natives conservent les usages sans rendre
comparables les décomptes de contexte de trois harnesses différents.

La priorité U03 est concrètement éprouvée. Retenir pour la suite les documents projet,
les preuves rattachées aux octets, l'actualisation après décision approuvée et la
conservation après clôture. Ne pas promouvoir MP comme supérieur ni en produit.
La [remédiation opérationnelle séparée](../continuity-confined/protocol.md) conserve
le projet Git et utilise la protection native macOS ; elle ne réécrit pas cette paire
et ne sera pas comparée causalement à M0. Aucun L2 ni installateur.
