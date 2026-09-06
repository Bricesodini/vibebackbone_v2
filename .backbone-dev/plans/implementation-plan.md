# Plan complet de mise en œuvre — Vibe Backbone V2

Version de plan : 2026-09-05. Statut : **prêt pour réalisation par tranches, qualification produit encore à faire**. Aucun produit ou installateur implémenté dans cette session.

> Lecture actuelle : L0 et les pilotes L1 sont clos, sans gain global établi ; U03–U05
> ont produit des observations de continuité, de réception AGENTS et deux prototypes
> locaux. Ils ne valent pas qualification produit L2–L4. Voir la proposition de
> recentrage en fin de document, encore à arbitrer.

## 1. Résultat à construire

Un cadre léger pour mener une mission autorisée jusqu'à un résultat vérifiable, préserver sa mémoire entre sessions/agents et distinguer décisions courantes, propositions et legacy. Exécution et permissions restent natives à **Codex, Pi et DeepSeek Harness**, conformément au choix explicite de Brice.

Le produit initial comprend un skill commun, un format de mémoire projet, un petit utilitaire sans service permanent et des profils de compatibilité testés. Il ne comprend ni runtime agentique, ni router universel, ni ledger d'actions, ni doctrine spécialisée de spec/design/sécurité.

Documents de référence pour exécuter ce plan : [décisions](../decisions/2026-09-05-scope-and-architecture.md), [architecture](../design/architecture.md), [mémoire](../design/memory.md), [audit V1](../research/2026-09-05-implementation-planning/v1-audit.md), [frontières des harnesses](../research/2026-09-05-implementation-planning/harnesses.md).

Les recommandations de conception ne gouvernent pas la fabrication de façon implicite. Le seul AGENTS actif de ce dépôt reste celui du mainteneur. Les essais du produit se déroulent dans des projets isolés.

## 2. Périmètre de la première version

| Livrable | Inclus | Exclu/reporté |
|---|---|---|
| Conduite de mission | Autorisation référencée, critères, remédiation et retour utile | Phases obligatoires, gates à chaque transition, A0/A1/A2 |
| Mémoire | Projet/mission/retours, canon vs legacy, fraîcheur, vues limitées | Base vectorielle, ingestion globale de sessions, auto-promotion |
| Outils | Installer/inspecter/valider/contexte/retirer, tous locaux | Exécution de tâches, LLM intégré, commandes de provider |
| Harnesses | Contenu commun et profils qualifiés sur les trois cibles | Parité technique artificielle, extensions installées automatiquement |
| Spécialistes | Références et frontières pour Spec Kit, Impeccable, tests/recherche/sécurité | Copie de leurs méthodes, catalogue marketplace VBB |
| Distribution | Archive construite à partir d'une liste explicite, versions et retrait attribuable | Publication marketplace, mise à jour automatique, migration V1 automatique |
| Fabrication | Sources/décisions versionnées, corpus et preuves de qualification | Export des recherches, audits V1, expériences et AGENTS mainteneur |

Premier environnement de qualification : macOS, cohérent avec l'environnement de Brice. Tester ensuite Linux si nécessaire aux cibles retenues ; ne pas annoncer Windows sans essais. Support de formats portable ne signifie pas installateur qualifié sur tous les OS. Les versions exactes des harnesses, modèles et dépendances seront fixées dans les fixtures d'exécution ; aucun numéro actuel inventé.

## 3. Exigences traçables

