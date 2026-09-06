# Vibe Backbone V2 — candidat local minimal

Deux outils de mesure en lecture seule et une consigne optionnelle de continuité projet. Python 3.10+ standard ; Git pour vérifier des références Git. Aucun service, appel modèle, routeur, session ou réglage global.

**Candidat en qualification, pas une release validée.** Les outils mesurent des fichiers ; ils ne certifient pas l'autorité ou la fidélité d'un agent. Les profils et limites sont dans [profiles.md](profiles.md).

## Essayer dans un projet isolé

Extraire l'archive dans un répertoire, puis créer un projet distinct :

```sh
mkdir /tmp/vbb-essai
python3 -B /chemin/archive/vbb.py install --project /tmp/vbb-essai
python3 -B /chemin/archive/vbb.py inspect --project /tmp/vbb-essai
```

L'installation ajoute `.vbb/` et un bloc attribuable dans `AGENTS.md`. Elle active explicitement la consigne de reprise pour ce projet. Elle préserve le contenu AGENTS préexistant. Lire [agreement.md](agreement.md) pour le sens commun ; les documents métier et les permissions natives conservent leur autorité. Aucune installation sur la factory de conception.

Lancer ensuite son harness natif depuis le projet. Les profils sont distincts ; ce paquet n'en configure ni les credentials ni l'isolation. Une réponse triviale ne demande aucun document de mémoire.

## Comparer à un manifeste déclaré

Un manifeste JSON `baseline.json` décrit une baseline explicitement nommée et des observations taille/SHA256 :

```json
{"name":"A","files":{"p.txt":{"size":3,"sha256":"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"}}}
```

Cette entrée correspond aux trois octets `abc`. Une sélection `selection.json` :

```json
{"paths":["p.txt","late.txt"]}
```

```sh
python3 -B .vbb/vbb.py compare --root . --baseline baseline.json --baseline-name A --request selection.json
```

`not_in_baseline` indique un enregistrement manquant, pas une absence historique. Le manifeste est déclaré par son auteur ; son hash ne certifie ni l'instant, ni l'exécution ni la réception passée. Sa création/maintenance et sa sélection restent une responsabilité du projet.

## Inspecter une transmission

```json
{"paths":["memory/ENTRY.md","docs/decision.md"],"references":[{"name":"review","candidates":["reviews/note.md","archive/note.md"]}],"git_refs":["HEAD"]}
```

```sh
python3 -B .vbb/vbb.py inventory --source /chemin/source --destination /chemin/recu --request transmission.json
```

Deux candidats présents restent ambigus même si leurs octets sont égaux. L'outil ne choisit aucune autorité. Un fichier requis hors sélection reste invisible à l'instrument : confronter la sélection au mandat. Les racines sont explicites ; rien n'est copié et aucun test métier n'est lancé.

JSON par défaut ; `--format text` projette le même résultat. Code 0 : éléments sélectionnés égaux ; 1 : différence, absence, ambiguïté ou non-enregistrement ; 2 : entrée invalide ou mesure indisponible. Lire le détail même au code 2. **Aucun code ne vaut approbation ou clôture métier.** Les chemins sélectionnés avec liens symboliques sont refusés ; racines normalisées. Worktrees avec fichier `.git` non pris en charge par la vérification Git, pas d'audit des alternates/configurations Git, pas de snapshot atomique de l'arbre.

## Cycle de vie local

Répéter `install` avec le même paquet rétablit les fichiers gérés absents mais refuse les fichiers divergents. Pour un autre paquet explicite :

```sh
python3 -B /chemin/nouveau-paquet/vbb.py install --project /tmp/vbb-essai --update
python3 -B /chemin/nouveau-paquet/vbb.py inspect --project /tmp/vbb-essai
python3 -B /chemin/nouveau-paquet/vbb.py remove --project /tmp/vbb-essai
```

Le retrait retire uniquement les fichiers dont les octets correspondent au reçu, ainsi que son bloc AGENTS exact. Les autres textes AGENTS, la mémoire et les données projet restent. Les fichiers gérés modifiés et les fichiers inconnus sont conservés comme résidus déclarés. Le reçu `.vbb/receipt.json` reste alors disponible pour inspection ; ne pas le modifier pour forcer un effacement. Le code retour 1 indique des résidus non entièrement retirés ; 2 un refus/une erreur. `inspect` expose le détail des fichiers et de l'entrée AGENTS.

Une interruption peut laisser l'état `pending` décrit par le reçu écrit avant les mutations. Relancer **le même paquet** pour terminer, ou retirer les effets attribuables ; ne pas lancer une autre mise à jour sur un état pending. Le reçu décrit aussi le résultat attendu du retrait du bloc AGENTS, pour reconnaître ce résultat après interruption. Les octets et le mode POSIX du fichier préexistant sont préservés ; les ACL étendues ne sont pas qualifiées. Les écritures sont atomiques fichier par fichier, pas transactionnelles sur tout le projet. Utiliser un seul écrivain pendant une opération de cycle de vie ; concurrence d'installateurs et modifications simultanées ne sont pas prises en charge. Aucun rollback aveugle ni écrasement forcé.

Après retrait, les documents ordinaires de mémoire restent lisibles directement. Une session neuve ne doit pas prétendre avoir chargé une consigne retirée ; le retrait des fichiers n'efface pas les conversations ou caches déjà détenus par un harness.

Un arrêt brutal pendant une écriture peut laisser un temporaire `.vbb-write-*` dans `.vbb`. Il est signalé comme résidu et conservé, sans attribution fondée sur son seul nom ; examiner son contenu avant un nettoyage manuel. Le retrait ne déclare pas une suppression complète tant que ce résidu existe. Un dossier `.vbb` entièrement vide est inspecté comme `empty` et peut être retiré par répétition de `remove`, même sans reçu : aucun fichier utilisateur n’y est supprimé.
