# Handoff — démonstrateur intégré Vibe Backbone V2

Préparé le 2026-09-06 à la demande de Brice après U05 et la prise de recul sur le plan d'ensemble.
Demande de cette session : préparer le lancement dans une nouvelle session, sans lancer
ici de nouvelle collecte. Le prompt en fin de document porte la mission proposée pour
cette reprise. Les choix produit finaux et L2 restent à décider à partir des preuves.

## Cap à conserver

Permettre à un agent de poursuivre et corriger une mission dans le mandat autorisé,
de changer de session/harness et de transmettre un résultat fidèle avec des preuves
récupérables, sans micro-validations humaines ni mémoire envahissante.

Nous avons des briques ; la prochaine étape utile est leur intégration dans une mission
complète. Ne pas repartir vers un catalogue d'outils, une refonte générale de DSH ou un
nouveau corpus documentaire. La valeur ajoutée de VBB reste une hypothèse à éprouver.

## Lecture minimale, dans cet ordre

1. [INDEX](../INDEX.md), puis la section « Proposition de recentrage après U05 » du
   [plan](../plans/implementation-plan.md). Le reste du plan L0–L8 est la carte historique
   de livraison, pas la liste de lots déjà qualifiés.
2. [Décisions D01–D03 et frontières](../decisions/2026-09-05-scope-and-architecture.md) :
   cadre léger, exécution/permissions/sessions natives, mémoire durable et sélective.
3. [Guide DSH](../operations/guide-dsh.md), puis seulement les sections nécessaires de
   la [stratégie Pi → DSH](../design/dsh-from-pi-reference.md).
4. [Rapport AGENTS U04](../evaluations/agents-common-v2/report.md).
5. [Prototype des deux outils](../experiments/deterministic-tools/README.md) et son
   [bilan local](../experiments/deterministic-tools/report.md).

Pour le scénario mémoire, lire ensuite le [mode opératoire](../operations/cross-harness-continuity.md)
et ses rectificatifs. Pour retrouver le sens produit, consulter les §§7,16,21,25–26 du
[brief fondateur](../../VIBE_BACKBONE_V2_BRIEF_FONDATEUR_v2.md), entrée de conception
non normative. Ne pas charger toutes les traces ou tous les rapports antérieurs.

## État transmis, sans surqualification

- L0 terminé ; L1 et L1 bis clos. Aucun gain global établi contre M0.
- U03 : création et entretien documentaires réellement observés entre les trois harnesses,
  mais défauts stricts de fidélité/protection ; aucun cycle autonome complet qualifié.
- U04 : neuf réponses conformes aux sondes AGENTS racine/sous-dossier/session neuve après
  changement ; requêtes Pi/DSH contenant l'accord exact, preuve comportementale Codex.
  Le premier gel conserve six indisponibilités de démarrage dues au conducteur.
- Le second gel U04 découvre un titre LLM DSH concurrent au modèle principal : la séquence
  des processus était respectée, celle des requêtes internes ne l'était pas. La mission
  mémoire U04 n'a donc pas tourné. Corriger le profil est une tâche technique, pas un
  motif pour rejeter DSH ou imposer une validation humaine à chaque réglage.
- U05 : `compare` et `inventory` implémentés en interne ; 20 tests locaux passent,
  exemples CLI archivés. Aucun appel modèle ni comparaison manuel/outils dans cette tranche.
- DSH est en developer preview et configurable. Brice propose de le configurer depuis
  une référence Pi fonctionnelle et envisage un [mode VBB V2 natif](../design/vbb-native-mode.md).
  Ce mode reste une option de conception, pas un produit disponible.
- Distribution vide ; aucun L2/installateur. Les homes d'essai ont été nettoyés de leurs
  copies de clés ; ne pas les considérer comme prêts à lancer.

## Travail à réaliser à la reprise

### 1. Assembler et vérifier un candidat expérimental minimal

Réutiliser les briques existantes : AGENTS court, documents ordinaires du mandat/canon,
entrée de mémoire sélective et deux opérations déterministes. Les notes de mémoire
seront produites par les exécutants, pas préparées parfaitement par l'évaluateur.

Créer un nouveau dossier interne et des projets d'essai hors factory avec racine Git
propre. Reconstituer des homes privés, épingler versions et paramètres réels. Les profils
historiques étaient Codex CLI gpt-6-astra low et Pi/DSH Qwen3.8-27B local off ; DSH ne
signifie pas modèle DeepSeek. Revalider la disponibilité sans substitution silencieuse.

Prendre Pi comme référence de capacités prouvées ; traduire explicitement vers DSH
modèle, compatibilité, effort, plafonds, retries et outillage. Inspecter la composition
native effective et les appels auxiliaires. Retirer du profil privé le provider de titre
LLM et les appels automatiques inutiles. Ne pas modifier les réglages globaux.

Tester sans modèle les commandes ET redirections réelles sous protection. Conserver les
traces natives dans le home autorisé, les archiver depuis le conducteur après fin. Protéger
sources et oracles. Le profil DSH au mode interne `danger-full-access` n'est admissible
ici que sous l'enveloppe macOS externe obligatoire, jamais seul.

Figer ensuite les sondes de capacités et leurs critères avant leurs appels modèles.
Vérifier réception, lecture/écriture/contrôle utiles et **absence de concurrence interne**,
pas seulement l'ordre des harnesses. Garder distinctes la qualification du profil et la
réussite du futur scénario métier.