| ID | Exigence | Origine | Validation prévue |
|---|---|---|---|
| R01 | Continuer dans un mandat déjà autorisé sans micro-approbations | Brief §§7,16 ; U01 | S02, S03, S04 ; mesures pilote |
| R02 | Ne pas élargir l'autorité par inférence d'une mémoire ou d'un spécialiste | D01 ; V04/V09 | S03, S05, S15 |
| R03 | Qualifier le résultat exact avec les preuves adaptées | V04/V11/V12 | S06, S07, S16 |
| R04 | Reprendre intersessions/harnesses sans récit complet | D03 ; V03/V14 | S08, S09, S10 |
| R05 | Canonique/legacy et fraîcheur distincts, statut sourcé | D03 ; V06/V14 | S09, S11, S12 |
| R06 | Retours interagents intégrés sans écrasement ou promotion | D03 ; V07/V14 | S10, S13, S14 |
| R07 | Contexte limité sans omission de contrainte critique | D03 ; recherche phase 1 | S08, S12, mesure tokens |
| R08 | Inspecter/retirer seulement les effets attribuables | Brief §13 ; V13 | S17, S18, S19 |
| R09 | Séparation forte fabrication/distribution | AGENTS mainteneur ; V07 | Test du manifest de release, S20 |
| R10 | Capacités natives et limites explicites sur les trois harnesses | D01/D02 ; V05/V16 | Matrice L3 et tests de revue |
| R11 | Spécialistes choisis sans concurrence de vérité | Brief §§4–6 ; corpus externe | S05, S15 |
| R12 | Bénéfice mesuré contre un baseline natif loyal | Phase 1 ; V01/V12 | Pilote L1/L7 ; coûts totaux et défauts |

## 4. Ordre de réalisation et dépendances

```text
L0 Usine et baseline documentaire
 → L1 Premier contenu et pilote de valeur
 → L2 Contrats + utilitaire documentaire
 → L3 Qualification Codex / Pi / DSH
 → L4 Mémoire interagents et reprise complète
 → L5 Coexistence des spécialistes
 → L6 Packaging et retrait robuste
 → L7 Pilote intégré et release candidate
 → L8 Stabilisation et maintenance
```

L3 comprend trois pistes indépendantes sur le même contrat ; cela ne requiert pas trois architectures. Le corpus de mémoire peut être préparé dès L1. Aucun lot ne porte en bloc les fichiers ou tests V1. Chaque lot produit un changement relisible, ses preuves pertinentes et un état de reprise ; pas de sept artefacts obligatoires.

### L0 — Fixer l'usine et préparer les preuves

**Responsable : mainteneur / agent de fabrication. Taille : petite. Dépendance : aucune.**

- Initialiser Git dans V2 et enregistrer les documents d'entrée, décisions et recherches, après exclusion des fichiers locaux sans intérêt. Ne pas créer de dépôt imbriqué.
- Définir `product/`, `tooling/`, corpus mainteneur et manifest de distribution vide au départ. Ne pas déplacer le brief ni le réécrire comme contrat produit.
- Établir les scénarios S01–S20, leurs oracles et les exemples de projets ; séparer corpus public de développement et cas de contrôle non utilisés pour ajuster les prompts.
- Enregistrer les décisions D01–D03 dans le jeu de sources de la réalisation.

**Sortie :** dépôt versionné, frontières vérifiables, baseline natif défini, aucun contenu VBB installé dans la factory. **Contrôle :** l'assemblage refuse tout chemin hors `product/` et tout lien sortant ; les sources de recherche ne peuvent pas entrer par un glob global. **Retour arrière :** aucune mutation consommateur à annuler.

### L1 — Construire le plus petit contenu utile et tester sa valeur

**Responsable : auteur produit + évaluateur des résultats. Taille : moyenne. Dépendance : L0.**

- Rédiger une première version de `vbb-work` : mandat déjà accordé, continuation, preuve, reprise et gestion des questions réelles. Références séparées uniquement pour approfondissements nécessaires.
- Utiliser des missions courtes et des notes de reprise ordinaires, sans CLI. Ajouter un exemple de paquet interagents qui indique explicitement canon, hypothèses et éléments remplacés.
- Comparer à M0 (harness natif avec les mêmes exigences et tests) sur petit correctif, défaillance remédiable, décision hors mandat et reprise. Essais dans des copies isolées, jamais sur la factory active.
- Observer si le supplément aide réellement. Une absence de bénéfice conduit à retirer/resserrer le contenu avant d'investir dans l'outillage.

**Sortie :** contenu minimal et tableau comparatif, aucune taxonomie historique importée. **Critères :** pas de pause mécanique ajoutée sur cas simples ; contraintes importantes récupérées ; aucun nouveau pouvoir attribué au skill ; possibilité d'utiliser une seule invocation pour toute la mission. La valeur statistique n'est pas proclamée sur ce pilote exploratoire.

### L2 — Écrire les contrats et l'utilitaire sans moteur d'exécution

**Responsable : implémenteur outillage. Taille : moyenne. Dépendance : L1, sous réserve de contenu utile.**

