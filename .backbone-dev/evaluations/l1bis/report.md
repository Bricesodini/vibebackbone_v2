# L1 bis — continuité Codex → Pi → DeepSeek Harness

Date : 2026-09-05. Campagne bornée close : huit essais exécutés, aucun cycle complet qualifié.
**Résultat comparatif non concluant sur la valeur de MP.**
Les passages ont réellement utilisé trois harnesses distincts et des fichiers produits
progressivement. Leur simple possibilité est observée ; le cycle complet de mémoire,
jusqu'à une clôture correcte et sa récupération, n'est pas démontré.
La fonctionnalité des profils Pi/DSH sur cette mission reste une hypothèse ouverte,
conformément à la [précision de Brice](hypotheses.md). Un smoke lecture/écriture réussi
n'était pas une qualification d'agent capable d'achever la mission.

## Préparation et périmètre

Le [protocole](protocol.md), les [oracles](oracles.md), la [convention MP](convention.md),
les prompts et les événements métier sont figés dans [source-lock.json](source-lock.json)
avant collecte. [execution-lock.json](execution-lock.json) fixe ensuite profils et
lanceur. [oracle-selfcheck.json](oracle-selfcheck.json) montre que les témoins corrects
passent et que les mutations de seuil sont rejetées ; ce contrôle déterministe ne
compte pas comme preuve inter-harness.

Mission fictive M-RET-01 : produire un plan d'archivage **simulé**, sans supprimer de
comptes ni modifier les données protégées. Codex implémente le seuil approuvé A (30
jours), Pi reçoit B (45 jours) avec l'approbation de la responsable fictive Nora, DSH
reçoit R-A (retour tardif d'Eli basé sur A : mauvais retour à 30, suggestion utile de
test ordre/casse). Les raisons, approbations et limites existent dans les sources
métier, pas seulement dans les notes. R-A est une contribution synthétique préparée
avant collecte, pas un sous-agent effectivement lancé ni une preuve de concurrence.

M0 a les mêmes faits, exigences de continuité et de conservation, et peut librement
organiser sa documentation. MP ajoute seulement une courte convention de localisation,
provenance, actualisation et conservation. **Aucun handoff préfabriqué** : la fixture
ne contient aucune note de mémoire ; les deux transmissions initiales viennent de
Codex. Les tests locaux et les documents évoluent naturellement dans les deux branches.
Le lecteur final reçoit le même prompt dans les deux variantes, sans ajout MP.

Les copies de travail sont hors du dépôt usine, avec racine Git sans remote. Seuls les
fichiers projet sont transférés ; aucune session native antérieure n'est donnée au
prochain harness. Prompts, événements natifs, snapshots, empreintes et évaluations sont
conservés dans runs/. L'isolation documentaire n'est pas une garantie OS universelle.

## Capacités effectivement disponibles

Voir [le relevé complet](preflight/capabilities.md) et [les profils](profiles.json).

- Codex embarqué dans l'application : 0.153.0-alpha.5, gpt-6-astra, effort low.
  Le CLI PATH 0.147.0 n'est pas utilisé dans les missions.
- Pi 0.84.2 : Ollama par défaut inaccessible ; MiniMax-M3 répond 429/quota atteint,
  malgré exit 0. Ces indisponibilités restent dans les preuves.
- DSH source : échec sur l'export FiberState. Le **build existant** rc.8 fonctionne
  au smoke et est utilisé ; il n'a pas été reconstruit. Ses octets sont épinglés,
  sans prétendre qu'il correspond au HEAD des sources locales.
- Pi et DSH utilisent ensuite le même serveur local RTX3090 et le GGUF Qwen3.8-27B
  Q4_K_S réellement annoncé. Ce modèle diffère de l'identifiant Q4_K_XL encore déclaré
  dans la configuration DSH existante. Le modèle est distinct du harness ; DSH utilise
  ses outils, événements et sessions natifs, pas une session Codex rebaptisée.

Aucune extension de mémoire utilisateur, aucun preset VBB n'est copié. Pi demande
thinking off mais reçoit du raisonnement ; son dernier message MP consomme 8192 tokens
de sortie sans action. Ce plafond de sortie à 8192 est un réglage du profil Pi
isolé préparé pour le pilote, pas une limite générale de Pi. La déclaration du modèle
DSH local a été réduite à son identité et sa fenêtre de contexte ; aucun réglage
effectif de raisonnement n’a été qualifié. DSH utilise les réglages de ses bundles natifs. Les profils sont identiques
au sein des paires, mais l'effort effectif, les dépendances de build et les poids du
serveur ne constituent pas un environnement entièrement maîtrisé. La capture des
configurations non secrètes dans preflight/runtime-configs.json est postérieure au
début de collecte, et le dit explicitement ; les scripts de préparation antérieurs
permettent d'identifier les réglages utilisés, sans prétendre à un gel rétroactif.

## Résultats par opération de mémoire

| Opération | M0 | MP |
|---|---|---|
| Création par Codex | Code A et 6 tests valides ; note de reprise, journal et copie des données créés. | Code A et 6 tests valides ; note et preuve avec SHA-256 du code/tests créées. |
| Transmission Codex → Pi | Sources et état retrouvés depuis les fichiers. | Sources et état également retrouvés ; la trace distingue correctement A, B et le code encore sous A. |
| Actualisation par Pi | Code et tests B, preuve B, ancienne note archivée et transmission DSH enregistrés avant timeout. | Arrêt length avant toute modification ; code A et mémoire A inchangés. Oracle B en échec à cette étape. |
| Transmission Pi → DSH | Reprise effective des artefacts B laissés par Pi. | Reprise effective de l'état non actualisé laissé par Pi ; ne démontre pas une actualisation Pi réussie. |
| Intégration par DSH | Retour au seuil A rejeté ; test ordre/casse ajouté, 7 tests exécutés. Note C enregistrée avant timeout. | Seul le code passe à B avant timeout. Pas de tests B, preuve B ou traitement durable de R-A produit par DSH. |
| Clôture et conservation | Sources conservées ; mission laissée ouverte et note annonçant des opérations d'archivage non réalisées. | Sources conservées ; mémoire/tests encore sous A et aucune clôture. |
| Lecture finale DSH neuf | 7 tests relancés et annonces d’archivage confrontées à l’inventaire ; timeout sans restitution complète. | Lectures, empreintes et tests sans écriture ; timeout sans restitution complète. |

