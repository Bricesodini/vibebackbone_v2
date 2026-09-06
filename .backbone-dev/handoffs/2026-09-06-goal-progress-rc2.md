# Reprise du goal actif — candidat local rc.2

La tranche précédente constitue une progression : comparatif six cellules exécuté puis noyau choisi, produit créé, revue fraîche de rc.1, trois défauts reproduits et corrigés dans rc.2 ; qualifications locales passent. Goal actif, ni complet ni bloqué. Brice a adopté les autorisations conditionnelles ; aucune micro-validation à demander.

Lire INDEX, `evaluations/value-2026-09-06/report.md`, `decisions/2026-09-06-minimal-local-core.md`, `evaluations/candidate-rc2/report.md`, puis `evaluations/qualification-rc2/protocol-draft.md`.

## État concret

- product/ contient vbb.py (mesures + lifecycle), continuity.py (2 opérations en lecture seule), agreement.md optionnel, README, profiles.md (statuts encore pending), bundle.json.
- `tooling/distribution.json` liste six fichiers exacts. `tooling/build_candidate.py` produit **rc.2**, refuse de remplacer une même version par d'autres octets. Changer la version pour toute correction, préserver archives/gels.
- Archive actuelle `.backbone-dev/releases/vbb-0.1.0-rc.2.tar.gz`, SHA256 `220aed795dc8bca30f4b58f630bcf6f75e96fbd1cc28dad5b4cd4fb61b067ef7`. rc.1 historique conservée.
- 20 tests lifecycle + 3 frontière passent (`python3 -B -m unittest discover -s tooling/tests -v`) ; 20 mesures sur module **extrait** et CLI réel (`python3 -B tooling/qualify_candidate_local.py`). Mise à jour réelle rc.1→rc.2 et retrait préservant mémoire dans candidate-rc2/real-upgrade.json.
- Reviewer Codex neuf sur rc.1 : trois défauts statiques, puis reproductions dynamiques par évaluateur (candidate-rc1/reproductions.txt). rc.2 ajoute digest initial AGENTS, journal du résultat de son retrait, préservation mode/ownership, et supprime création de bytecode lors des mesures. Les états pending historiques rc.1 sans digest initial ne sont pas rétroactivement qualifiés. ACL étendues non qualifiées.
- Comparatif Pi : F (fraîcheur) N/C/T et T (transmission) T/C/N, équipement constant. Les outils donnent des sorties exactes/reproductibles ; aucun gain global de coût. La baseline T se trompe sur compte/ambiguïté ; C reconstruit les sorties ; T a une causalité non prouvée dans son rapport. Aucun changement de source ni perte de règle unique ; pas de garantie de fidélité complète.
- FRET-62 reste strictement échoué (fausse archive, reconstructions, temporalité). Son gel4 améliore la récupération, jamais PASS autonome. Ne pas le répéter jusqu'à vert.

## Action suivante

Matérialiser puis geler la nouvelle qualification du candidat **installé** selon qualification-rc2/protocol-draft.md : 3 triviaux + nouvelle mission spécialiste choisi/erreur/correction/décision B/retour A/transmission/outils/lecteur + retrait et lecteur sans produit (8 appels prévus). Le runner de tests de cette fixture produit des preuves structurées natives ; il reste hors distribution et n'est pas une troisième commande VBB. Mémoire initialement absente, aucun résultat idéal injecté. Adapter des détails raisonnables avant le gel seulement.

## Profils et isolation

Les templates privés du comparatif sont **nettoyés** par value-2026-09-06/close.py. Ceux d'integrated-2026-09-06 aussi. Ne pas relancer leurs conducteurs/profiles.json comme prêts à l'emploi, ni relancer leurs prepare.py sur place : fichiers gelés. Reconstituer des homes/profils neufs dans qualification-rc2, par copie adaptée du preparer integrated ; configs expurgées dans integrated/preflight/profile-configs.json. Clé choisie [PRIVATE_PROVIDER] lue sans affichage depuis ~/.dsh/.credentials.yaml et seulement écrite dans home privé neuf.

Le runner de value protège docs/input/source/received ; celui du nouveau cas devra protéger aussi .vbb (installateur exécuté par conducteur entre passages), .specify/specs, spécialistes non choisis et runner de tests. Toute exécution Codex/DSH en mode interne permissif reste obligatoirement sous sandbox-exec externe. Sorties réelles dans home autorisé, archive après fin. Instrumentation capture-fetch.mjs observe débuts/fins, prime-pi-fetch.mjs nécessaire Pi. Aucun modèle/sous-agent parallèle, aucun titre/reviewer auxiliaire, aucun réseau outil agent. Nouveau preflight sans modèle avant gel.

Les six appels comparatifs et le reviewer rc.1 sont terminés normalement ; rien à attendre actuellement. Trois observations slots inactifs après chaque passage, cloud Codex fin normale CLI seulement. Tous les secrets temporaires d'exécution retirés ; validation.json du comparatif confirme globals et gels inchangés, zéro match des trois secrets connus testés.

## Obligations restantes

Qualification de mémoire et mission sur trois harnesses, spécialiste choisi/non choisi par fixtures, trivial sans cérémonie, retrait et mémoire lisible par lecteur neuf, revue fraîche **du candidat final exact** (rc.2 corrigée pas encore relue), profils précis et documentation de support réaliste. Toute modification de profiles.md changera l'identité archive : conserver les hashes des composants inchangés et requalifier les surfaces affectées, lifecycle exact et revue. Aucune publication/push/global/factory install. Aucun commit factory encore fait ; préserver tous changements préexistants.