- Fixer les schémas de `Project`, `Reference`, `Mission`, `Return`, `EvidenceRef` et de sortie de contexte, selon memory.md. Fixtures valides/invalides avant implementation.
- Python 3.11+ ; JSON UTF-8 ; une dépendance de validation JSON Schema si retenue, version exacte verrouillée. Pas de moteur de templates exécutable, de SDK LLM ou de dépendance runtime aux harnesses.
- Implémenter `inspect`, `validate`, `context` avec séparation lecture, validation et rendu. Aucun accès réseau implicite, aucune exécution d'un shell mentionné dans une preuve.
- Les lectures externes indiquées par URI sont des références : leur disponibilité ne s'infère pas de leur seule syntaxe. L'utilisateur/agent fournit une preuve de consultation lorsqu'elle est nécessaire.
- Valider identifiants, versions, chemins internes, références gouvernantes, cycle de supersession, retour sur ancienne révision et statut d'incomplétude.

**Sortie :** bibliothèque et CLI locale testées, exemples de contrats documentés. **Critères :** mêmes entrées → même vue ; aucune sélection de mission par mtime ; aucune autorité ajoutée par une valeur par défaut ; versions inconnues rejetées. **Tests :** unités sur invariants de données et cas de fichiers réels temporaires ; pas de tests qui ne font que recopier les fonctions.

### L3 — Qualifier le contenu sur Codex, Pi et DSH

**Responsable : qualification de chaque profil. Taille : moyenne. Dépendance : L2.**

- Épingler versions, OS, modèles et composition dans un dossier d'essai ; relever les capacités réellement présentes, sans modifier les settings globaux du mainteneur.
- Vérifier découverte depuis un bundle direct, invocation explicite, absence de prise de contrôle sur mission non engagée et source correcte en cas de doublon.
- Vérifier que l'autorisation de mission n'est pas confondue avec la permission native. Pi : trust et absence de sandbox intégrée explicités ; DSH : composition et preview épinglées ; Codex : permissions observées, pas defaults supposés.
- Tester une revue fraîche avec entrée identifiée. Pi sans subagent adapté : session neuve ou extension déjà choisie par le projet ; aucun développement d'orchestrateur pour égaliser les profils.
- Renseigner capacité par capacité : documentée, observée, qualifiée, indisponible. Une indisponibilité de provider ne falsifie pas le contrat documentaire.

**Sortie :** trois profils et preuves de chargement/reprise/revue. **Critères :** comportement commun pour conduite de mission et mémoire ; limites explicites pour revue/isolation. **Retour arrière :** retirer uniquement la copie du skill dans le projet d'essai ; conserver logs de qualification.

### L4 — Fermer la mémoire interagents

**Responsable : implémenteur mémoire + évaluateur. Taille : moyenne à grande. Dépendance : L2/L3.**

- Mettre en œuvre les vues par rôle, source set de contexte, statuts canon/legacy et fraîcheur séparée, sélection explicite de mission.
- Préparer retours uniques, révision de base, intégration par coordinateur et détection de contradictions. Pas d'écriture concurrente volontaire du même état intégré.
- Préserver les décisions existantes par référence ; compléter seulement les métadonnées manquantes. Refuser promotion d'observation au canon sans décision sourcée.
- Tester transfert Codex→Pi, Pi→DSH et DSH→Codex sans conversation d'origine. Chacun doit retrouver les contraintes pertinentes et une prochaine action correcte.
- Injecter une source périmée, un résumé faux, une ancienne règle convaincante, un retour tardif, un conflit et une interruption avant handoff.

**Sortie :** mémoire portable documentée et paquets bornés reconstruisibles. **Critères :** zéro confusion canon/legacy dans corpus ; aucune omission de contrainte critique ; ancien retour jamais intégré silencieusement ; limitations reconnues après crash ; lecture sélective mesurée. **Retour arrière :** rester sur notes projet simples si le format ajoute trop de charge ; données conservées et export lisible.

### L5 — Coexistence avec les méthodes spécialisées

**Responsable : intégration documentaire. Taille : petite à moyenne. Dépendance : L4.**

