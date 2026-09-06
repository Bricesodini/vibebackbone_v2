# Architecture cible proposée — VBB V2 léger

Statut : base de mise en œuvre, interne à la fabrication. D01 (cadre léger) est une décision utilisateur ; les mécanismes ci-dessous sont des choix de conception à qualifier. Références : [décisions](../decisions/2026-09-05-scope-and-architecture.md), [audit V1](../research/2026-09-05-implementation-planning/v1-audit.md), [harnesses](../research/2026-09-05-implementation-planning/harnesses.md).

## 1. Produit et promesse

VBB fournit un **contrat de travail réutilisable et une mémoire de projet sélective**. Il permet à un agent de reprendre une mission, poursuivre dans le mandat, exploiter les méthodes du projet et rendre un résultat avec des preuves proportionnées. Il réduit les décisions répétées et les pertes de contexte sans posséder la boucle d'exécution.

Consommateur initial : Brice et ses projets de développement utilisant Codex, Pi ou DSH. La première version cible un coordinateur par mission, avec des agents contributeurs éventuels et des passages d'un harness à un autre. Pas de service multiutilisateur, de synchronisation cloud ou de flotte distribuée.

Promesses exclues : garantie de sécurité par prompt, exactement-une-fois des effets, annulation transactionnelle d'actions déjà lancées, indépendance statistique des reviewers, découverte exhaustive de toutes les instructions chargées, effacement rétroactif des contextes. Elles relèvent d'un autre système ou sont inobservables.

## 2. Composants minimaux

| Composant prévu | Responsabilité | Hors responsabilité |
|---|---|---|
| Un skill `vbb-work` et ses références progressives | Mandat, continuation, reprise, qualification, revue, mémoire | Décrire toutes les disciplines ; router toutes les demandes |
| Contrats de mémoire JSON, documentation lisible et exemples | Liens entre mission, décisions, preuves et retours | Dupliquer specs, tickets, sessions natives ou historique Git |
| Utilitaire `vbb` local, sans daemon | Installer/retirer ses fichiers, inspecter, valider, préparer une vue de contexte | Lancer agents/outils de projet, classifier le risque, approuver, exécuter les tâches |
| Profils documentés Codex/Pi/DSH | Chargement et limites testés ; recette de revue selon capacités | Branches de logique métier ou settings globaux propres à chaque harness |
| Outillage de fabrication et corpus d'évaluation | Assembler, vérifier séparation, qualifier les promesses | Être distribué ou chargé chez les consommateurs |

Le skill reste utilisable sans utilitaire. L'utilitaire ne devient nécessaire que pour les vérifications et opérations demandées ; aucun appel automatique avant chaque tool call. La version documentaire L1 peut être abandonnée ou simplifiée si elle n'améliore pas le baseline natif.

## 3. Autorité, adoption et autonomie

L'installation rend VBB **disponible**. L'invocation explicite l'applique à une mission ; elle n'est pas une autorisation de modifier une configuration, publier, déployer ou élargir la mission. La demande utilisateur ordinaire reste la source du mandat.

Pour rendre ce défaut explicite concret, la release prévoit les métadonnées natives : `disable-model-invocation: true` et `user-invocable: true` pour Pi/DSH ; `policy.allow_implicit_invocation: false` dans le compagnon `agents/openai.yaml` pour Codex. Ces possibilités ont été vérifiées dans les sources des trois profils ; elles seront testées dans L3. Le contenu de conduite reste unique. Une invocation manuelle dans une session de reprise charge la mémoire existante et ne redemande pas d'approuver un mandat encore valide. Un client qui ignore ces contrôles n'est pas qualifié pour la non-activation implicite sur cette version.

Une adoption permanente dans un projet peut ensuite être déclarée par son responsable via un lien minimal dans ses instructions existantes. Cette option est additive, visible et réversible ; elle n'est pas le comportement automatique de l'installateur MVP. Il n'existe pas de classifier global qui décide que VBB doit prendre le contrôle parce qu'un mot figure dans la demande.

L'agent commence par utiliser ce qui a déjà été autorisé. Il ne redemande ni le mandat, ni une décision retrouvée et toujours applicable. Les limites effectives du harness/organisation restent applicables. Un framework externe fournit une méthode dans le périmètre choisi ; son installation ne lui donne pas le pouvoir de changer l'intention projet.

