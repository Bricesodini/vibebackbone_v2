# Configurer DSH depuis une référence Pi fonctionnelle

Statut : stratégie candidate explicitement proposée par Brice après U04, le 2026-09-05.
Conception interne ; aucun runtime produit, L2, installateur ou nouveau lancement modèle.

## Interprétation corrigée

DSH est en developer preview et sa composition est personnalisable. L'échec U04 porte
sur le profil headless choisi, dont un provider de titre lance une requête concurrente.
Il ne démontre pas une incapacité du harness à fonctionner séquentiellement. La suite
peut construire une composition adaptée, au lieu de traiter le bundle par défaut comme
une frontière immuable ou de limiter la correction au symptôme du titre.

Pi peut servir de référence technique, capacité par capacité, pour configurer DSH. Le
profil Pi U04 fonctionne pour le chargement AGENTS et le dialogue séquentiel observé ;
les essais U03 apportent des preuves complémentaires d'outillage et de mémoire avec leurs
limites. Aucun de ces résultats ne qualifie tout Pi ni une fidélité autonome complète.
Le « runtime Pi » désigne ici le profil expérimental du harness, pas un runtime VBB V2
à distribuer ou à appliquer à l'agent concepteur.

## Fondement local

Le README DSH annonce la developer preview et des changements incompatibles. Le bundle
base documente la composition par lignes de plugins adressables par id et les patches de
profil ; remplacer une ligne remplace son bloc config entier, sans fusion implicite.
L'adaptateur `dsh-llm-pi-ai` s'appuie sur `@earendil-works/pi-ai`, ce qui fournit un point
d'appui concret pour traduire endpoint, modèle et compatibilité de requête.
Ce partage d'adaptateur n'établit pas l'équivalence des boucles d'agent et des plugins.

Sources locales consultées et empreintes : [manifeste](../research/2026-09-05-dsh-from-pi/sources.json).
Profils expurgés et preuves déjà disponibles :
[configuration U04](../evaluations/agents-common-v2/preflight/profile-configs.json),
[réception observée](../evaluations/agents-common-v2/loader-assessment.json),
[écart de séquence](../evaluations/agents-common-v2/sequence-violation.json).

## Traduction à effectuer explicitement

| Aspect de la référence Pi | Cible DSH | Vérification nécessaire |
|---|---|---|
| Même endpoint, modèle exact et protocole | Route `llm-pi-ai`, modèle par défaut | Requête effectivement émise ; aucune substitution |
| Qwen thinking off et compatibilité | `reasoningEfforts.off`, effort par défaut et compat | `enable_thinking: false` dans la requête |
| Contexte 131072, sortie déclarée 8192 | Capacités et limites explicites adaptées à DSH | Distinguer capacité déclarée et plafond réellement envoyé ; pas d'héritage supposé |
| Retry Pi désactivé dans U04 | Politique de retry DSH explicite | Examiner les retries du provider et ceux de la boucle ; omission DSH non équivalente |
| Une requête utile à la fois | Composition sans titre LLM automatique ni autre appel auxiliaire concurrent | Inventaire des plugins, requêtes internes et fins effectives |
| AGENTS racine découvert, sources identiques | Loader DSH natif conservé | Racine/sous-dossier/session neuve ; ne pas copier le prompt système Pi |
| Outils nécessaires et protection éprouvée | Outils DSH natifs et enveloppe externe compatible | Même comportement permis/refusé avec les redirections réelles |
| Reviewer Pi, seulement s'il est dans le mandat | Capacité native DSH équivalente si disponible | Qualification séparée ; aucun import présumé du paquet pi-subagents |
| Documents de continuité du projet | Mêmes fichiers et obligations, sessions natives distinctes | Création/actualisation/relecture réelle, sans note parfaite injectée |

U04 fixe `maxTokens: 8192` et retry désactivé côté Pi ; le profil DSH enregistré ne fixe
pas ces deux éléments de la même façon. La documentation de l'adaptateur DSH indique une
politique normale avec cinq retries en cas d'omission. Ce sont des écarts de configuration
à examiner, pas la preuve que des retries ont eu lieu dans les essais collectés.

## Chemin de qualification candidat

1. Choisir un profil Pi précis et ses preuves, puis reconstruire sa configuration dans
   un home neuf. Revalider uniquement les capacités nécessaires à la mission visée.
2. Écrire un inventaire Pi → DSH : équivalent configuré, différence native conservée,
   capacité absente, ou inconnue. Épingler versions, dépendances et composition effective.
3. Construire un profil DSH privé minimal répondant au même besoin. Traduire les réglages
   explicites, conserver le loader et les outils utiles, retirer les appels auxiliaires
   automatiques inutiles. Garder le titre déterministe si utile. Inspecter le résultat
   composé ; ne pas copier aveuglément les fichiers Pi ou patcher les globals.
4. Vérifier sans modèle le démarrage, les secrets référencés, les permissions et les
   redirections. Figer ensuite le profil, le protocole, les prompts et les oracles avant
   la collecte. Les valeurs encore inconnues empêchent de déclarer une équivalence.
5. Tester Pi puis DSH, strictement séquentiellement, avec comptage des requêtes principales
   et auxiliaires. Une même entrée documentaire n'impose pas des prompts système natifs
   identiques. Conserver les différences et indisponibilités, sans chercher trois PASS.
6. Après réception et séquence qualifiées, mener la mission mémoire ; seulement ensuite
   ouvrir le micro-pilote déterministe déjà préparé. Réintroduire un équipement optionnel
   une capacité à la fois, si le besoin justifie son coût et une qualification séparée.

Une évolution de DSH impose de revalider les surfaces affectées et la composition, sans
réécrire les observations précédentes. Cette stratégie autorise l'adaptation technique
comme piste de conception ; elle ne transforme ni Pi ni ses conventions en autorité V2.
Les collectes U04 closes et leurs empreintes restent intactes.

## Forme produit à examiner ensuite

Brice propose aussi un [mode natif Vibe Backbone V2](vbb-native-mode.md). Un profil DSH
configuré et qualifié pourrait en être le premier candidat. L'idée reste à décider après
preuve du besoin et du fonctionnement ; elle ne transforme pas l'expérience en L2.
