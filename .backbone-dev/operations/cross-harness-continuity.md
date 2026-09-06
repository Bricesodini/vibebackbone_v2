# Continuité inter-harness — mode opératoire interne issu du pilote

Ce document sert à reproduire une expérience isolée ou préparer une mission autorisée.
Il n'installe rien sur la factory et ne constitue pas un composant VBB distribuable.
Les résultats et limites effectifs figurent dans les rapports
[équipé](../evaluations/continuity-equipped/report.md),
[confiné](../evaluations/continuity-confined/report.md) et
[reprise corrective](../evaluations/continuity-confined-v2/report.md), puis
[rectification et lecteur final](../evaluations/continuity-reviewed/report.md).
La mécanique fonctionne sur ce cas ; la fidélité documentaire intégrale reste non qualifiée.

## Profils vérifiés sur cette machine

| Harness | Modèle utilisé | Équipement et rôle |
|---|---|---|
| Codex CLI | gpt-6-astra, low | Création du travail et de sa mémoire, workspace-write |
| Pi 0.84.2 | Qwen3.8-27B UD-Q4_K_S local, off | Reprise et actualisation ; pi-subagents 0.42.1, un reviewer bloquant |
| DeepSeek Harness 0.1.0-rc.8 compilé | même Qwen local, off | Réconciliation, preuves, clôture puis lecture en session neuve |

DeepSeek Harness n'implique pas l'utilisation d'un modèle DeepSeek. Pi charge le paquet
existant explicitement ; aucune mémoire Hippo ou autre mémoire globale n'est nécessaire
à ce pilote. Le reviewer ne remplace ni une approbation métier ni une protection système.

Configurer les providers dans des homes privés temporaires, sans exposer les clés dans
les fichiers portables. Pour Pi, `reasoning: true` avec
`compat.thinkingFormat: qwen-chat-template` permet ici à `--thinking off` d'envoyer
`enable_thinking: false`. Pour DSH, déclarer `reasoningEfforts.off: null`, la même
compatibilité et `agent-default-model.reasoningEffort: off`. Vérifier la requête réelle,
pas seulement le libellé du profil. Ces détails dépendent des versions observées.

Le [reviewer](../evaluations/continuity-equipped/reviewer-v2.md) et sa
[configuration](../evaluations/continuity-equipped/plugin-config.json) sont les profils
expérimentaux vérifiés. `extensions:` vide est accepté ; `extensions: []` avait été
interprété comme un nom de fichier. Un appel avec `agent`, `task`, `async: false`,
`context: fresh` produit la revue ; `action: send` n'est pas cet appel. Aucun enfant
parallèle, aucune tâche programmée, aucune délégation récursive.

## Protection native et séquence

Sur ce macOS, l'enveloppe `sandbox-exec` protège les écritures de Pi, DSH et leurs
enfants : projet isolé, home temporaire et traces du run autorisés ; sources reçues
protégées ; `TMPDIR` privé, cache JITI désactivé. Sonder avant lancement une écriture
permise et des écritures refusées. Une simple consigne dans le prompt n'avait pas empêché
les écritures dans `/tmp` ; la revue documentaire ne les avait pas détectées.

DSH possède déjà une protection shell qui ne peut être imbriquée dans cette enveloppe
macOS. La composition vérifiée utilise `DSH_PERMISSION_MODE=danger-full-access` **uniquement
à l'intérieur de l'enveloppe externe obligatoire**. Les droits effectifs restent bornés
par macOS, y compris pour bash et ses enfants. Le [contrôle natif](../evaluations/continuity-confined-v2/preflight/native-shell-probe-v2.json)
montre commande autorisée à l'intérieur et écriture refusée à l'extérieur. Ne pas lancer
ce profil seul, modifier le réglage global ou retirer la protection pour résoudre un refus.
Un autre OS/harness doit être requalifié avec ses propres capacités natives.

Lancer **un essai à la fois**. Attendre sa fin complète puis trois observations de slots
inactifs avant le suivant ; après timeout, vérifier aussi la fin côté serveur. Un statut
inconnu interrompt la série. Le serveur reste partagé : slots inactifs ne signifient ni
réservation ni absence de requêtes futures. Budget du pilote : 600 s par passage, reviewer
240 s inclus ; ces valeurs ne garantissent pas un temps maximal sur un autre projet.

## Documents à créer et à entretenir pendant la mission

1. Fixer mandat, canon approuvé, provenance, sources reçues, faits critiques et oracles
   avant la collecte. Une proposition récente ou un test vert ne crée pas d'autorité.
2. À la première étape, l'agent produit une entrée de reprise courte : liens vers mandat
   et canon, état réel, réalisé/restant, inconnues, preuves et prochaine action. Noms libres.
   Les preuves désignent commandes effectivement exécutées, résultats et octets testés.
3. Après une décision approuvée nouvelle, actualiser code, tests et entrée ; conserver
   le prédécesseur et borner ses preuves à l'ancienne révision. Revoir les affirmations
   contre les fichiers ; un exemple supplémentaire n'est pas automatiquement un gain
   de couverture. Consigner les constats fondés et leur traitement.
4. Transmettre le **projet**, y compris son Git si une preuve le cite. Garder les sessions,
   homes, caches et artefacts natifs des plugins à part. Contrôler les empreintes du
   passage ; le prochain harness doit retrouver l'information essentielle sans ces sessions.
5. Pour un retour tardif, préserver auteur, base et contenu. Comparer au canon actuel,
   distinguer intégré/rejeté/inconnu et conserver les informations uniques hors mandat.
6. Clôturer seulement après satisfaction effective du mandat. Un contrôle obligatoire
   indisponible reste du travail à terminer ; le décrire ne suffit pas à autoriser la clôture.
   Après correction, conserver l'échec et l'ancienne preuve comme historiques, ajouter une
   nouvelle preuve et actualiser l'état. Alléger l'entrée sans effacer les sources utiles.
7. Faire reconstruire l'état par un lecteur neuf, sans mutation : mandat, canon et
   approbation, décisions remplacées, provenance de la revue, retours, preuves/limites,
   clôture réelle et suivi unique. Évaluer sa réponse contre les fichiers et les oracles,
   pas seulement son assurance ou son arrêt normal.

Les scripts sous evaluations sont des conducteurs de collecte, avec des chemins privés
historiques nettoyés après usage. Pour une reproduction, préparer un nouveau dossier et
ses profils, revalider les capacités, figer les entrées et conserver les nouveaux échecs.
Ne pas écraser un run existant. Aucun synchroniseur, contrat L2 ou installateur n'est requis
pour ces opérations documentaires ; aucune supériorité de MP sur M0 n'est démontrée.

## Rectificatif U04 — composition et observabilité

La qualification [AGENTS](../evaluations/agents-common-v2/report.md) montre deux limites
absentes du contrôle historique ci-dessus. Elles ne requalifient pas rétroactivement les
anciens résultats, mais interdisent de considérer ce guide seul comme preuve de séquence.

- Si la factory est interdite en lecture, Node peut avorter lorsque stdout/stderr y sont
  redirigés. Écrire les traces natives dans le home privé autorisé, puis archiver après fin.
  Tester les redirections exactes au préflight ; une sonde capturée par pipes est insuffisante.
- Le bundle base DSH présent monte un provider LLM de titre automatique. Il peut appeler le
  modèle concurremment au principal. Inventorier la composition effective et retirer ce
  provider du profil privé avant une future qualification séquentielle. Vérifier les
  requêtes internes, pas seulement les processus et les slots entre passages. Cette correction
  de profil n'a pas encore fait l'objet d'une collecte dans U04.
