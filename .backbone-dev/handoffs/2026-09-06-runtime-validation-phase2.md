# Nouvelle session — validation runtime VBB V2 et entrée en phase 2

## Intention et statut

Handoff préparé à la demande explicite de Brice après livraison rc.5. Il demande des tests avec des sous-agents sur le brouillon de refonte de son site, puis un VBB V2 validé en usage réel et prêt pour la phase 2 : intégration ou adaptation des frameworks spécialisés et skills de développement.

Ce document prépare une nouvelle session ; il ne lance ni goal, ni sous-agent, ni campagne, ni push. Le goal précédent est clos pour un **candidat local expérimental**, pas pour la validation complète du plan initial. Les limites de fidélité de Pi/DSH restent des données de départ.

« Runtime » désigne ici le comportement effectif de VBB dans les harnesses : chargement, travail, délégation, permissions, correction, mémoire, reprise, preuves et retrait. Cela n'autorise pas à construire un runtime d'exécution VBB. Exécution, sessions et contrôle des outils restent natifs.

## Reprise minimale

1. `.backbone-dev/INDEX.md`, puis ce handoff.
2. `.backbone-dev/plans/implementation-plan.md`, surtout exigences R01–R12, lots L0–L8 et scénarios S01–S20. Le document contient des strates historiques : ne pas considérer toute la roadmap comme achevée.
3. `.backbone-dev/decisions/2026-09-06-minimal-local-core.md` et `.backbone-dev/handoffs/2026-09-06-local-candidate-delivery.md`.
4. `.backbone-dev/evaluations/final-audit/verdict.md`, les rapports PARCEL-95 référencés et les preuves ciblées nécessaires. Le verdict précédent porte sur rc.5 locale et remédiée ; il n'est pas un PASS du nouveau goal.
5. `product/README.md`, `product/agreement.md`, `product/profiles.md`, `tooling/distribution.json` et `.backbone-dev/operations/guide-dsh.md`.

Ne pas charger d'emblée toutes les traces dans le contexte des workers. Séparer protocole/oracles mainteneur et informations auxquelles le consommateur aurait accès.

## État observé à la préparation

- Factory : `[FACTORY]`.
- Remote fourni par Brice : `git@github.com:Bricesodini/vibebackbone_v2.git`, **public**. Aucun remote configuré localement au moment de cette préparation ; contenu distant/authentification non vérifiés.
- Dernier commit local observé : `7acf620`. Nombreuses modifications et fichiers non suivis, y compris travaux préexistants, produit, tests et preuves. Aucun push effectué pendant le goal précédent.
- Candidat : `.backbone-dev/releases/vbb-0.1.0-rc.5.tar.gz`, SHA256 `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`. Six fichiers distribués, 47 tests, revue ciblée et 24 contrôles CLI supplémentaires. Compatibilité des deux commandes effectivement observée sur Codex/Pi/DSH.
- Limite principale : erreurs de résumé, provenance et boucle de lecteur observées. Les meilleures reprises ont bénéficié de revue puis clarification par l'évaluateur. Pas de validation d'autonomie runtime robuste sur des projets représentatifs.
- Site autorisé comme matériau d'essai : `[PRIVATE_SITE_SOURCE]`.
- Ce dossier **n'est pas un dépôt Git**. Fichiers observés : `index.html`, `llms.txt`, `og-image.png`, `robots.txt`, `sitemap.xml`. Aucun package.json ni suite de tests trouvés. HTML/CSS/JS statiques, navigation mobile, ancres, animation et métadonnées structurées ; dépendance externe aux polices Google. Aucun diagnostic fonctionnel ou visuel encore exécuté. Les liens `href="#"` et placeholders ne sont pas automatiquement des bugs à corriger sans contrat d'essai.

## Autorisations et frontières pour la nouvelle session

La demande actuelle remplace la restriction antérieure « aucun push » pour la sauvegarde du travail VBB dans **le dépôt GitHub fourni**, après contrôle de ce qui sera public. Préparer et effectuer les commits cohérents et push ordinaires nécessaires. Vérifier remote, authentification et état distant avant mutation ; pas de force-push, réécriture de l'historique distant, suppression de travaux, écrasement d'une branche divergente ou publication marketplace/release sans besoin nouveau. Si le distant contient un historique incompatible, préserver les deux et utiliser une branche distincte ; expliquer tout véritable arbitrage restant.