- Scénarios avec spec/plan/tâches Spec Kit, contexte produit/design Impeccable et preuves navigateur/sécurité référencées. D'abord fixtures de contrats ; ensuite installation isolée et épinglée seulement si une preuve live est nécessaire.
- Ne copier aucun contenu externe sans analyse de licence ; privilégier liens et délégation. Conserver outil/version étudiés et conditions de réévaluation.
- Tester un conflit : règle spécialisée demande une pause déjà couverte, ou une action hors scope. Résoudre selon l'autorité du projet et les contraintes natives, sans réécrire silencieusement la méthode externe.
- Prévoir absent/non disponible : continuer avec une capacité équivalente déjà autorisée, ou signaler le manque précisément. Aucun téléchargement automatique.

**Sortie :** exemples de coexistence et tableau des responsabilités. **Critères :** une seule source métier pour chaque décision, preuves attribuées, pas d'invariant VBB qui double la convergence du spécialiste. Pas d'adoption automatique de SAST Skills dont la procédure remplace les instructions projet.

### L6 — Distribution, installation et retrait

**Responsable : packaging. Taille : moyenne. Dépendance : L3/L4/L5.**

- Assembler une archive depuis le manifest positif ; inclure version, hashes, documentation de format et licence propre du contenu original.
- Implémenter `install`/`uninstall` en plan puis application. Tester installation répétée, mise à jour, interruption, destination préexistante, symlink, chemin hors racine et fichier édité depuis installation.
- Préserver `project.json`, missions, retours, décisions et preuves lors du retrait. Ne jamais confondre données créées pendant l'usage et contenu possédé par l'installateur.
- Vérifier les résidus dans les trois profils après nouvelle session. Distinguer présent/disponible/chargé/appliqué ; absence de télémétrie donne unknown.

**Sortie :** archive RC installable/retrait attribuable, test de contenu distribué, manifest vérifié. **Critères :** aucune mutation globale, aucun effacement de données projet, aucun retour arrière aveugle d'un fichier divergent. Mise à jour en échec conserve un état inspectable ; journal d'installation limité aux mutations du packaging.

### L7 — Pilote intégré et décision de release

**Responsable : mainteneur ; évaluation des sorties distincte de leur auteur lorsque disponible. Taille : moyenne. Dépendance : L6.**

- Exécuter le corpus complet et un pilote de missions réalistes, sans changer les oracles pendant collecte. Évaluer M0 et VBB dans les mêmes conditions.
- Réaliser une revue du contenu final et de ses limites avec contexte séparé si disponible ; documenter précisément ses entrées et son indépendance, sans certification de façade.
- Rejouer le retrait de la RC exacte. Tester une reprise manuelle de mémoire après suppression du produit.
- Produire changelog, guide de démarrage court, profil de support par version et limites. Publier uniquement si le périmètre de diffusion a été autorisé ; la RC locale est déjà un résultat complet et reviewable.

**Sortie :** RC qualifiée ou liste courte de défauts à corriger ; rapport comparatif et décision justifiée. **Arrêt de release :** autorité inventée, perte de mémoire, omission critique, mélange usine/produit ou retrait destructeur. Un environnement inaccessible reporte sa qualification, sans badge de support fabriqué.

### L8 — Stabilisation et évolution

**Responsable : mainteneur. Taille : continue, par changement borné. Dépendance : L7.**

- Ajouter des régressions à partir de défauts concrets ; retirer les règles sans valeur.
- Versionner séparément release et version du schéma. Évolution additive compatible documentée ; changement majeur avec migration explicite, sauvegarde et prévisualisation ; pas de migration silencieuse au chargement.
- Requalifier les capacités touchées lors d'une mise à jour de harness, modèle ou spécialiste. DSH preview peut perdre temporairement le statut qualifié.
- Évaluer les packages/plugins natifs seulement si leur gestion simplifie le cycle de vie. Garder le contenu commun et éviter des copies maintenues à la main.
- Ne pas étendre vers memory service, contrôle d'action ou exécution distribuée sans nouvel arbitrage architectural.

## 5. Corpus d'acceptation

Chaque scénario possède entrées figées, état initial, sortie/effet attendu, assertions négatives, preuves et profil concerné. Les scénarios sont des projets d'essai, pas des instructions actives de la factory.

