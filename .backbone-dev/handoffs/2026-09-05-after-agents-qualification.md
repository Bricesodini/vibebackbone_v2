# Reprise après qualification AGENTS bornée

Lire INDEX, [U04](../decisions/2026-09-05-agents-entry-outcome.md), puis le
[rapport final](../evaluations/agents-common-v2/report.md). Ne pas relancer les collectes
agents-common ou agents-common-v2 : closes, résultats et gels à conserver.

Réception AGENTS : racine/sous-dossier/instruction changée en session neuve observées sur
Codex, Pi et DSH. Capture des octets transmis pour Pi/DSH ; preuve comportementale Codex.
Aucune qualification de continuité par ce point d'entrée : la phase mémoire n'a pas tourné.

Pi/DSH avaient d'abord avorté parce que stdout était dirigé dans la factory interdite en
lecture. Le second gel corrige cette composition : sorties dans home privé, archivage après
fin. Mais DSH appelle automatiquement un LLM de titre en parallèle du principal. Les trois
réponses DSH restent des observations ; la qualification stricte de séquence échoue.

Orientation ajoutée par Brice : DSH est en developer preview et largement configurable.
Lire la [stratégie Pi → DSH](../design/dsh-from-pi-reference.md). Prendre un profil Pi
fonctionnel comme référence de capacités et traduire explicitement sa configuration vers
DSH ; le bundle par défaut n'est pas une contrainte immuable. Les résultats U04 restent
ceux du profil essayé, sans verdict général d'incapacité de DSH.

Avant une nouvelle collecte autorisée :
1. Refaire des homes privés sans clés dans les artefacts. Ne pas réutiliser les homes nettoyés.
2. À partir de la référence Pi choisie, configurer un profil DSH privé minimal : paramètres
   modèle, limites, retries, outils et loader explicites ; retirer le provider de titre LLM
   et les autres appels automatiques inutiles. Inspecter la composition effective et tous les appels
   auxiliaires possibles. Pas de modification globale, ni de simple consigne au modèle
   pour contrôler un plugin natif qui agit hors de son initiative.
3. Reproduire les commandes ET redirections réelles au préflight sans modèle. Garder la
   protection macOS externe, les sources protégées et les oracles inaccessibles.
4. Nouveau protocole et gel avant appels ; ordre séquentiel, compteur de requêtes internes,
   attente de fin locale et serveur ; état inconnu/timeout sans fin attestée = suspension.
5. Qualifier ce profil séparément, puis seulement la petite mission mémoire prévue.

Le [protocole déterministe](../evaluations/deterministic-next/protocol.md) est préparé,
non exécuté. Les cas/oracles sémantiques et budgets sont écrits ; fixtures exécutables,
instrument éventuel et empreintes restent à geler avant toute collecte. Aucun L2 ni
installateur, distribution vide. Aucun gain MP, tokens ou fidélité autonome démontré.

Brice propose ensuite d'envisager un [mode Vibe Backbone V2 natif](../design/vbb-native-mode.md),
par exemple un profil DSH préconfiguré. Option de conception à évaluer après qualification
du profil ; ni adoption L2 ni lancement d'un installateur. Conserver l'accord commun et
les adaptations natives comme responsabilités distinctes.

Avant toute préparation DSH, consulter maintenant le [guide-dsh.md interne](../operations/guide-dsh.md),
créé à la demande de Brice comme point de référence dans le dépôt. Il regroupe le parcours
et pointe vers les preuves, sans remplacer la configuration native ou activer VBB.

## Suite outils U05

Brice a ensuite demandé d'enchaîner sur les outils. Lire le
[bilan U05](../decisions/2026-09-05-deterministic-prototype-outcome.md) et le
[prototype local](../experiments/deterministic-tools/README.md) : comparaison de baseline
nommée et inventaire de transmission, 20 tests réussis, aucun appel modèle. Le protocole
préparatoire conservé précède ce prototype ; le gel exécutable de la comparaison reste
à préparer. Distinguer développement local possible maintenant et collecte agentique,
qui conserve les préalables DSH et mémoire. Aucun L2/installateur ni gain mesuré.
