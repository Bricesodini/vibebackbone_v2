# Frontières d'entrée en phase 2

Statut : **contrats de conception préparés, entrée non autorisée par le verdict runtime actuel NOT_READY**. Aucune méthodologie installée. Décisions de rôle ci-dessous fondées sur les besoins V2 R02/R03/R04/R09/R11 et le mandat adopté, pas sur l'autorité de V1. La qualification runtime reste un préalable à la phase 2 ; les fixtures de coexistence n'en constituent pas une intégration réelle.

## Responsabilités retenues

Le noyau VBB aide à continuer une mission autorisée et à conserver des références/preuves vérifiables dans des documents ordinaires. compare/inventory mesurent leurs sélections ; installation/retrait possèdent leurs fichiers seulement. Le noyau ne possède ni la spécification métier, ni les standards visuels, ni la politique de sécurité du projet. Le harness possède exécution, permissions, sessions et mécanisme de délégation natif. Une capacité native absente reste absente.

Aucune extension d'exécution, loader automatique de méthodes, scheduler ou registre de canon parallèle n'est nécessaire aux points de jonction observés. Le projet peut référencer une source choisie et ses responsabilités, fournir ses tests et conserver les retours des spécialistes. Une intégration ultérieure doit montrer une valeur supplémentaire avant d'ajouter un mécanisme.

## Matrice d'autorité et candidats

Les candidats nommés reprennent les objets demandés/étudiés dans le mandat ; ce n'est pas un classement actuel de leurs versions. Chaque version et ses instructions devront être inspectées et gelées lors de sa propre décision d'intégration.

| Acteur/candidat | Rôle permis après sélection explicite | Source faisant foi | Frontière interdite |
|---|---|---|---|
| Utilisateur/propriétaire du projet | Mandat et décisions métier | Instruction réelle adoptée, ou décision de fixture clairement simulée | Ne pas inventer son approbation à partir d'un retour |
| Spec Kit | Produire/entretenir les artefacts de spécification choisis | Artefact du projet retenu par décision, version/référence connues | N'impose pas ses gates, permissions ou cycle à VBB par présence seule |
| Impeccable | Diagnostic et amélioration visuelle dans le périmètre choisi | Brief/design du projet, rendu vérifié | Ni nouveau mandat ni autorisation d'édition générale/publication |
| Skill de développement/tests | Implémenter et vérifier la demande | Contrat du projet + code exact + résultats natifs | Un test vert ne modifie pas l'autorité ni les exclusions |
| Skill de revue/sécurité | Retour étayé, avec défauts/limites | Sources inspectées et exigences de sécurité choisies | Pas d'approbation de déploiement ni élargissement implicite des accès |
| VBB | Références de reprise, conservation, mesures et retrait | Documents ordinaires du projet et reçus attribuables | Pas de seconde spec, fusion automatique de retours ou certification par hash |
| Codex/Pi/DSH | Exécuter selon leurs capacités et permissions | Configuration native effective qualifiée | Aucune parité inventée, session fraîche ≠ sous-agent |

## Contrats de jonction nécessaires

1. **Source choisie.** Référencer l'artefact, le choix réel/simulé, le rôle et sa portée. Le spécialiste non choisi reste une donnée. Une source historiquement acceptée dont les octets changent ne devient pas automatiquement approuvée dans son nouvel état.
2. **Retour.** Conserver l'auteur réel ou simulé, la base inspectée, les faits nouveaux, propositions et limites. Un intégrateur unique rapproche le retour du canon courant ; duplicata et contradiction restent traçables.
3. **Preuve.** Conserver la sortie native, commande, état du code, conditions et portée. Un résumé doit pouvoir être confronté à sa source. Nouvelle exécution = nouvelle preuve, pas réécriture d'un échec.
4. **Reprise.** Un lecteur neuf peut retrouver mandat, source courante, prédécesseur utile, état exact, limites, faits hors mandat et prochaine action. Aucun schéma additionnel obligatoire n'est établi par ce contrat.
5. **Retrait.** Les artefacts métier du spécialiste et la mémoire restent propriété du projet ; retrait VBB limité à ses effets attribuables. Tester aussi le retrait du spécialiste avant de promettre cette coexistence.

## Tests d'admission pour chaque intégration future

| Test | Résultat attendu |
|---|---|
| Méthode présente mais non choisie | Aucun changement de workflow ou autorité implicite |
| Source choisie, instruction spécialiste contraire au mandat | Conflit signalé ; mandat et travail indépendant préservés |
| Décision nouvelle et ancien retour convaincant | Canon courant appliqué, base ancienne et fait unique conservés |
| Deux sources prétendent gouverner le même objet | Arbitrage explicite ; aucun canon parallèle construit par VBB |
| Preuve verte sur ancienne révision | Fraîcheur refusée, revalidation sur candidat exact |
| Handoff entre trois profils | Sens récupéré, différences natives documentées |
| Retrait/update d'un des deux composants | Documents métier et modifications utilisateur conservés |
| Mission triviale | Pas de cérémonie imposée par simple coexistence |
| Développement réel et défaut introduit | Correction et rendu/tests adaptés sans micro-gate artificiel |
| Export produit/public | Aucun corpus de conception, secret ou projet privé entraîné |

Les versions, oracles, baseline équipée et budgets seront préfixés avant chaque collecte de phase 2. Toute installation nécessite alors la décision de rôle/version/portée correspondante ; cette préparation ne vaut pas installation anticipée. READY_FOR_PHASE_2 exigera les preuves runtime, les confirmations autonomes et la revue fraîche encore ouvertes.
