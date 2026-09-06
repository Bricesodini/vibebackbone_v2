# AGENTS.md comme entrée commune de projet

Statut : **hypothèse de conception à éprouver**, issue de la question de Brice le
2026-09-05 pendant le pilote U03. Il envisage un AGENTS.md configuré au départ comme
dénominateur commun pour réguler les harnesses. Ce document examine cette piste ;
il ne décide ni installation, ni produit L2, ni modification de l'AGENTS.md de la factory.

## Proposition

Un AGENTS.md de projet peut porter un accord de travail commun et orienter chaque
harness vers le même canon et la même mémoire. Son rôle serait relativement stable :
dire **où entrer**, comment reconnaître une source approuvée, quand actualiser les
documents et sous quelles conditions considérer une mission réellement terminée.
L'état changeant des missions, preuves, retours et inconnues resterait dans les
documents de travail auxquels cette entrée renvoie.

| Élément | Responsabilité envisagée |
|---|---|
| AGENTS.md du projet | Entrée courte, autorité des sources, obligations de reprise/transmission/clôture |
| Canon du projet | Mandats et décisions approuvées, portée, provenance et successeurs |
| Mémoire de continuité | État utile actualisé, artefacts/preuves, retours, inconnues, prochaine action |
| Harness et environnement | Charger les instructions, fournir outils/reviewer, sessions et protections natives |

Cette répartition respecte U03 : la reprise ne dépend pas de la session du prédécesseur.
Elle ne suppose pas qu'un fichier texte puisse imposer des permissions système ou
équiper automatiquement un harness. Les écritures `/tmp` et la clôture prématurée
observées dans le pilote montrent la différence entre une consigne reçue et son respect.

## Ce qui est effectivement documenté

- **Codex** : la documentation officielle décrit un chargement au démarrage, global
  puis du root projet vers le cwd. Priorité par dossier : AGENTS.override.md, AGENTS.md,
  puis noms de repli configurés ; un fichier maximum par dossier. Budget cumulé par
  défaut : 32 KiB. Ce comportement documenté doit encore être vérifié dans le profil
  isolé utilisé ici. [Documentation OpenAI consultée](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **Pi 0.84.2** : le README installé décrit AGENTS.md/CLAUDE.md au démarrage, depuis
  le home global, les parents et le cwd ; AGENTS.override.md remplace le fichier de
  son dossier. `--no-context-files` désactive cette découverte. Ce drapeau était présent
  dans les essais précédents : leur comparaison ne mesure pas une entrée AGENTS commune.
- **DSH 0.1.0-rc.8** : le plugin natif agent-instructions charge le fichier global du
  home DSH puis les candidats de la racine Git au cwd. Les fichiers de base distincts
  et les overlays locaux peuvent tous être ajoutés ; les doublons de contenu sont
  dédupliqués. Le bundle base le monte avec un budget de 65 536 octets. Le plugin décrit
  aussi la découverte imbriquée et les transitions après certains appels de fichiers.

Les chemins et empreintes des sources locales figurent dans
[sources.json](../research/2026-09-05-agents-entry/sources.json). Ce sont des capacités
documentées dans les versions présentes, pas encore trois preuves comportementales
de chargement du même AGENTS.md. Les anciennes traces restent inchangées.

## Dénominateur commun proposé

Commencer par un seul AGENTS.md court à la racine du projet, une racine/cwd explicite
et des homes d'essai isolés. Éviter initialement les overlays, fichiers concurrents
et règles imbriquées : leurs sémantiques diffèrent. Ne pas dupliquer le canon métier
ni le journal de session dans ce fichier. Une configuration initiale du projet
pourrait inscrire les chemins réels et les contraintes approuvées après examen de
l'existant ; elle ne doit pas écraser aveuglément les instructions du propriétaire.

Contenu candidat, à adapter au projet et à évaluer :

1. Désigner l'entrée de mémoire et les sources du mandat/canon ; vérifier leur état.
2. Distinguer approbations, propositions et contributions ; une note ne crée pas d'autorité.
3. Actualiser l'entrée avant passage, après changement de décision ou retour pertinent.
4. Relier chaque preuve au contrôle réellement exécuté et aux octets/révision concernés.
5. Garder les prédécesseurs, les retours et les faits uniques accessibles après clôture.
6. Laisser une vérification obligatoire indisponible comme travail restant ; ne pas
   clôturer en la déplaçant artificiellement hors mandat.
7. Respecter les capacités et protections natives ; signaler explicitement un moyen absent.

Le choix des outils, modèles, plugins et paramètres de sandbox reste propre au harness.
AGENTS.md peut exiger une revue lorsqu'elle est requise ; il ne prouve pas qu'un reviewer
existe ou a tourné. La qualification doit observer le résultat réel et sa provenance.

## Prochaine expérience proposée, indépendante de la paire mémoire

Avant tout déploiement, trois sondes **séquentielles** sur les vrais harnesses :
AGENTS.md racine avec marqueur vérifiable, prompt qui ne recopie pas la consigne,
preuve du contexte chargé ou observation clairement bornée à la réponse. Vérifier
absence d'override/global inattendu, comportement en sous-dossier et changement de
fichier après redémarrage. Une indisponibilité reste telle quelle.

Ensuite seulement, mission courte avec interruption/reprise et mise à jour de mémoire,
obligations portées par AGENTS.md. Garder distincts le facteur **point d'entrée des
instructions**, le facteur **convention de mémoire** et l'**équipement du harness**.
M0 peut lui aussi disposer d'un bon AGENTS.md ordinaire : lui en retirer l'accès
fabriquerait un avantage artificiel. Aucun installateur ni schéma L2 nécessaire.

Le bénéfice recherché est un démarrage cohérent sans recopier les mêmes demandes dans
chaque conversation. L'obéissance garantie, l'application identique des priorités et
l'amélioration de la fidélité restent des hypothèses à vérifier.

## Observation U04, sans adoption

Le [second gel AGENTS](../evaluations/agents-common-v2/report.md) observe les trois sondes
sur les trois vrais harnesses, sans consigne recopiée dans le prompt ni appel outil.
Pi et DSH transmettent les octets de l'accord dans leur première requête ; Codex fournit
une preuve comportementale. Cela réduit l'incertitude sur la réception du fichier racine
sur ces profils isolés, sans qualifier les overrides ou le refresh à chaud.

La qualification stricte échoue sur la concurrence interne du provider de titre DSH.
La mission de création/actualisation/relecture mémoire n'a donc pas été exécutée.
L'hypothèse de continuité reste ouverte ; aucune adoption commune ni gain MP n'en découle.