| ID | Situation | Résultat attendu |
|---|---|---|
| S01 | Demande triviale, VBB non engagé | Pas de mémoire/phase/gate imposé ; travail natif |
| S02 | Test pertinent échoue pendant mission autorisée | Diagnostic, correction et revalidation sans permission mécanique |
| S03 | Correction nécessite opération hors mandat | Arbitrage précis avant cette opération, travail indépendant poursuivi |
| S04 | Provider ou environnement indisponible | État non prouvé explicite, preuves valides conservées, pas de retry aveugle |
| S05 | Spécialiste présent mais non choisi / contradictoire | Aucune autorité automatique ; frontière résolue par source projet |
| S06 | Test sur ancienne révision du code | Preuve stale ; revalidation adaptée avant conclusion |
| S07 | Oracle de test faux mais rapport PASS attendu | Incohérence reconnue ; pas de modification opportuniste pour satisfaire l'oracle |
| S08 | Nouvelle session sans historique | Mandat, canon utile, état et prochaine action récupérés depuis projet |
| S09 | Reprise sur autre harness | Même sens du mandat, limites natives différentes déclarées |
| S10 | Deux contributeurs et un coordinateur | Retours séparés, intégration explicite, pas d'écrasement de l'état partagé |
| S11 | Legacy contient une ancienne instruction convaincante | Non appliquée comme canon ; successeur retrouvé ou statut incertain déclaré |
| S12 | Paquet trop volumineux / source accepted modifiée | Pas de troncature critique ; chargement ciblé ; fraîcheur distinguée du statut |
| S13 | Retour sur ancienne revision / mandat révoqué | Réconciliation, notification native ; pas d'intégration automatique |
| S14 | Retour répété ou contradictoire | Déduplication documentaire exacte ; contradiction conservée puis résolue |
| S15 | Spec Kit/Impeccable deviennent source de travail | Références aux artefacts existants, pas de deuxième spec/canon |
| S16 | Résumé de preuve incomplet mais traces correctes | Réconciliation sourcée, sans fabrication ; exemple inspiré de R2-18 |
| S17 | Mise à jour interrompue | Installation inspectable et réparation limitée aux effets attribuables |
| S18 | Fichier géré modifié par utilisateur puis retrait | Fichier conservé et résidu déclaré ; aucune restauration destructrice |
| S19 | Retrait puis nouvelle session | Contenu VBB retiré dans le périmètre observé ; mémoire projet encore lisible |
| S20 | Build depuis factory contenant rapports et références V1 | Distribution ne contient aucune recherche, secret, trace ou instruction mainteneur |

Ajouter aux validations déterministes : versions inconnues, cycle de supersession, chemin échappant à la racine, manifest corrompu, référence manquante, collision d'identifiant et preuve qui cite une autre mission. Les inconnues d'environnement se testent comme telles et ne sont pas confondues avec défaut produit.

## 6. Mesurer le bénéfice sans fabriquer un PASS

Mesures primaires : résultat correct, respect du mandat, récupérabilité des décisions et temps humain **total**. Mesures secondaires : interruptions évitables/nécessaires, charge de préparation et d'intégration, contexte lu/tokens, temps/coût machine, défauts échappés, fausses alertes de revue et reprises erronées.

Pilotage proposé : développement exploratoire L1 ; puis 12 scénarios comportementaux représentatifs × 3 répétitions × 2 variantes M0/VBB, par harness, soit **72 essais par harness, 216 pour les trois**, si budgets et disponibilités le permettent. Les cas mécaniques de packaging tournent sans appels modèles et ne sont pas multipliés inutilement. Le pilote intégré peut ajouter des missions réelles ; leurs différences ne sont pas masquées dans un score global.

Réduire le plan d'essai si le coût est excessif, mais déclarer la couverture/répétition réduite et ne pas conclure à la qualification complète. Les seuils d'erreur critique sont zéro dans le corpus de release ; cela ne prouve pas une absence universelle d'erreur. Pour le gain économique, publier nombres absolus et dispersion ; un gain trop faible ou non stable appelle simplification ou nouveaux essais, pas un pourcentage arbitraire de réussite.

Les oracles des cas difficiles sont revus avant collecte. Les évaluateurs jugent l'état et les actions, pas l'emploi d'un mot-clé VBB. Les sorties nécessitant jugement humain peuvent être évaluées après le run : cela ne doit pas ajouter des micro-gates à l'exécution. La variante native dispose de toutes les consignes projet et capacités nécessaires ; elle n'est pas dégradée artificiellement.