L'autorisation d'utiliser le brouillon comme terrain de tests ne vaut pas autorisation de publier sa source complète, ses captures ou ses données sur le dépôt public VBB. Garder les snapshots bruts localement ; publier uniquement les éléments VBB et preuves dérivées revus, sans secrets ni contenu privé. Ne pas perdre la traçabilité : manifestes/empreintes, scripts reproductibles, inventaire des exclusions et emplacement local des preuves. Ne pas supprimer les preuves pour satisfaire un scanner ou alléger Git.

Travail autonome autorisé : inspection, copies isolées, Git dans les copies, serveurs locaux temporaires, tests navigateur, dépendances de test locales identifiées, installation/update/retrait VBB dans les copies, corrections produit/tests/conducteurs, sous-agents natifs, revues et essais de non-régression. Aucun changement global de configuration, installation VBB sur factory ou sur le dossier source du site. Aucun déploiement du site, envoi de formulaire, message externe, activation de service commercial ou modification du site en production.

Les frameworks/méthodologies spécialisés restent pour la phase 2 après décision de rôle et frontière. Un outil de test navigateur nécessaire à la qualification n'est pas une adoption méthodologique ; inspecter les capacités disponibles avant d'ajouter une dépendance. Ne pas installer Spec Kit/Impeccable ou un ensemble de skills de dev pour masquer un manque du noyau.

## Séquence d'exécution

### A — Sauvegarder et réconcilier le plan

- Revalider le checkout et les fichiers préexistants. Inventorier taille/type des traces, archives, copies Git et possibles données sensibles ; contrôle des secrets au-delà des seules valeurs connues (configurations, URLs privées, sessions, captures, identifiants).
- Configurer le remote fourni après vérification. Préparer une sélection publique explicite ; éviter `git add .` sans examen, ne pas pousser les répertoires de projets consommateurs ou sessions brutes par défaut. Les rapports de conception peuvent être versionnés dans la factory publique sans entrer dans l'archive produit.
- Produire des commits lisibles, puis pousser et vérifier le SHA distant. Si auth/réseau bloque, documenter et poursuivre la qualification indépendante ; un commit local n'est pas un push confirmé.
- Consolider un **état de référence actuel** du plan : pour chaque lot/exigence/scénario, réalisé, remplacé par décision justifiée, restant ou hors phase. Détailler les écarts concrets : pas de skill vbb-work distribué, pas de schéma mémoire imposé, pas de validate/context ni dry-run. Ne pas implémenter mécaniquement ces mécanismes sans valeur démontrée ; ne pas confondre suppression d'un mécanisme et suppression du besoin.
- Fixer une carte de couverture runtime qui relie les besoins originaux aux tests nouveaux et aux preuves existantes. Les références historiques restent disponibles.

### B — Préparer le terrain réel

- Lire les instructions applicables au site et à ses parents, examiner tous les fichiers, relever versions/outils disponibles. Faire un manifeste initial des octets du dossier source ; créer un snapshot local hors factory/publication avec permissions adaptées.
- Créer des copies d'essai indépendantes et initialiser Git **dans ces copies**. Il n'existe pas de Git source à transférer : documenter la création du premier historique, puis préserver l'historique réellement créé à chaque passage. Ne pas inventer une provenance antérieure.
- Démarrer le site sur loopback seulement ; contrôler les accès externes (polices notamment), fixer viewports et conditions pour les preuves visuelles. Arrêter serveurs/processus en fin d'essai.
- Établir un état fonctionnel initial : navigation mobile et clavier, ancres, responsive, erreurs console, liens/métadonnées pertinentes. Les outils déterministes ne remplacent pas la vérification du résultat rendu. Conserver captures/logs natifs et hashes nouveaux, sans reconstruction manuelle de « sorties brutes ».
- Choisir des tâches qui correspondent au vrai code. Candidats à préciser après inspection : navigation mobile et fermeture/focus ; évolution d'une section responsive sans perte des ancres/contenus ; cohérence d'une décision éditoriale/métadonnées et retour tardif. Ce sont des pistes, pas des défauts déjà prouvés ni une approbation de changement éditorial réel.

### C — Préfixer une campagne loyale et bornée

Avant le premier worker, écrire protocole, matrice, budgets/arrêts, missions, injections, oracles, critères de réussite et fichiers protégés. Première proposition : trois tâches représentatives × deux conditions (baseline native équipée / candidat VBB), puis deux tâches de confirmation distinctes gardées à part. Fixer le nombre exact après diagnostic, avant lancement ; ne pas dérouler un plafond historique ou une boucle jusqu'au PASS.

Équipement natif, modèle par rôle, moyens navigateur/tests, données de départ, contraintes et budget comparables. Une condition « convention seule » peut compléter une question de conception précise ; la justifier et la préfixer avant de la collecter. Les essais de confirmation ne servent pas à régler le prompt. Une modification ouvre un nouveau gel avec son motif, sans effacer l'échec ni ajouter seulement les passages favorables.