Exécution conceptuelle : cadrer ce qui manque réellement → travailler et vérifier avec les outils du projet → corriger dans les limites accordées → remettre résultat ou blocage précis. Ces activités peuvent se répéter ou se recouvrir ; aucune machine à sept phases. Une panne se traite localement quand possible ; une tentative supplémentaire doit avoir un motif et respecter le budget accordé. Budget absent : pas de quota caché universel ; s'appuyer sur les limites natives et signaler une boucle sans progrès.

L'interruption est qualifiée en décision, intervention, information ou notification. Seule l'action dépendante est suspendue ; le travail indépendant peut continuer. Un résultat non prouvé reste non prouvé, même si l'environnement est la cause. Une autorisation révoquée invalide les délégations dépendantes ; le coordinateur utilise les outils natifs pour notifier/arrêter les agents. VBB ne garantit pas l'annulation d'un effet déjà en vol.

## 4. Contrats et espace projet

Les noms suivants sont **prévus**, aucun de ces fichiers produit n'est créé par cette planification.

```text
projet-consommateur/
  .agents/skills/vbb-work/       contenu distribué géré ; aucune donnée métier
  .vbb/
    install.json                inventaire des seuls fichiers gérés par VBB
    project.json                index de références et conventions, propriété projet
    missions/<id>/
      mission.json              état courant et mandat référencé, propriété projet
      returns/<return-id>.json  contribution immuable d'un agent, propriété projet
    decisions/<id>.md           seulement si aucune source de décision adaptée n'existe
```

Les specs, tests, ADR et résultats d'outils gardent leurs emplacements projet. Leurs chemins et révisions sont référencés, pas copiés dans `.vbb`. Aucun `active-mission` global qui supposerait une seule mission pour tout le repo. Sélection explicite par identifiant ; en cas d'ambiguïté l'utilitaire liste sans choisir. Une petite tâche achevée dans une session peut n'avoir aucun fichier mission : le résultat dans la conversation suffit si aucune reprise, délégation ou preuve durable n'est nécessaire.

Les contrats détaillés, autorité canon/legacy et chargement sont décrits dans [memory.md](memory.md). Les schémas refusent les versions majeures inconnues et les références contradictoires plutôt que d'inventer une migration.

## 5. Interfaces de l'utilitaire

CLI proposée, bibliothèque interne pure pour validation et rendu ; aucune API serveur.

| Commande prévue | Entrée / sortie | Effets permis |
|---|---|---|
| `vbb install --project PATH --dry-run` | Manifest de release ; plan exact de fichiers | Aucun en dry-run ; avec application explicite, copie exclusivement les fichiers déclarés et écrit `install.json` |
| `vbb inspect --project PATH` | État présent, versions, modifications, doublons connus, observabilité native | Lecture seule ; `unknown` pour chargé/appliqué si pas de preuve native |
| `vbb validate --project PATH [--mission ID]` | Schémas, liens locaux, empreintes, revisions/retours, conflits d'autorité déclarée | Lecture seule ; pas de commandes citées dans les preuves exécutées |
| `vbb context --project PATH --mission ID --role ROLE` | Vue limitée, références obligatoires, dépendances et éléments omis | Lecture seule, sortie texte ou JSON ; aucune collecte récursive d'historique |
| `vbb uninstall --project PATH --dry-run` | Plan de retrait selon inventaire et hashes courants | Retire uniquement contenu géré inchangé ; conserve données projet et fichiers divergents, signale les résidus |

Sorties JSON versionnées pour automatisation et texte concis pour humain. Codes prévus : 0 opération/validation réussie ; 2 entrée invalide ; 3 conflit ou dérive empêchant l'opération demandée ; 4 donnée/preuve indispensable indisponible ; 1 erreur interne. Ce ne sont pas des verdicts de qualité métier. `inspect` peut réussir techniquement en décrivant un état `unknown` ; `validate` ne convertit pas ce manque en PASS d'une affirmation qui en dépend.

La mise à jour est une nouvelle installation comparant version gérée, hashes existants et contenu cible ; pas de sixième moteur d'upgrade. Les options précises seront fixées dans L2 avant écriture, dans les limites de cette interface.

## 6. Installation et fabrication

Installations locales seulement au MVP. Aucune mutation de `$HOME`, confiance, permissions, hooks Git, prompt global ou environnement de lancement. Le répertoire skill choisi doit être un enfant direct de `.agents/skills`, compatible avec la découverte DSH documentée. Noms en conflit : échec explicite, aucun écrasement.