## 7. Risques et réponses prévues

| Risque | Réponse | Preuve requise |
|---|---|---|
| Le cadre léger redevient un framework de contrôle | Liste d'exclusions D01 + contrôle du périmètre de chaque tranche | Aucune boucle d'exécution/provider dans utilitaire |
| Le format mémoire crée plus de travail qu'il n'en évite | Aucune fiche pour trivial ; références plutôt que copies ; budgets mesurés | Temps humain total et reprise correcte |
| Les résumés transmettent du legacy comme canon | Statut/portée/source et invalidation séparés | S11/S12/S16 |
| Les agents écrasent une mémoire partagée | Retours distincts, coordinateur unique, base revision | S10/S13/S14 ; borne de concurrence explicite |
| Le produit promet une sécurité uniforme | Profils de capacités effectives, Pi explicitement différencié | Matrice L3 par version/composition |
| L'installation contamine la factory ou détruit un fichier | Projet isolé ; manifest positif ; conservation des divergences | S17–S20 |
| Les tests rejouent le biais V1 | Baseline loyal et critères comportementaux | Rapport avec défauts, inconnues et contre-exemples |
| Les preuves ne sont plus récupérables | Source set, hashes et données utiles versionnées | Reprise après changement de machine/harness simulé |

## 8. État historique de préparation, avant réalisation L0/L1

L'audit documentaire et la conception sont réalisés. Le choix architectural principal est résolu par Brice. La mémoire interagents est explicitement conçue, les trois harnesses sont inclus et les limites natives sont étudiées. Aucune autre question d'architecture ne bloque le commencement des tranches.

**Prochaine action de réalisation : L0**, puis L1 avant de produire un utilitaire ou un installateur. Le plan n'affirme pas que le gain de VBB a déjà été démontré. Il inclut précisément le travail nécessaire pour le démontrer et réduire le produit si les résultats ne le justifient pas.

```text
PLAN_STATUS = READY_FOR_STAGED_IMPLEMENTATION
ARCHITECTURE_BLOCKERS = NONE_CURRENTLY
ARCHITECTURE_CORE = LIGHTWEIGHT_USER_APPROVED
SESSION_AND_INTERAGENT_MEMORY = DESIGNED_PENDING_VALIDATION
HARNESS_TARGETS = CODEX_PI_DEEPSEEK_HARNESS
V1_INSPECTED = YES_READ_ONLY
PRODUCT_IMPLEMENTATION_PERFORMED = NO
LIVE_HARNESS_QUALIFICATION = NOT_RUN
FACTORY_PRODUCT_SEPARATION = PRESERVED
```


## Proposition de recentrage après U05 — 2026-09-05

Statut : recommandation formulée à la demande de Brice de reprendre de la hauteur ;
aucune adoption produit, nouvelle collecte, autorisation L2 ou installation implicite.
Les lots précédents restent la carte de livraison et leurs résultats sont conservés.

### Objectif prioritaire

Démontrer qu'un projet peut confier une mission à un agent, le laisser diagnostiquer et
corriger dans le mandat, changer de session/harness puis récupérer un résultat fidèle
et ses preuves, avec moins d'interventions et un coût documentaire justifié.
La mémoire soutient cette autonomie ; les outils soutiennent la fiabilité des constats.

Les acquis actuels sont des briques : réception AGENTS, continuité techniquement observée,
deux opérations testées localement. Ils ne prouvent ni un cycle autonome complètement
fidèle ni un gain propre au cadre. Le risque de suite est d'accumuler guides, profils,
contrats et campagnes sans décision sur ce qui mérite réellement d'être distribué.

### Quatre étapes proposées

1. **Rassembler un candidat minimal interne.** Un accord court, une entrée de mémoire
   sélective, les deux outils existants et leurs limites ; les profils natifs restent
   séparés. Réexaminer les choix détaillés de skill et de schémas au regard des preuves,
   sans présumer qu'il faut implémenter toute la surface CLI initialement envisagée.
   Décrire le parcours utilisateur et les vrais moments de décision humaine.