Séparer trois niveaux de preuve : résultat métier du site, comportement VBB/agent, qualité de la lecture/reprise. Tests obligatoires proportionnés au vrai travail : échec constaté puis correction ; décision nouvelle approuvée dans la fixture ; retour ancien convaincant ; fait unique hors mandat ; résumé erroné ou preuve périmée ; interruption/reprise ; retrait et lecture neuve. Identifier les décisions simulées comme telles : aucune approbation réelle de Brice inventée.

Mesurer d'abord erreurs d'autorité, omissions critiques, fidélité, conservation, interventions et terminaison. Puis temps, requêtes/tokens natifs et volumes documentaires, coûts de préparation/revue/remédiation compris ou explicitement inconnus. Publier les résultats défavorables. Une baseline ne doit pas être privée d'outils, de contexte utile ou de revue disponibles dans la condition VBB.

### D — Employer réellement des sous-agents, strictement en séquence

Brice demande explicitement leur utilisation. Distribuer des responsabilités concrètes avec contexte borné :

| Rôle | Mandat et accès | Livrable |
|---|---|---|
| Concepteur de tests / oracle | Inspection source/copie, exigences ; indépendant du worker | Protocole et assertions avant lancement |
| Worker | Copie consommateur et mandat, sans oracle privé ni historique factory | Changement réel, tests et mémoire produits pendant le travail |
| Reviewer | Copie/mandat/preuves, contexte neuf | Défauts étayés, vérifications et limites |
| Lecteur de reprise | Session neuve sans conversation d'origine | Reconstruction vérifiable du mandat/état/preuves/prochaine action |

Le coordinateur vérifie les sorties et attribue les interventions. Ne pas transmettre la réponse attendue ou une mémoire idéale au worker/lecteur. Conserver les retours par sous-agent ; un seul intégrateur écrit l'état commun. Ne pas corriger soi-même la mémoire avant de noter le résultat autonome.

**La demande de sous-agents n'annule pas la contrainte de modèles strictement séquentiels.** Pas de `Promise.all` de modèles, pas de sous-agents simultanés, titres LLM/reviewers automatiques/jobs concurrents. Lancer un rôle, attendre sa fin vérifiée, puis le suivant ; éviter les tours de raisonnement concurrents du coordinateur pendant un worker. Utiliser l'attente native, pas une boucle de polling avec de nouveaux modèles. Si un outil de sous-agent n'offre pas ce contrôle, choisir un mécanisme natif séquentiel et consigner sa limite.

Qualifier séparément la coordination de sous-agents de fabrication et les capacités du consommateur. Les sous-agents Codex ne prouvent pas la délégation Pi/DSH. Sur ces harnesses, inspecter la capacité native réelle ; une session neuve ne doit pas être présentée comme un fork/subagent. Tester les mécanismes retenus quand ils existent, afficher les absences et leur impact sans substitution silencieuse par Codex.

Réutiliser les profils privés prouvés comme point de départ, puis revalider versions/composition/permissions. Trois observations serveur inactif aux frontières, fin locale et streams internes clos. Au timeout, ne pas lancer le suivant avant fin/annulation vérifiée ; ne jamais annuler le travail d'un tiers. Serveur partagé non réservé. Homes neufs, secrets hors artefacts, nettoyage final. DSH permissif uniquement sous enveloppe externe vérifiée, jamais seul.

### E — Corriger, requalifier et conclure

Corriger les problèmes produit/configuration/tests constatés dans le mandat, conserver les reproductions. Ne pas réduire VBB aux seules commandes qui passent si le besoin de conduite/reprise n'est pas satisfait. Ne pas ajouter un moteur modèle ou une taxonomie volumineuse par réflexe.

Toute modification produit crée une nouvelle archive/version, sans écraser rc.5 ni les anciennes. Rejouer les tests touchés, le cycle de vie exact et les parcours natifs pertinents. Une correction de prompt ou de protocole n'est pas une correction produit à elle seule : distinguer leur portée. Faire une revue fraîche du candidat final.

Un manque d'auth GitHub ou de provider ne bloque que sa branche dépendante. Ne pas marquer le goal accompli avec une obligation restante ; suivre les règles natives de goal pour un blocage véritable persistant, sans attendre inutilement Brice pour les décisions réversibles déjà autorisées.

## Critères de sortie : runtime validé, entrée en phase 2

« Totalement validé » doit être un verdict sur une **matrice explicite de capacités, versions et scénarios**, jamais une promesse de comportement parfait de tout LLM. Fixer cette matrice avant les essais et ne pas la réduire après échec. Minimum requis :

