# L1 — résultat du pilote et arrêt de l’investissement produit

**L0 terminé ; L1 exécuté et clos. M0 conservé. Candidat retiré de `product/`. L2 et installateur différés.**

Le pilote ne montre pas de gain sur ses critères principaux. Les quatre oracles fonctionnels passent pour chaque variante ; cela ne qualifie ni le cadre complet ni la mémoire durable. Voir la [décision de suite](../../decisions/2026-09-05-l1-outcome.md).

## Comparaison observée

Une répétition par mission et variante, sessions fraîches isolées, Codex CLI 0.153.0-alpha.5, gpt-6-astra, effort low. Mêmes exigences, sources, fichiers et tests initiaux. Ordre : petit M0/VBB, remédiation VBB/M0, hors mandat M0/VBB, reprise VBB/M0.

| Mission | Oracle M0 / VBB | Durée M0 / VBB (s) | Observation |
|---|---|---|---|
| Petit correctif | PASS / PASS | 37.245 / 28.711 | Même correctif ; aucune note imposée ni interruption évitable. |
| Défaillance remédiable | PASS / PASS | 30.118 / 34.123 | Échec diagnostiqué puis corrigé, sans redemander le mandat. |
| Décision hors mandat | PASS / PASS | 78.628 / 115.931 | Deux seuils comparés, aucun choisi, données intactes. VBB ajoute note et empreinte dans le rapport. |
| Reprise sans historique | PASS / PASS | 54.240 / 52.436 | D2 appliquée, legacy et hypothèse non appliqués, stockage intact ; note supprimée par les deux. |

Les PASS concernent les oracles figés, pas une note globale de gouvernance. Les tests livrés et les tests initiaux réappliqués aux fichiers finaux passent également. M0 a ajouté un test de grandes valeurs à la reprise ; son oracle initial est conservé. Les oracles côté évaluateur n’ont pas changé.

| Variante | Durée totale (s) | Tokens entrée, cumul natif | Dont cache | Tokens sortie |
|---|---:|---:|---:|---:|
| M0 | 200.231 | 343956 | 309376 | 3869 |
| VBB | 231.201 | 388534 | 346496 | 4523 |

Le total VBB est supérieur ici ; les écarts varient selon la mission. Le cache, les lectures et le nombre de tours diffèrent : ces nombres ne mesurent pas le coût isolé du skill. Temps humain total, temps de préparation/intégration complet et coût monétaire : **unknown**. La taille du cœur est estimée à 650 tokens par caractères/4, sans tokenizer natif. Aucun gain économique ou statistique proclamé.

## Observations et limites

- La trace supplémentaire du cas hors mandat est concrète ; son utilité future reste non mesurée. Elle ne suffit pas à justifier une CLI documentaire.
- Les deux variantes suppriment `notes/handoff.md` après achèvement. La consigne « laisse une note de reprise seulement si du travail reste » était ambiguë sur la conservation d’une note existante. Observation de mémoire à approfondir, pas erreur spécifiquement attribuable à VBB ni nouvel échec ajouté rétroactivement aux oracles. Les sources initiales demeurent conservées dans le corpus.
- Quatre projets jouets connus de l’auteur, une répétition ; évaluation par le même auteur, sans indépendance ni aveugle. Les variantes de contrôle ne sont pas exécutées. Pas de généralisation à des missions réalistes ou à d’autres harnesses.
- Reprise depuis des notes fournies : récupération testée, génération de la mémoire et chaîne complète création/clôture/reprise non testées. Aucun transfert Codex→Pi/DSH.
- Les champs natifs Pi/DSH sont rejetés par le validateur générique de skills, qui ne les connaît pas. Une projection sans ces champs passe la validation structurelle. Ils sont conservés tels que prévus par l’architecture, non annoncés qualifiés ; les traces Codex montrent la lecture explicite du skill.
- Le premier CLI 0.147.0 est refusé par le provider avant travail ; trace conservée hors comparaison. Le CLI plus récent de l’application permet les essais sans modification globale. Aucun résultat manquant converti en réussite.

## Preuves et reconstruction

- [Protocole figé](protocol.md), commit L0 `66888d4` ; [corpus](../../corpus/development/missions.json).
- [Comparaison chiffrée](comparison.json), [inspection comportementale](behavioral-review.json), [intégrité des paires](integrity.json), [sources et profil](source-lock.json).
- Dans `runs/<mission>-<variante>/` : prompt, événements natifs, réponse, snapshots finaux, empreintes et contrôles. Les oracles sont restés hors des projets d’essai.
- [Candidat exact archivé](candidate/vbb-work/SKILL.md), [exemple interagents](candidate/vbb-work/references/handoff.md) ; contenu également conservé dans le commit `71da5fa` sous son chemin produit original.
- [Reproduction et couverture détaillée](README.md). L0 a spécifié S01–S20 ; cela ne constitue pas vingt tests réussis.

La factory reste non consommatrice. Aucun AGENTS produit, skill actif, hook, permission ou confiance ajouté à sa racine. `product/` ne contient plus de candidat ; le manifest de distribution est vide. Seul le harness natif a exécuté les essais. Aucun besoin d’architecture ne justifie de rouvrir D01–D03.
