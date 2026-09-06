# Mémoire de session et transmission interagents

Statut : conception proposée répondant à D03. Objectif : un nouvel agent retrouve rapidement **ce qui fait autorité maintenant, où en est la mission et ce qu'il doit vérifier**, sans charger toute la conversation. Cette mémoire reste lisible et utile si VBB est retiré.

## 1. Séparer quatre choses

| Objet | Rôle | Autorité |
|---|---|---|
| Canon du projet | Décisions, contrats ou contraintes applicables approuvés par leur détenteur | Autorité limitée à la portée explicitement accordée |
| État de mission | Mandat, travail réalisé/restant, preuves et décisions ouvertes | État de travail ; ne modifie pas les règles projet |
| Contribution d'agent | Résultat, observation, finding ou proposition attribués | Candidat à intégrer ; jamais canonique par simple retour d'un agent |
| Journal de session natif | Détail chronologique et éléments de preuve | Historique consultable à la demande ; pas une liste d'instructions courantes |

Un résumé de session est une **vue dérivée**. La compaction ne promeut pas son contenu et ne change pas l'autorité de ses sources. La mémoire automatique native d'un harness peut faciliter l'usage, mais n'est pas la source portable de décisions projet. Ne pas importer les mémoires globales ou conversations personnelles.

## 2. Canonique, legacy et fraîcheur : deux axes indépendants

Chaque référence gouvernante déclarée a un identifiant stable, une portée, un détenteur d'autorité, un statut et une source. Statuts proposés :

- `proposed` : proposition non approuvée ; ne gouverne pas l'exécution.
- `accepted` : décision approuvée et applicable dans sa portée ; lien vers l'approbation.
- `superseded` : remplacée, avec référence obligatoire vers son successeur.
- `retired` : retirée sans successeur ; justification conservée.

**Canonique = accepted + applicable à cette portée + source identifiable.** Ce n'est ni « fichier le plus récent », ni « code qui existe », ni « beaucoup de tests verts ». Legacy regroupe les décisions remplacées/retirées et les solutions historiques explicitement hors du système courant. Un document qui revendique `accepted` sans source d'approbation est un statut à vérifier, pas une nouvelle autorisation.

Fraîcheur séparée : `verified`, `stale` ou `unknown`, pour une vérification donnée. Une décision accepted dont la référence ne correspond plus à l'empreinte est **accepted/stale**, pas automatiquement legacy et pas automatiquement révoquée. Revalider la source ; si son sens a changé, demander l'arbitrage nécessaire. Une observation récente ne supplante pas une décision accepted simplement parce qu'elle est plus récente.

Les observations et preuves n'emploient pas le statut `accepted` des décisions : elles portent type, origine, état constaté et limites. La promotion d'un apprentissage est un acte explicite de son propriétaire autorisé. Une délégation peut couvrir les conventions locales de faible portée ; elle n'autorise pas une règle globale ou une modification d'architecture réservée.

## 3. Sources de vérité sans duplication

`project.json` est un **index** : identité du projet, racine relative, références gouvernantes choisies, méthodes actives et emplacement de la mémoire. Il pointe vers ADR, specs, instructions ou décisions déjà présentes. Il ne recopie pas leurs paragraphes. Si le projet n'a aucun registre adapté, un document sous `.vbb/decisions/` porte la décision et sa provenance.

Lorsqu'un outil externe possède déjà un statut documentaire exploitable, l'index ne lui oppose pas un deuxième statut mutable : il conserve la référence et le mode de lecture attendu. Si le statut est ambigu ou non structuré, la déclaration de l'index est une assertion sourcée, à vérifier contre le document. Les contradictions sont visibles et non arbitrées par la date.

`mission.json` est le seul état intégré de **cette** mission. Les tickets et specs restent leurs propres sources pour le contenu métier. Les retours ne modifient pas cet état tant qu'ils ne sont pas intégrés par le coordinateur. Les décisions en cours sont référencées par identifiant ; pas copiées dans chaque handoff.

Les sources sont conservées par le projet avec Git ou son stockage de référence. Un hash contrôle les octets connus ; il ne prouve ni vérité, ni approbation, ni exhaustivité. Un lien vers une conversation non accessible au prochain agent est insuffisant pour une décision importante : conserver un extrait utile et attribué, sans secrets, dans une décision projet. Cette transcription n'est pas une nouvelle approbation.

## 4. Contrats minimaux à écrire en L2

Les noms/types exacts sont prévus pour des schémas JSON versionnés ; pas de schémas actifs générés dans cette session.