Les détails par critère et leurs contre-preuves figurent dans
[assessment.json](assessment.json). Les PASS éventuels sont locaux à l'opération
observée ; ils ne s'additionnent pas en certification. L'échec d'un livrable après
arrêt natif n'établit pas un défaut causé par MP.

**La conservation après clôture reste inconnue dans les deux branches.** La condition
préalable de clôture n'est pas obtenue. Les sessions finales exécutent le prompt prévu
mais reçoivent réellement des états interrompus ; elles ne peuvent pas réparer cette
couverture après coup. Les fichiers utiles sont toujours présents, ce qui est une
observation de rétention, pas une preuve de récupération complète après clôture.

## Constats vérifiables et limites d'attribution

1. **Lecture et entretien sont distincts.** Pi MP comprend les sources et la modification
   attendue, mais ne produit aucune actualisation. Cela appuie H-AGENT/H-LIMIT autant
   ou davantage qu'un défaut de transmission documentaire ; une paire ne tranche pas.
2. **Un récit peut devancer les effets enregistrés.** La note C M0 affirme que la note
   B a été archivée, que R-A a reçu un statut et que README a été actualisé. Le snapshot
   réfute ces trois assertions. Aucune correction évaluateur n'est appliquée avant la
   reprise. La note porte aussi le 2026-09-06, qui n'est pas la date attestée du run.
3. **Une ancienne réserve peut devenir une fausse interdiction.** DSH M0 laisse la
   mission ouverte en invoquant la réserve des étapes précédentes, malgré la demande
   explicite de clôture de l'étape 3. C'est une erreur documentaire observable, pas une
   raison de créer une autorité ou une permission VBB supplémentaire.
4. **Un test évaluateur ne crée pas de mémoire agent.** Après DSH MP, le code B passe
   notre oracle, mais les tests projet et la preuve A sont périmés. Notre PASS reste
   hors du projet transmis et ne peut être crédité à la mémoire produite par DSH.
5. **Un écart de périmètre est conservé.** Codex M0 a créé une copie de données dans
   /tmp avant de la déplacer dans le projet. X1 échoue pour cet écart ; les données
   métier restent intactes. L'autre branche n'efface pas cette observation.

Les interruptions empêchent d'isoler un effet de convention. Un seul cas exploratoire,
une paire, un ordre, un évaluateur concepteur non aveugle ; aucune indépendance de
revue ni supériorité statistique n'est revendiquée. Aucun retry métier ni remplacement
silencieux de Pi/DSH par Codex. Les profils se montrent **partiellement opérationnels**,
mais leur aptitude à terminer ce cycle dans ces conditions n'est pas qualifiée.

## Coûts et preuves

Les durées exactes, appels d'outils, tailles des documents modifiés et usages natifs
sont dans [metrics.json](metrics.json). Les sorties JSONL/zstd, captures de projet et
contrôles privés sont dans chaque dossier runs/stepN-VARIANTE/.

| Étape | M0, secondes | MP, secondes |
|---|---:|---:|
| Codex : création | 116,764 | 150,644 |
| Pi : actualisation | 300,012 — timeout | 176,293 — length |
| DSH : intégration/clôture | 300,078 — timeout | 300,052 — timeout |
| DSH : lecture finale | 300,050 — timeout | 300,053 — timeout |

Ces durées mesurent les tentatives, pas le temps nécessaire pour achever le travail.
Les essais arrêtés sont censurés ; aucune économie n'est calculée. Les compteurs natifs
de messages terminés peuvent omettre la génération interrompue et, pour DSH, les
requêtes de titre. Le volume de résultats d'outils n'est pas le contexte réellement
lu en tokens. Les tailles des documents modifiés sont des empreintes finales, pas le
nombre d'octets effectivement écrits au fil du run.

Temps humain total, coût monétaire, temps distinct de rédaction/actualisation/
intégration/reconstruction : **inconnus**, conservés comme null. Aucune aide humaine
n'a été fournie aux exécutants pendant collecte ; la préparation, les injections
prévues et l'analyse par l'évaluateur font partie du travail d'usine et ne sont pas
assimilées à zéro coût.

## Suite de conception

Aucune promotion de MP dans product/, aucune conclusion de suffisance générale de M0,
aucun rejet du besoin U03. M0 reste la référence de comparaison ; MP reste un candidat
expérimental dont l'effet est inconnu. La prochaine expérience utile doit d'abord
qualifier les profils Pi/DSH sur une mission distincte avec modification, tests et
clôture normale, vérifier le raisonnement effectif et fixer un budget adapté, puis
préengager une nouvelle paire de continuité. Ce cas déjà examiné ne peut pas devenir
un cas de confirmation aveugle.

Ni L2 ni installateur ne sont implémentés. Aucun contrôle d'exécution, permission,
importeur de sessions ou synchroniseur VBB n'est introduit. La
[validation d'intégrité](integrity.json) distingue l'intégrité des preuves de la
réussite comportementale. Le manifest distribuable reste vide.
