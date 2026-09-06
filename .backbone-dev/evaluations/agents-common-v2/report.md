# Qualification AGENTS commune — résultat borné

**Réception observée sur les trois harnesses ; qualification stricte non acquise.**
Date : 2026-09-05. Protocole et oracles gelés avant appels dans [freeze.json](freeze.json).
Aucun L2, installateur, équipement global ou composant distribuable ajouté.

## Résultat

| Capacité | Codex CLI | Pi | DeepSeek Harness |
|---|---|---|---|
| Version native vérifiée | 0.153.0-alpha.5 | 0.84.2 | 0.1.0-rc.8 compilé |
| Modèle/effort | gpt-6-astra low, configuration et tour CLI | Qwen3.8-27B local off, requête observée | même Qwen local off, requête observée ; aucun modèle DeepSeek |
| AGENTS racine, réponse attendue | observé | observé | observé |
| Même AGENTS depuis work/ | observé | observé | observé |
| Instruction changée, session neuve | observé | observé | observé |
| Octets AGENTS dans première requête | indisponible dans la trace CLI collectée | observé, contexte system | observé, message user natif |
| Zéro outil et mutation pendant sondes | observé | observé | observé |
| Ordre séquentiel des processus | observé | observé | observé |
| Absence de requête auxiliaire concurrente | pas de requête auxiliaire exposée par CLI ; visibilité cloud limitée | une requête locale par passage | **échec : titre automatique concurrent** |
| Création/actualisation/relecture mémoire | non exécutée, préalable strict non satisfait pour la tranche commune | idem | idem |

Les neuf réponses passent les oracles **comportementaux de loader**. La première requête
Pi/DSH contient l'accord exact ; le prompt ne révèle aucun marqueur et interdit les outils.
Pour Codex, l'usage du bon marqueur, y compris après changement, est une preuve
comportementale compatible avec le chargement, pas une capture directe de sa requête.
Détails et réponses : [loader-assessment.json](loader-assessment.json).

**Le prérequis strict échoue** : DSH appelle son modèle principal et le provider natif de
titre dans le même passage. En racine, les requêtes HTTP commencent à 21:35:27.989Z et
21:35:27.992Z. L'historique confirme `session/title-llm-request` et le titre produit.
Les trois passages DSH présentent cette composition. Preuve ciblée avec lignes natives :
[sequence-violation.json](sequence-violation.json). Aucun passage mémoire lancé après
ce constat ; [SUSPENDED.json](SUSPENDED.json) verrouille le conducteur.

La séquence de processus et les trois observations serveur inactif avant/après chaque
passage ne suffisent donc pas à établir la séquence des requêtes **internes**. Le contrôle
précollecte aurait dû inventorier ce provider auxiliaire ; il ne l'a pas fait. Cet écart
vient de la composition du profil choisi et du contrôle insuffisant du conducteur ; il
n'est pas un défaut d'obéissance à AGENTS ni une autorisation implicite de parallélisme.

## Première collecte et correction technique séparée

La [première collecte](../agents-common/report.md) reste conservée : trois succès Codex,
six indisponibilités natives Pi/DSH, sans requête locale observée. Node avortait lorsque
stdout pointait vers la factory interdite en lecture. Le diagnostic sans modèle reproduit
l'arrêt avec cette redirection et réussit avec une sortie dans le home autorisé.

Ce second gel déplace seulement les sorties natives dans le home privé, puis les archive
après fin. Les fixtures, prompts et oracles sont identiques en octets ; toutes les cellules,
y compris Codex, ont été refaites sous le nouveau gel. Il ne remplace pas les échecs V1.
Les trois commandes natives avec redirection réelle passent avant le second gel :
[launch-checks.json](preflight/launch-checks.json). Aucune troisième collecte corrective.

## Profils et protection

Homes neufs à chaque passage ; racine Git indépendante hors factory ; absence de fichiers
concurrents dans les ancêtres contrôlés. Le projet revient identique à chaque harness ;
le même projet sert aux trois sondes de ce harness et seule l'instruction est remplacée
avant le troisième passage. Aucun paquet/reviewer ajouté, aucune mémoire préfabriquée.
Pi active sa découverte et l'approbation du projet isolé (`--approve`), avec extensions,
skills et templates désactivés. Le bundle headless DSH conserve ses plugins natifs,
dont le provider de titre découvert après collecte.

Sandbox macOS externe obligatoire : écritures bornées au projet/home/traces ; docs et
AGENTS en lecture seule, factory/oracles illisibles. Les modes internes Codex/DSH
`danger-full-access` sont contenus par cette enveloppe. C'est un profil expérimental
**différent du Codex workspace-write historique**, sans modification de réglage global.
Sondes DSH réelles : écriture permise, refus hors racine et dans canon, refus de lecture
d'oracle dans [native-probes.json](preflight/native-probes.json). Les sondes loader ne
qualifient pas l'usage métier des outils ni la fidélité documentaire.

Les sessions et requêtes ont terminé, les groupes locaux ont disparu et les slots sont
inactifs après chaque passage. Aucun timeout. Le serveur reste partagé et non réservé.
Les fins cloud Codex ne sont pas directement observables : fin normale CLI uniquement.

## Différences documentées, non généralisées par cet essai

Codex : chargement global puis racine–cwd, override prioritaire et budget documentés dans
la [documentation officielle consultée](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Pi : AGENTS/CLAUDE, parents et cwd, override du dossier, désactivation possible par
`--no-context-files`. DSH : chaîne Git–cwd, candidats de base et overlays, déduplication,
contexte durable user et transitions après outils de fichiers. Sources et empreintes :
[loader-sources.json](preflight/loader-sources.json).

Aucune collision d'overrides, troncature, session reprise, découverte dynamique ou
portabilité inter-version testée. La session « changed » est neuve, pas un test de refresh
à chaud. Pi ajoute dans sa dernière réponse « pas de docs/mandat.md à lire » alors que le
fichier existe : formulation non étayée à conserver, hors oracle du marqueur et sans
qualification de fidélité narrative. Aucun gain mémoire/MP/coût déduit de ces sondes.

## Suite

L'accord racine court est un candidat techniquement reçu par ces trois profils. Il ne
constitue ni permission native ni garantie de continuité. Avant toute nouvelle collecte,
préparer un profil DSH privé sans provider de titre LLM, inspecter sa composition effective
et tous les appels auxiliaires possibles, puis geler et qualifier séparément ce profil.
Ne pas modifier les globals ou réécrire ces résultats. La phase mémoire prévue reste
non qualifiée, et doit précéder la comparaison déterministe.

Le [protocole déterministe suivant](../deterministic-next/protocol.md) est préparé seulement :
deux opérations, baseline manuelle loyale, cas nouveaux, coûts de maintenance et oracles
sémantiques. Pas de prototype ni collecte ; gel des octets exécutables encore nécessaire.
Nettoyage, intégrité et frontière produit : [validation.json](validation.json).