1. Plan actuel consolidé et delta original documenté ; chaque besoin runtime applicable de R01–R12/S01–S20 a une preuve, ou une exclusion de portée justifiée avant collecte qui n'enlève pas une exigence utilisateur.
2. Dépôt public synchronisé avec des commits vérifiés et une sélection publique contrôlée ; tous fichiers/preuves exclus ont une conservation locale et un inventaire. Aucun brouillon privé ou secret publié par défaut.
3. Travail réel et correction sans micro-validation, sous-agents effectivement exercés selon rôles et capacités natives, contraintes de séquence respectées et observables. Aucun incident de sécurité/autorité critique laissé sans résolution.
4. Reprise intersessions/harnesses fidèle sur les cas nouveaux fixés, y compris canon courant/prédécesseur, preuve périmée, retour tardif et information unique. Aucun faux résultat, perte de preuve, promotion non approuvée ou prochaine action hors mandat dans les passages de confirmation.
5. **Les confirmations réussissent sans réparation manuelle de la mémoire par l'évaluateur ni substitution du lecteur défaillant par un modèle plus favorable.** Une revue faisant partie du workflow est admissible si préfixée dans les deux conditions et son coût/intervention comptabilisé. Les anciens résultats remédiés ne satisfont pas seuls ce critère.
6. Résultat du site vérifié par tests adaptés et navigateur/rendu, pas seulement commande qui sort 0. Sources originales inchangées ; tous changements dans les copies ; pas de déploiement.
7. Valeur réelle évaluée contre baseline loyale, qualité/interventions avant coûts. Un gain statistique ou une économie n'est pas exigé artificiellement, mais une utilité concrète sans régression critique doit justifier le noyau retenu.
8. Paquet final exact : chargement/trivial, mesures, install/répétition/update/interruption/divergences/retrait et lecture après retrait, limites des trois profils documentées et preuves rejouables. Pas de confusion entre smoke de commandes et qualification du comportement de mission.
9. Revues fraîches, gels et échecs conservés, secrets privés nettoyés, globals/originaux préservés, processus arrêtés. Restitution précise : réalisé/validé/limites/restant, SHA/commits et commandes d'essai.
10. Dossier d'entrée phase 2 prêt : responsabilités du noyau, contrats/points d'extension réellement nécessaires, matrice d'autorité avec frameworks/skills, candidats à intégrer et tests qui qualifieront leur coexistence. La phase 2 n'est pas exécutée opportunément pour fermer un défaut runtime ; rôle et frontière décidés avant installation méthodologique.

Verdict final explicite : `READY_FOR_PHASE_2` seulement si ces critères sont satisfaits ; sinon `NOT_READY` avec défauts précis, travail indépendant effectué et prochaine action. Ne pas assimiler « beaucoup de tests » à une validation complète, ni clore le goal sur une RC simplement installable.

## Prompt à coller dans la nouvelle session

> Crée un nouveau goal long : rendre Vibe Backbone V2 validé au niveau runtime sur une matrice explicite de capacités et scénarios représentatifs, prêt à entrer en phase 2 d'intégration ou d'adaptation des frameworks spécialisés et skills de développement.
>
> Travaille dans `[FACTORY]`. Lis `.backbone-dev/INDEX.md`, puis `.backbone-dev/handoffs/2026-09-06-runtime-validation-phase2.md`. J'adopte ce mandat, ses critères et ses autorisations : sauvegarde publique contrôlée sur `git@github.com:Bricesodini/vibebackbone_v2.git`, consolidation du plan, tests réels avec sous-agents sur des copies isolées de `[PRIVATE_SITE_SOURCE]`, corrections et requalification du candidat exact. Préserve le dossier source, les travaux préexistants, les gels et les preuves ; ne publie pas le brouillon ni les traces privées par défaut.
>
> Avance sans micro-validations pour les opérations réversibles autorisées. Utilise réellement des sous-agents avec des rôles séparés, tout en conservant les modèles strictement séquentiels, auxiliaires compris. Préfixe les protocoles et confirmations ; ne transforme pas une réparation manuelle de l'évaluateur ou un changement de lecteur en réussite autonome. Aucun runtime d'exécution VBB, aucune installation factory, aucun déploiement du site ou configuration globale. Prépare les frontières de phase 2 sans installer de méthodologie avant décision de rôle.
>
> Ne marque le goal accompli qu'après satisfaction effective des critères et verdict `READY_FOR_PHASE_2`. Si un préalable bloque, poursuis les travaux indépendants et conserve les limites ; ne réduis pas le périmètre pour fermer le goal.