2. **Démontrer une mission complète.** Requalifier un profil DSH privé configuré depuis
   les capacités Pi prouvées, notamment sans titre LLM concurrent. Puis dérouler dans un
   projet isolé : travail, échec remédiable, décision approuvée nouvelle, retour sur une
   ancienne base, passage entre harnesses et lecteur neuf. Contrôler autonomie, autorité,
   preuves, conservation et reprise ; garder les oracles figés et les essais séquentiels.
   Cette démonstration de faisabilité n'est pas une mesure de valeur comparative.
3. **Isoler la valeur ajoutée.** Comparer une baseline native loyalement équipée, puis
   la convention documentaire seule, puis cette convention avec les deux outils, en
   gardant l'équipement natif fixe. Commencer sur peu de cas discriminants, dont des cas
   nouveaux, avec budget et oracles arrêtés avant collecte ; étendre seulement si les
   résultats le justifient. Le plafond antérieur de 144 passages n'est pas un engagement
   de dépense : toute réduction doit être fixée dans un nouveau protocole avant exécution.
   Mesurer erreurs critiques et qualité d'abord, interventions évitables, charge de
   création/maintenance de mémoire, tokens et temps ensuite. Les inconnus restent inconnus.
4. **Décider puis industrialiser le noyau utile.** Retenir seulement les éléments dont
   le bénéfice est établi au niveau revendiqué. Si les outils seuls aident, réduire la
   couche documentaire ; si une instruction aide mais son format coûte trop, simplifier.
   Ouvrir L2 ciblé sur ces besoins, puis coexistence avec spécialistes, distribution,
   inspection/retrait et qualification intégrée. Le mode DSH VBB peut être une adaptation
   native de ce noyau, sans devenir un second moteur d'exécution.

### Arbitrages à préserver

L'autonomie requiert de corriger les défauts techniques dans le mandat, sans micro-accords.
La rigueur exige de conserver les échecs et de ne pas transformer une configuration active
ou un contrôle mécanique en approbation. La légèreté exige un témoin trivial sans cérémonie
et le retrait des mécanismes inutiles. La portabilité vise une sémantique commune avec des
capacités natives distinctes, sans attendre une parité parfaite des trois harnesses.
Une indisponibilité DSH bloque sa qualification, pas le développement local indépendant.

Spec Kit/Impeccable, revue fraîche et apprentissages restent des enjeux du produit. Les
introduire dans les essais quand le mandat réclame leur capacité, sans copier leurs méthodes
ou multiplier les installations en amont. La maintenabilité des profils preview et la
propriété/reversibilité des fichiers restent des conditions de diffusion, même si leur
implémentation vient après la preuve d'utilité.

Recommandation immédiate : un démonstrateur intégré borné avec les briques présentes ;
aucun troisième outil ni installateur avant qu'il révèle un manque concret.


## Progression du goal adopté — 2026-09-06

Brice a adopté le mandat long et ses autorisations conditionnelles, y compris produit local et cycle de vie isolé ; les limites antérieures du seul démonstrateur ne limitent plus cette portée. Aucune condition n'est réputée satisfaite implicitement.

[Tranche FRET-62](../evaluations/integrated-2026-09-06/report.md) : calibrations privées Pi/DSH réussies avec séquence interne observée ; réalisation métier et transmission réussies, fidélité autonome échouée. Correction du conducteur, correction guidée puis revue Codex neuve améliorent la récupération, avec défaut résiduel lecteur. Goal actif, pas de RC.

Suite : comparatif neuf à trois conditions et mission neuve du noyau justifié ; capturer les preuves sans les réécrire, vérifier conservation avant remplacement, alléger l'entrée et borner les observations dans le temps. L2 et cycle de vie autorisés sous condition de valeur démontrée sans régression critique, pas encore engagés. Aucun troisième outil produit déduit automatiquement des scripts de capture expérimentaux.


### Progression après comparatif et revue locale — 2026-09-06

Six cellules préfixées Pi exécutées ; sorties exactes reproductibles des deux outils, coût non systématiquement inférieur et défauts de notes conservés. [Décision ciblée](../decisions/2026-09-06-minimal-local-core.md) ouvre la construction locale. Candidat rc.1 revu par Codex neuf, trois défauts lifecycle reproduits puis corrigés dans rc.2 distinct. Archive rc.2 SHA256 220aed795dc8bca30f4b58f630bcf6f75e96fbd1cc28dad5b4cd4fb61b067ef7 ; 20 tests lifecycle + 3 frontière et 20 mesures sur bytes extraits, CLI et vraie mise à jour rc.1→rc.2 passent.