### 2. Exécuter une mission nouvelle de bout en bout

Proposition de scénario à préciser et geler avant collecte :
- Codex commence un petit travail réel de fixture, rencontre un échec remédiable, le
  corrige dans le mandat et crée sa mémoire.
- Pi reprend le projet sans session précédente, reçoit une décision approuvée nouvelle,
  actualise le travail, les preuves et la mémoire en conservant les prédécesseurs.
- DSH traite un retour tardif fondé sur l'ancienne décision, utilise les outils lorsque
  pertinents, conserve les informations uniques et juge la clôture réelle.
- Un lecteur neuf reprend sans mutation ni conversation antérieure et reconstruit le
  mandat, le canon actuel, la décision remplacée, les preuves et leurs limites, le statut
  de clôture, les informations utiles et la prochaine action.

Le rôle du lecteur, le nombre de passages, les budgets et les injections doivent être
arrêtés avant lancement ; aucun quota implicite. Choisir un cas neuf plutôt que reprendre
Q-27 ou les anciens runs jusqu'à obtenir PASS. Pour montrer une clôture réussie, prévoir
des contrôles obligatoires réellement accessibles ; un contrôle indisponible, s'il est
choisi comme contre-cas, interdit seulement cette clôture et reste explicitement ouvert.

Les prompts donnent les missions, pas les marqueurs privés ou les réponses attendues.
Les oracles figent autonomie, autorité, exactitude des preuves, conservation et fidélité
au lecteur. Figer aussi sources, profils, outils, prompts, métriques et critères d'arrêt.
Ne pas adapter les oracles après résultats. Une correction légitime garde l'ancienne preuve
et produit une version distincte ; les échecs d'un gel ne sont jamais effacés.

Transmettre le projet et l'historique Git si les preuves y renvoient, sans sessions,
secrets ou caches. Le conducteur mesure la transmission ; le résultat d'un contrôle
évaluateur ne remplace pas une preuve que l'agent devait produire.

### 3. Conclure et préparer la mesure de valeur

Produire un rapport court : ce qui fonctionne réellement, défauts, indisponibilités,
interventions, coûts observables, limites et changements minimaux nécessaires.
Une démonstration réussie n'établit pas à elle seule un gain contre une pratique native.

Proposer ensuite un petit comparatif à trois conditions : pratique native loyale,
convention documentaire seule, convention plus outils, équipement natif constant.
Le [protocole déterministe préparatoire](../evaluations/deterministic-next/protocol.md)
fournit des cas et mesures ; son plafond de 144 passages n'est pas un engagement à lancer.
Préparer une version plus petite et ses oracles avant toute éventuelle collecte comparative.
Cette reprise vise d'abord le démonstrateur, pas l'exécution automatique de toute la roadmap.

## Contraintes et critères de fin

- Modèles strictement séquentiels, y compris reviewer, titre, job et appel auxiliaire.
  Attendre fin locale et trois observations serveur inactif avant le suivant. Au timeout,
  fin/annulation serveur vérifiée sinon suspension ; serveur partagé non réservé.
- Un défaut technique peut être diagnostiqué/corrigé dans le périmètre déjà accordé.
  Suspendre seulement le travail dépendant quand une condition manque ; poursuivre les
  préparations indépendantes. Pas de micro-approbations inventées.
- Aucun nouveau produit, installateur, méthode spécialisée installée, runtime agentique
  central ou auto-application VBB à la factory. Aucun troisième outil sans manque concret.
- Les collectes closes et leurs gels restent intacts. Préserver les travaux non commités.
- Fin de tranche : candidat identifié, profil/capacités prouvés ou limites explicites,
  scénario exécuté dans les conditions qualifiées ou partie dépendante non exécutée avec
  cause précise, verdict métier sourcé, nettoyage des clés et contrôle de frontière.
  Aucun besoin de conclure PASS ; aucune économie inventée depuis les seuls tests locaux.

## État du dépôt pour la nouvelle session

Le travail de cette session est sur disque dans le checkout courant, avec fichiers
modifiés et non suivis ; il n'a pas été commité par ce handoff. Reprendre dans le même
dossier `[FACTORY]` et vérifier `git status`.
Une nouvelle worktree créée depuis HEAD seul n'emporterait pas ces artefacts : préserver
ou transférer explicitement les changements avant d'utiliser une autre copie.

## Prompt de lancement à copier

> Reprends Vibe Backbone V2 depuis `.backbone-dev/INDEX.md`, puis lis
> `.backbone-dev/handoffs/2026-09-06-integrated-demonstrator.md`. Réalise la tranche du
> démonstrateur intégré : assemble les briques minimales existantes dans une expérience
> isolée, configure et qualifie DSH depuis une référence Pi fonctionnelle, puis exécute
> une mission nouvelle avec création, évolution, transmission et reprise fidèle par
> un lecteur neuf. Vérifie les capacités et tous les appels auxiliaires, puis fige
> profils, protocole, budgets et oracles avant chaque collecte. Modèles strictement
> séquentiels, indisponibilités explicites, remédiation technique autonome dans ce
> périmètre. Aucun L2, installateur ni application à la factory. Conclus sur la
> faisabilité réelle et prépare seulement le petit comparatif de valeur suivant.