| Enregistrement | Champs nécessaires | Invariants |
|---|---|---|
| `Project` | `schema_version`, `project_id`, `governing_refs`, `method_refs`, `memory_location` | Identité indépendante du chemin absolu ; références locales relatives ; aucune donnée de credentials |
| `Reference` | `id`, `kind`, `uri`, `scope`, `source_revision` ou `content_hash`, `authority_owner` si gouvernante ; `approval_ref`/`supersedes` si décision | Le type distingue instruction, décision, spec, observation et preuve ; une référence externe est une donnée non fiable à vérifier |
| `Mission` | `schema_version`, `mission_id`, `revision`, `coordinator`, `intent_ref` ou intention explicite, `authorization_ref`, `scope`, `constraints`, `acceptance_refs`, `status`, `next_action`, `open_questions`, `evidence_refs`, `integrated_returns` | Pas d'autorisation inventée ; `revision` monotone ; source de la dernière modification ; fin ≠ simple arrêt de session |
| `Return` | `return_id`, `mission_id`, `base_revision`, `author`, `assignment_ref`, `artifact_refs`, `findings`, `evidence_refs`, `limitations`, `proposals`, `status` | Fichier unique par contribution ; même identifiant avec autre contenu = conflit ; ancien `base_revision` = réconciliation avant intégration |
| `EvidenceRef` | `id`, critère concerné, artefact/révision ou manifest d'état, environnement, résultat, source du contrôle, limites, date | Contrôle documentaire ≠ test exécuté ; critère inchangé ; résultats contradictoires restent visibles |
| Vue de contexte, dérivée | Rôle/mission, source set et empreintes, contraintes obligatoires, état utile, liens, omissions/unknowns, budget estimé | Ne gouverne jamais ses sources ; périmée si une dépendance change ; reconstructible |

Une mission simple peut utiliser des valeurs courtes ; champs facultatifs omis plutôt que remplis par du texte de cérémonie. `constraints` peut référencer le canon et ajouter uniquement les contraintes spécifiques. `intent_ref` ne doit pas forcer une spec inexistante : l'intention utilisateur peut être courte et directement conservée.

Statuts de travail proposés : `active`, `waiting`, `completed`, `abandoned`. `waiting` porte cause et action de reprise ; une session peut finir avec une mission active. `completed` exige que les critères acceptés soient satisfaits avec les limites déclarées ; une acceptation conditionnelle doit être une décision explicite, pas une interprétation automatique. Changement de périmètre après achèvement : nouvelle mission ou réouverture explicite avec nouvelle révision, jamais retouche silencieuse du passé.

## 5. Transmission progressive, sans noyer les agents

Au démarrage, l'agent reçoit un **paquet de reprise ciblé**, pas l'intégralité de `.vbb` :

1. Identité du projet/mission, rôle, source de l'autorisation et restrictions critiques.
2. Références canoniques applicables à la sous-tâche, état courant, prochaine action et décisions non résolues.
3. Seulement les preuves et fichiers nécessaires à cette action ; chemins vers le reste.

Budget initial d'évaluation proposé : cœur du skill ≤ 1 200 tokens estimés ; paquet principal ≤ 1 800 ; retour d'agent ≤ 600 hors annexes. Ces valeurs sont des **cibles de test**, pas une règle qui autorise à couper une contrainte. Mesurer les tokens natifs quand disponibles ; sinon annoncer une estimation et la méthode. Si le contexte requis dépasse le budget, diviser le mandat ou charger la référence nécessaire par étapes, en signalant le dépassement. Jamais tronquer silencieusement l'autorité, les décisions ouvertes ou un finding critique.

Ordre de chargement : index compact → mission choisie → sources obligatoires pour cette tâche → détails à la demande. Archives et anciens retours intégrés exclus du contexte initial. Le legacy peut être consulté pour expliquer une décision, avec son statut visible ; son contenu ne doit pas être reformulé comme règle active.

