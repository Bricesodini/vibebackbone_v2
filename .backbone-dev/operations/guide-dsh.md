# Guide DSH — référence interne pour Vibe Backbone V2

Statut : guide de conception et d'expérimentation, proposé par Brice le 2026-09-05.
Ce document est l'entrée de référence DSH de la factory. Il ne s'applique pas comme
instruction automatique à l'agent concepteur et n'active aucun mode VBB sur ce dépôt.
Aucun L2, installateur ou profil produit n'est implémenté par ce guide.

## Quand le consulter

Avant de préparer, modifier ou qualifier un profil DeepSeek Harness pour une expérience
VBB V2 ; après une mise à jour de DSH affectant sa composition ; pour interpréter un
écart entre Pi et DSH. Lire ensuite uniquement les références nécessaires à l'opération.

DSH est en developer preview et personnalisable. Un défaut du bundle choisi est un
résultat sur cette composition, pas une incapacité générale du harness. Les versions,
réglages, plugins et protections font partie de la preuve. Une configuration proposée
et une configuration effectivement qualifiée doivent être distinguées.

## Où trouver la référence

| Besoin | Document |
|---|---|
| Configurer DSH depuis Pi | [Stratégie Pi → DSH](../design/dsh-from-pi-reference.md) |
| Examiner un mode VBB V2 natif | [Option de conception](../design/vbb-native-mode.md) |
| Comprendre les obligations documentaires | [Entrée AGENTS](../design/agents-entry-point.md) |
| Reproduire confinement et transmission | [Mode opératoire](cross-harness-continuity.md), y compris son rectificatif U04 |
| Connaître les observations actuelles | [Rapport U04](../evaluations/agents-common-v2/report.md) et [décision](../decisions/2026-09-05-agents-entry-outcome.md) |
| Reprendre la prochaine expérimentation | [Handoff](../handoffs/2026-09-05-after-agents-qualification.md) |
| Vérifier la provenance technique | [Sources DSH/Pi](../research/2026-09-05-dsh-from-pi/sources.json) |

Les collectes closes sont des preuves à consulter, pas des homes ou profils prêts à relancer.
Les sources natives de DSH font autorité sur ses mécanismes ; les besoins V2 déterminent
quels mécanismes retenir. Ce guide ne remplace pas leur vérification à la version présente.

## État connu

Version observée : DSH compilé 0.1.0-rc.8. Modèle des expériences : Qwen3.8-27B local off,
pas un modèle DeepSeek. L'adaptateur DSH utilise pi-ai ; sa configuration et sa boucle
native ne sont pas identiques à celles de Pi Coding Agent.

AGENTS racine est reçu dans les trois sondes U04 : racine, sous-dossier, session neuve
après changement. Les octets apparaissent dans la première requête DSH. Cela ne prouve
ni une continuité documentaire autonome, ni le comportement de tous les overrides.

Le profil headless essayé monte un provider de titre LLM qui appelle le modèle en
concurrence avec la réponse principale. Cette composition échoue à la contrainte de
Brice. Le retrait de ce provider dans un profil privé est une correction candidate,
encore à qualifier. Aucun mode VBB V2 fonctionnel complet n'est déclaré disponible.

## Préparer un profil expérimental

1. Choisir une référence Pi précise et ses capacités prouvées. Distinguer le dialogue,
   les outils, la mémoire et un éventuel reviewer ; ne pas qualifier un ensemble à partir
   du seul succès du chargement AGENTS.
2. Relever versions natives, dépendances et configuration effective. Traduire explicitement
   endpoint, modèle, effort, compatibilité, limites de contexte/sortie et retries. Ne pas
   importer des secrets ou supposer qu'une valeur omise a le même défaut dans les deux harnesses.
3. Créer un home DSH neuf et un projet Git expérimental séparé de la factory. Utiliser les
   mécanismes natifs de profil/patch de la version présente. Vérifier leur résultat composé :
   un patch de ligne peut remplacer tout son bloc config, sans fusion des champs omis.
4. Garder les loaders et outils nécessaires au mandat. Inventorier les appels auxiliaires,
   retries, tâches et délégations possibles. Configurer la séquence stricte à ce niveau ;
   une consigne AGENTS ne contrôle pas un plugin agissant hors de l'initiative du modèle.
5. Relever les fichiers globaux, parents et overrides effectivement consultables. Fournir
   le même accord et les mêmes sources métier aux harnesses, sans recopier les marqueurs
   des oracles dans leurs prompts ni remplacer leur système natif par celui de Pi.

## Vérifier avant de collecter

Tester la commande réelle, son environnement ET ses redirections, sans appel modèle.
Sur le macOS expérimenté, garder l'enveloppe externe obligatoire. Le mode interne DSH
`danger-full-access` n'est utilisable dans cette composition que sous cette enveloppe.
Ne jamais le reprendre seul pour résoudre un refus.

Sonder : écriture permise dans le projet, refus hors projet et sur les sources protégées,
refus de lecture des oracles. Stocker les sorties natives dans le home autorisé, puis les
archiver depuis le conducteur après fin. U04 a montré qu'une redirection directe dans
la factory interdite en lecture pouvait faire avorter Node ; un test par pipes ne couvre
pas cette composition.

Figer profil, sources, prompts, oracles, budget et critères d'arrêt avant collecte.
Épingler la composition effective, pas seulement le nom du profil. Prévoir l'observation
des requêtes internes et des appels auxiliaires, au-delà du seul ordre des processus.

## Exécuter et conclure

Modèles strictement séquentiels pour les expériences de Brice. Attendre la fin locale
et trois observations serveur inactif entre passages. Au timeout, vérifier annulation/fin
côté serveur ; si impossible, suspendre. Le serveur partagé n'est pas réservé par une
observation d'inactivité. Conserver une indisponibilité comme telle.

Qualifier d'abord réception et séquence, puis la petite mission de création, actualisation
et reprise de mémoire. La comparaison déterministe reste séparée. Rapporter chaque
capacité comme documentée, observée, échouée ou inconnue ; ne pas confondre profil chargé,
requête correcte et mission terminée. Nettoyer les copies privées de clés et vérifier
les réglages globaux, les sources natives et la frontière de distribution.

## Entretenir ce guide

Après une nouvelle preuve ou une évolution native, mettre à jour ici les constats utiles
avec leurs liens. Garder traces, gels et rapports historiques intacts. Ne pas recopier les
traces brutes ou les configurations privées dans le guide. Les prochaines décisions sur
un mode VBB V2 s'appuient sur les besoins et preuves, sans importer une méthodologie V1.

Un futur projet utilisant VBB pourrait disposer de son propre `guide-dsh.md`, référencé
conditionnellement par AGENTS pour le travail avec DSH. Ce serait un artefact distinct,
adapté au projet et limité aux capacités distribuées. Le présent guide de fabrication,
ses oracles et ses conducteurs ne doivent pas être copiés automatiquement dans ce produit.
