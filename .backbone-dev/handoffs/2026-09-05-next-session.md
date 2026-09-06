# Handoff — qualifier l'entrée commune avant les outils

Préparé à la demande de Brice le 2026-09-05 pour une nouvelle session. Le bilan et les
preuves précédents sont versionnés au commit `7989bc8`. Ce handoff oriente la reprise ;
il n'autorise pas à lui seul une nouvelle collecte ou une adoption produit. La mission
ci-dessous est une proposition à reprendre avec la demande de la nouvelle session.

## Lecture minimale

1. [INDEX](../INDEX.md), puis [bilan courant U03](../decisions/2026-09-05-equipped-continuity-outcome.md).
2. [AGENTS.md commun](../design/agents-entry-point.md).
3. [Mode opératoire natif](../operations/cross-harness-continuity.md) avant toute exécution.
4. Seulement pour préparer la tranche suivante : [outils déterministes](../design/deterministic-continuity.md)
   et [recherche croisée](../research/2026-09-05-deterministic-continuity/review.md).

Ne pas charger les traces brutes en bloc. Consulter un rapport puis son extrait et les
lignes natives nécessaires si une affirmation doit être vérifiée.

## État transmis et limites à préserver

Deux vraies chaînes Codex → Pi → DeepSeek Harness → DSH neuf ont été exécutées avec
mémoire produite et entretenue pendant le travail. La paire M0/MP reste sans vainqueur :
les deux branches ont des défauts stricts. Des reprises guidées MP ont ensuite stabilisé
le fonctionnement technique et corrigé trois erreurs documentaires ; le lecteur final
produit encore un faux constat d'absence de date. Aucun cycle autonome entièrement fidèle
n'est qualifié. Ne pas poursuivre Q-27 pour chercher un dernier PASS ; cette collecte est close.

Profils observés : Codex CLI gpt-6-astra low ; Pi 0.84.2 et DSH compilé 0.1.0-rc.8 utilisent
Qwen3.8-27B UD-Q4_K_S local off, pas un modèle DeepSeek. Pi dispose du paquet existant
pi-subagents 0.42.1, avec un reviewer neuf bloquant. L'équipement, la mémoire et le point
d'entrée AGENTS sont trois facteurs distincts.

Les réglages globaux n'ont pas changé ; les copies privées de clés ont été retirées.
Les chemins temporaires des anciens profils sont historiques : ne pas les réutiliser
comme profils prêts à lancer. Reconstituer de nouveaux homes isolés si une collecte
est demandée, sans clés dans les artefacts. Les résultats sont archivés avec empreintes.

## Prochaine mission proposée : AGENTS comme entrée commune

Question unique : un AGENTS.md racine peut-il transmettre les mêmes obligations de
continuité aux trois harnesses réellement disponibles, sans recopier ses consignes
dans chaque prompt ? Cette tranche teste réception et utilisation, pas supériorité MP.

1. Revalider versions, modèles, loaders, capacités natives et protection d'écriture.
   Pi était lancé avec `--no-context-files` : ce profil ne teste pas le chargement AGENTS.
   Examiner aussi les fichiers globaux/overrides ; ne pas supposer les priorités identiques.
2. Préparer une fixture indépendante sous les évaluations internes, avec AGENTS court,
   mandat/canon, entrée de mémoire et critères observables. Figer sources, prompts et
   oracles avant collecte. Le prompt ne doit pas révéler les marqueurs recherchés.
3. Tester séquentiellement Codex, Pi puis DSH : racine, sous-dossier et session neuve
   après changement d'une instruction. Fixer auparavant nombre de passages et budget ;
   distinguer preuve de chargement disponible et simple comportement compatible.
4. Si ce préalable réussit, vérifier sur une petite mission nouvelle que l'instruction
   conduit réellement à créer puis actualiser la mémoire et à la reprendre en session
   neuve. Même documentation ordinaire accessible à tous ; pas de note parfaite injectée.
5. Produire matrice observée/documentée/indisponible, écarts, traces et verdict borné.
   Un échec reste explicite ; pas de substitution par plusieurs sessions Codex.

Critère de fin de tranche : chaque capacité annoncée possède une preuve ou une limite
explicite ; les différences natives sont documentées ; aucune configuration globale ni
produit modifié. Aucun besoin de finir avec trois PASS. La décision de suite doit distinguer
ce qui est utilisable sur ces profils de ce qui reste une hypothèse générale.

## Tranche suivante, séparée

Préparer ensuite un micro-pilote de deux opérations déterministes : comparaison à une
baseline nommée et inventaire de transmission. Réutiliser les contre-exemples observés
mais ajouter des cas nouveaux, geler les oracles et inclure le coût d'entretien des
entrées structurées. Comparer à une baseline manuelle loyale, AGENTS et équipement égaux.
Un éventuel prototype doit rester un instrument expérimental interne, sans contrat L2.
Ne pas mener cette comparaison en même temps que le test du loader AGENTS.

## Contraintes persistantes

- Modèles strictement séquentiels. Attendre fin complète et observation serveur inactive ;
  après timeout, fin/annulation vérifiée avant le suivant, sinon suspendre explicitement.
  Le serveur partagé n'est pas réservé par un constat d'inactivité.
- La composition DSH vérifiée désactive sa sandbox interne uniquement sous l'enveloppe
  macOS externe obligatoire. Ne jamais lancer ce profil seul ni modifier le réglage global.
  Le guide décrit les sondes natives de refus d'écriture et leurs limites.
- AGENTS oriente ; il n'impose pas des permissions natives. Une preuve structurée n'est
  pas une approbation et une présence dans Git n'établit pas le canon.
- Factory et distribution séparées. Aucun L2, installateur, méthode V1 normative,
  installation de skills Matt Pocock ou application de VBB à l'agent concepteur.
- Garder les collectes closes intactes. Créer de nouveaux dossiers et de nouveaux gels.