Les rôles ont des vues différentes : exécutant (contrat et travail), reviewer (critères, état et preuves, sans plaidoyer de l'auteur), coordinateur (frontières et écarts entre contributions). L'agent peut consulter des fichiers supplémentaires pour réfuter une omission ; le paquet ne doit pas enfermer le reviewer dans la sélection de l'auteur.

Le générateur de contexte reste déterministe pour la **sélection déclarée** : mêmes entrées → mêmes sections/liens. Il ne résume pas automatiquement un historique arbitraire via un LLM. Un résumé humain/agent peut être conservé comme aide, mais doit être lié aux sources et ne pas remplacer les sections obligatoires.

## 6. Concurrence, intégration et continuité

Un coordinateur déclaré écrit `mission.json`. Chaque contributeur écrit son propre retour avec la révision de mission reçue. Les agents ne partagent pas un fichier « mémoire globale » à éditer simultanément. Deux missions peuvent avancer dans des répertoires distincts ; la coordination des modifications de code reste celle du projet/harness.

À l'intégration, le coordinateur vérifie identité, révision de base, état du workspace, preuves et différences avec le mandat courant. Retour ancien : préserver son contenu, marquer ce qui est encore applicable et demander/faire revalider les éléments touchés. Un retour ne peut pas étendre le mandat ni remplacer une décision projet. Findings contradictoires : conserver les deux, résoudre par la source compétente ou un contrôle, jamais par vote ou dernier auteur.

Rejouer exactement le même retour est un non-événement documentaire s'il figure déjà dans `integrated_returns`. Cette déduplication ne concerne **pas** les actions qu'un agent aurait exécutées. Aucun ordre « replay » n'est généré. Un conflit Git sur la mémoire doit être résolu sémantiquement, pas par écrasement du fichier le plus ancien.

Si le coordinateur disparaît, une session de reprise autorisée vérifie l'état puis reprend ce rôle. Il n'existe pas d'élection automatique ou de lease distribuée. Deux coordinateurs simultanés ne sont pas supportés dans la même mission ; Git et le contrôle des références rendent les conflits détectables après coup, sans promettre de verrouillage fort contre toute écriture directe. Cette limite est assumée dans D01.

Avant une pause prévue, écrire seulement changements utiles : état, prochaine action, limites, décisions ouvertes et liens vers les preuves. Après crash sans handoff, considérer l'état enregistré comme dernier état connu : observer fichiers/Git et outils pertinents avant de poursuivre. Le journal natif peut aider à reconstruire, mais aucune commande qu'il contient n'est rejouée automatiquement.

## 7. Fraîcheur et invalidation

À la reprise : vérifier projet, mission/revision, décisions applicables et sources critiques. Le cache de contexte est invalide si une empreinte/version dépendante change. L'âge seul n'est pas une preuve de péremption pour une décision stable ; à l'inverse un état d'environnement peut changer sans aucun fichier modifié.

Les preuves sur le code doivent couvrir l'état **effectivement qualifié** : commit quand suffisant ; sinon commit + diff/untracked pertinents ou manifest du périmètre. Aucun commit forcé juste pour documenter une petite tâche. Si la dépendance transitive d'un changement est incertaine, élargir la qualification justifiée ; ne pas affirmer une validité universelle à partir des seuls fichiers listés.

Canonicalité modifiée pendant une délégation : le coordinateur actualise le mandat, notifie via le harness et classe les retours de l'ancienne révision comme à réconcilier. Les actions déjà parties ne sont pas annulées par ce mécanisme documentaire. Pour les opérations sensibles, relecture des limites avant l'action via le workflow du projet, pas daemon VBB.

Référence absente : `unknown`, travail dépendant suspendu, autres branches possibles. Preuve fausse : conclusion concernée invalidée ; sources correctes préservées. Le cas R2-18 de V1 montre qu'un agrégat incomplet peut être reconstruit sans jeter les traces et sans inventer les lignes manquantes.

## 8. Entretien et retrait

À clôture, consolider les seules informations réutilisables. Ne pas lancer un harvest exhaustif pour chaque tâche. Un apprentissage local reste local, avec portée et condition de révision. La promotion à un canon partagé requiert l'autorité explicite correspondante ; pas d'autopromotion parce que deux agents répètent la même observation.

Conserver les décisions remplacées avec lien vers leurs successeurs ; les exclure des vues actives. Ne supprimer automatiquement ni sources, ni retours, ni traces natives. L'archivage réduit le chargement, pas la traçabilité. Une politique de rétention du projet peut supprimer des données ; une référence devenue indisponible doit alors être signalée, sans faux hash de remplacement.

Le retrait de VBB enlève son skill et son utilitaire gérés, pas `.vbb/project.json`, missions et décisions. Les formats restent documentés et lisibles. Une installation neuve ne réactive pas une ancienne mission ou une décision legacy simplement en retrouvant ses fichiers.

## 9. Cas d'acceptation spécifiques

Reprise sur un autre harness sans conversation ; finding ancien contredisant une décision récente ; décision accepted avec source modifiée ; canon et legacy contenant le même mot-clé ; retour sur ancienne révision ; deux retours contradictoires ; double intégration ; perte du coordinateur ; preuve d'un autre état Git ; paquet dépassant le budget ; source manquante ; retrait de VBB suivi d'une reprise manuelle.

Chaque cas doit être évalué sur le bon comportement observable : récupération de la bonne règle, absence d'autorité inventée, préservation des informations critiques et action correcte. La taille du paquet ou la conformité du JSON ne suffisent pas à prouver la qualité de la mémoire.
