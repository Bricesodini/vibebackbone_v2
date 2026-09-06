# Étude de mécanismes — G1, Backbone Know et mémoire externe

2026-09-06. Étude demandée par Brice ; aucun composant installé, aucun code Know exécuté, aucune adoption. G1 reste **NOT_READY**. Cette étude ne remplace ni la matrice runtime ni ses confirmations.

## Besoin causal observé

L'audit indépendant G1 distingue conservation, accès, exposition dans le contexte, compréhension observable, restitution et autorité. Les six lecteurs T3/C1/C2 ont reçu le fait unique dans leurs sorties d'outils. Plusieurs ne le restituent pas. C1-V affirme à tort l'absence de prédécesseur pourtant lié ; T3-N affirme absent un dossier de preuve existant ; C1-N affirme une indisponibilité Playwright non étayée. Cela justifie d'étudier suivi des références, vérification des assertions négatives et couverture de restitution. Une panne de stockage ou un manque d'embeddings n'est pas établi. Les notes originales FAIL restent intactes ; une adjudication distincte doit éviter d'assimiler omission finale et perte physique.

## Backbone Know : mécanismes retrouvés et portée

Inspection en lecture seule du dépôt Know au commit `b955aa97863d8692faa3a34f12c8baf48b38bbe0`. Les règles et statuts V1 restent propres à ce dépôt. Les résultats ci-dessous sont historiques, lus et non rejoués pour V2.

| Mécanisme | Source inspectée dans Know | Preuve et limite | Question V2 |
|---|---|---|---|
| Ancres liées à une révision SHA-256, plages UTF-8 et citation exacte | `tools/t12gr_anchor_poc_v02.py`, `docs/benchmarks/t12gr-anchor-contract-v02.md` | CONF-01 initial NO_GO ; CONF-01B 132 cellules, exactitude PASS mais efficience FAIL | Distinguer preuve courante, référence périmée et simple ressemblance, sans certifier le sens ni l'autorité |
| Relocalisation exacte puis distance de Levenshtein sur octets | `relocate`, lignes184–209 du même outil | Une occurrence donne un candidat ; égalité de scores donne ambiguïté. Seuil0,60 propre au prototype ; aucune promotion automatique en référence vérifiée | Aider à retrouver un passage déplacé ; ne corrige pas une fausse absence quand le lien fonctionne déjà |
| Projection de lecture, regroupement de requêtes et admission des sélecteurs | `tools/t12gr_anchor_readpath_poc_v04.py`, résultats CONF-01C/C2 | C2 est candidat à confirmation réaliste, pas architecture promue ; contraintes empêchant de promouvoir un sélecteur ambigu | Option si volumes/latences le justifient ; G1 ne montre pas de besoin PostgreSQL |
| Contrat de preuves et vérification de complétude | `tools/t12c_query_engine.py::evidence_contract/completeness` | Code réel mais références attendues liées aux fixtures/intents connus. Ce n'est pas un extracteur général d'obligations depuis du texte libre | Tester un contrôle de couverture dérivé des exigences consommateur, sans oracle injecté ni promesse de complétude sémantique |
| Routage lexical et hybride, décomposition d'intentions | `tools/t12d_query_planner.py`, `docs/benchmarks/t12g-results.md` | Holdout48 :44 entièrement corrects, une route forcée, verdict NO_GO conservé | Ne pas importer un routeur comme autorité ; vérifier les demandes composées et séparer livrable et contrainte de forme |
| Recherche lexicale, granularité, temporalité, contexte sous budget, ablations | `docs/audits/intent-decomp-20260716-1709.md`, run programme E0–E7 | Programme de POC documenté, pas preuve que toutes ces capacités sont implémentées ou validées | Réutiliser les questions expérimentales : gain marginal, couverture, coût total et changements de documents |

Les optimisations de lecture et les garanties sur les octets ne démontrent pas une meilleure synthèse par un agent. Un graphe de références, un index lexical ou une sélection sous budget seraient des candidats distincts, à comparer à documents et consigne égaux. La simple existence d'un prototype ne justifie ni dépendance ni schéma mémoire imposé dans V2.

## Services : frontières à vérifier avant un éventuel essai

Documentation officielle consultée le 2026-09-06 ; aucune version de SDK installée ou qualifiée.

**Mem0 Platform V3** documente une extraction additive en un appel LLM et une recherche hybride. Les faits produits par l'agent sont aussi mémorisés ; le traitement d'ajout est asynchrone. Pour V2, une affirmation de fin de tâche doit donc rester une affirmation attribuée, distincte de la preuve du résultat. Il faudrait qualifier la fin réelle des traitements auxiliaires, le filtrage par projet, la provenance, le retrait et la reproductibilité de la version. Ces propriétés ne sont pas démontrées par notre campagne. Ne pas transposer automatiquement cette documentation Platform à une variante OSS. [Migration officielle](https://docs.mem0.ai/migration/platform-v2-to-v3).

**Honcho**, dans sa documentation v2, organise messages, sessions et représentations de peers et décrit une couche de raisonnement en arrière-plan. La sérialisation annoncée concerne les tâches affectant une même représentation ; d'autres tâches peuvent être parallèles. Cela ne suffit pas à notre exigence de modèles strictement séquentiels, auxiliaires compris. Une intégration éventuelle demanderait une frontière d'exécution observable et une distinction entre source, fait dérivé et autorisation. [Architecture officielle](https://honcho.dev/docs/v2/documentation/core-concepts/architecture).

Ces services peuvent faire l'objet d'une comparaison ultérieure si une valeur propre à leur rôle apparaît. Leurs scores généraux et descriptions commerciales ne valent pas qualification de notre reprise de développement.

## Ordre de décision

1. Adjudication atomique append-only de G1 et inventaire déterministe des références déjà présentes ; aucune réparation de mémoire.
2. Diagnostic préfixé sur copies inchangées : effet d'une demande explicite de couverture versus consigne courte actuelle, avec les mêmes routes lecteur. Ce sont des reproductions de diagnostic, jamais des confirmations remplaçantes.
3. Choisir une intervention à partir du défaut restant : contrat de restitution, suivi de liens, sélection documentaire ou mécanisme externe. Vérifier un gain distinct, coût et complexité compris.
4. Toute modification ouvre son gel, puis des cas métier nouveaux et confirmations tenues à part. Produit modifié : nouvelle archive, qualification exacte et revue fraîche.

Aucune décision de rôle ne transfère à un index, résumé ou score l'autorité des décisions. Le document ordinaire et ses sources doivent rester consultables après retrait. Aucun runtime modèle VBB, aucune installation factory, aucun corpus privé envoyé à un service par cette étude.