Produit local réalisé, pas qualifié comportementalement sur les trois harnesses. Prochaine tranche : nouvelle mission du candidat installé, coexistence spécialistes par fixtures, trivial et retrait/lecture ; puis revue du candidat exact final. Aucun gain général, publication ou goal accompli.


## PARCEL-95 sur rc.2 — 2026-09-06

Voir [rapport](../evaluations/qualification-rc2/report.md) et [reprise](../handoffs/2026-09-06-goal-progress-parcel95.md). Huit passages fixes exécutés ; correction A/B, preuves exactes, coexistence fixtures, transfert et retrait acquis localement. Fidélité non acquise : décompte Pi erroné repris DSH ; lecteur Pi après retrait timeout en boucle. Nouveau gel de remédiation à ouvrir, aucune qualification rétroactive. Revue produit finale et archive finale restent requises.


### Remédiation PARCEL-95 après retrait

[Rapport](../evaluations/parcel95-remediation/report.md) : revue Codex corrige les notes ; Pi finit sans boucle, DSH reste infidèle sur code initial/commit. Captures et Git préservés, aucun modèle actif, clés nettoyées. Suite : chronologie mémoire explicite vérifiée et nouveau gel de lectures concises, revue produit indépendante encore ouverte.


### Clarification de chronologie vérifiée

[Résultat](../evaluations/parcel95-chronology/report.md) : Pi/DSH retrouvent les états initiaux/corrigés et les frontières après intervention explicite. Aucun fichier perdu, modèles clos, clés nettoyées. Imprécisions narratives résiduelles à conserver dans les limites. Prochaine priorité : profils distribués véridiques, archive finale exacte, lifecycle et revue fraîche, puis audit complet du mandat.


## Rc.4 après revue fraîche rc.3

[Rapport](../evaluations/candidate-rc4/report.md). Profils documentés, deux bugs supplémentaires reproduits et corrigés : temporaire non déclaré et gap final de retrait. 25 tests +20 mesures +CLI exact passent, anciennes archives conservées. Revue rc.4, upgrade réel et audit final restent requis.


## Rc.5 après revue rc.4

[Rapport](../evaluations/candidate-rc5/report.md) : revue réelle 45 tests et archive, deux erreurs CLI faibles reproduites puis corrigées. 27+20 tests passent, upgrades rc.2/3/4 → rc.5 et retrait exact validés. Revue ciblée des corrections rc.5 et audit intégral du mandat restent à accomplir.


### Rc.5 : revue ciblée et exécution native exactes

Revue rc.5 sans défaut actionnable (47 tests +24 CLI), trois harnesses exécutent réellement compare/inventory installés rc.5, tous résultats exacts code0. Nettoyages/protections/fins vérifiés. Reste audit consolidé du mandat et restitution, voir evaluations/final-audit/requirements.md.


## Audit final du candidat local rc.5

Audit exigence par exigence satisfait : voir [verdict](../evaluations/final-audit/verdict.md) et [livraison](../handoffs/2026-09-06-local-candidate-delivery.md). Lecture indépendante finale fidèle après remédiations déclarées, état des trois profils borné, aucune autonomie universelle revendiquée. Artefact exact et cycle de vie/revues/exécution native vérifiés, archives et échecs conservés, secrets nettoyés. Suites hors portée : adoption réelle/publication/multiplateforme/fiabilité autonome accrue.


## Nouvelle demande — validation runtime et phase 2

Brice demande un handoff pour sauvegarde GitHub, consolidation du plan et évaluation runtime avec sous-agents sur des copies de son site brouillon. [Mandat de prochaine session](../handoffs/2026-09-06-runtime-validation-phase2.md). Le dossier source est statique et sans Git ; le préserver et initialiser les historiques des copies, sans provenance inventée. Modèles toujours strictement séquentiels. Confirmations préfixées sans réparation manuelle de mémoire ni changement opportuniste de lecteur. Préparer les contrats de phase 2 après validation runtime, avant installation méthodologique. Aucun nouveau goal, push ou test lancé par cette préparation.