L'installateur possède le contenu distribué et son manifest. Il ne possède pas les décisions, missions et preuves créées pendant l'utilisation. Le retrait conserve ces données utiles même si VBB disparaît. Les scripts/commandes externes présents dans une source ne sont jamais exécutés par inspection ou validation.

Plan de mutation calculé puis vérifié au moment d'appliquer. Refuser traversée de chemin et destination symlink ambiguë ; n'accepter que chemins relatifs internes à la racine déclarée. Écrire par fichiers temporaires et remplacement local atomique ; conserver un journal **d'installation** permettant de reconnaître une opération partielle. Ce journal limité au packaging n'est pas un ledger d'actions agentiques. Lors d'un échec, retrait/réparation ne touche que les fichiers encore attribuables. Aucun restore aveugle d'un ancien fichier utilisateur.

Usine prévue : `product/` pour les seules sources distribuables, `tooling/` pour assemblage/tests et `.backbone-dev/` pour décisions/recherche. `dist/` est généré par liste explicite de fichiers de `product/`, jamais par copie globale du repo. Les références externes et rapports V1 ne sont pas dans cette liste. Pas d'AGENTS produit à la racine mainteneur ; autoapplication uniquement dans un projet de test séparé.

Le produit n'est pas forké par harness : même sémantique et contenu, petites recettes/projections natives seulement si un besoin est testé. Première distribution : archive versionnée avec empreintes, installable localement sans marketplace. Plugins natifs publiés seulement si leurs gestionnaires simplifient effectivement le retrait ; hors MVP.

Amorçage de l'utilitaire : l'archive extrait un point d'entrée Python utilisable depuis son chemin, avec dépendances dans un environnement virtuel explicitement choisi, sans ajout automatique au PATH. L'installation projet possède les fichiers qu'elle copie, pas le répertoire d'extraction choisi par l'utilisateur. Ce dernier est documenté comme distribution téléchargée, supprimable séparément. L'installation du skill peut être faite sans utilitaire ; le mode manuel doit conserver le même inventaire si le retrait automatisé est souhaité. Aucun téléchargement dynamique de dépendances au premier appel de `inspect` ou `context`.

## 7. Spécialistes et qualification

Spec Kit : ses artefacts restent source de spécification/convergence lorsqu'il est choisi. Impeccable : son contexte design reste la référence visuelle choisie. Playwright, sécurité et recherche : outils et méthodes spécialisés. VBB conserve les liens, critères et limites ; il ne recopie ni leurs workflows, ni leurs règles, ni leurs résultats complets.

Un spécialiste absent ne se déclenche pas par auto-installation. Si une capacité déjà présente suffit, l'agent l'utilise. Sinon il produit le diagnostic du manque ou adapte le contrôle dans le mandat. Le toolkit SAST étudié nécessite une frontière isolée ; ne pas retirer AGENTS.md d'un projet consommateur pour lui laisser la place.

L'agent choisit des preuves selon le dommage plausible, la réversibilité et les contrats touchés. Aucun score ou niveau historique obligatoire. Les critères d'acceptation ne sont pas affaiblis pour obtenir PASS. Un test doit parfois être modifié légitimement : conserver alors pourquoi son ancien oracle était faux et vérifier l'exigence réelle.

Revue fraîche ciblée pour questions à impact élevé ou mal couvertes par tests ; facultative pour trivial. Le reviewer reçoit exigences, état à juger, preuves et moyens d'inspection, pas la défense de l'auteur. Sur Pi sans capacité déléguée adéquate, une session neuve déjà disponible ou un humain peut assurer cette revue. S'il manque une revue requise, la limite est explicite ; pas de certification autoattribuée.

## 8. Bornes à qualifier

Pas d'enforcement métier : l'utilitaire peut refuser ses propres opérations invalides, pas empêcher un agent d'éditer directement un fichier. Pas de cohérence distribuée : Git et la discipline d'intégration du projet gèrent les échanges ; une modification simultanée de la même mission demande réconciliation. Pas de garantie absolue d'invalidation : elle couvre les dépendances déclarées, pas toutes les influences possibles d'un repo.

Ces bornes sont cohérentes avec D01. Si elles deviennent insuffisantes, revenir à une question d'architecture explicite avant d'ajouter une base, des hooks permanents ou un runtime.
