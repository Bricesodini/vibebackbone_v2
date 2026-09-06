# Exploitation de la mémoire projet entre harnesses

Statut : proposition de conception précisant [U03](../decisions/2026-09-05-cross-harness-memory.md)
et [D03 / mémoire](memory.md). Le besoin est explicite ; les noms de fichiers,
formats et mécanismes sont à éprouver. Aucun contrat JSON L2 n'est implémenté.

## Ce que doit retrouver le prochain agent

Un agent utilisant un autre harness doit pouvoir répondre depuis les fichiers du
projet : quelles décisions s'appliquent, pourquoi, quel travail est autorisé,
quel est l'état réel, quelles preuves le couvrent et quelle action reste utile.
Un résumé complet de toutes les conversations n'est pas requis pour cela.

| Couche | Contenu | Exploitation |
|---|---|---|
| Sessions natives | Échanges, appels d'outils, traces détaillées | Investigation à la demande ; localisation et origine si disponibles |
| Artefacts de travail | Code, specs, décisions, tests, résultats, contributions | Sources identifiées avec état/révision ; chaque outil garde sa responsabilité |
| Documentation canonique | Décisions et contraintes approuvées, applicables à une portée | Autorité identifiable ; successeurs explicites ; propositions et legacy séparés |
| Mémoire de continuité | Index utile, mandat, état, questions ouvertes, preuves et prochaine action | Entrée portable et ciblée pour un agent qui ne possède pas les sessions précédentes |

La documentation canonique reste celle du projet. VBB doit permettre de la trouver
et d'en comprendre le statut ; il ne doit pas recopier une spec ou faire d'une note
de session une deuxième source métier. Code existant, date récente et test vert ne
créent pas à eux seuls une approbation.

## Cycle proposé, déclenché par les changements utiles

**Entrer dans le projet.** Lire une entrée courte qui désigne les sources applicables
et les missions disponibles ; choisir la mission à partir de la demande, sans
sélection automatique par date. Consulter ensuite les seules sources nécessaires.

**Travailler dans un harness.** Les fichiers, tests et sessions se produisent avec
ses outils natifs. Conserver les décisions nouvelles à leur source avec provenance ;
les idées non approuvées restent des propositions. Une conclusion de test référence
les octets effectivement contrôlés, pas seulement la session qui l'a annoncée.

**Transmettre.** Avant un passage prévu, mettre à jour l'état utile dans les documents
ordinaires du projet : mandat, contraintes, réalisé/restant, état des artefacts,
preuves, inconnues et prochaine action. Une référence de session indique l'origine ;
elle ne remplace pas l'information critique si le destinataire ne peut pas l'ouvrir.
Le passage utilise les fichiers disponibles dans la copie de travail ou le mécanisme
Git choisi par le projet ; aucun service VBB de synchronisation n'est supposé.

**Reprendre ailleurs.** Lire cette entrée, vérifier les sources et l'état réel, puis
poursuivre sans refaire approuver un mandat valide. Une preuve ancienne ou une source
absente est signalée pour la conclusion concernée. Après interruption sans note,
l'état mémorisé est seulement le dernier connu et doit être confronté aux fichiers.

**Intégrer plusieurs contributions.** Préserver auteur, mission et révision de départ
de chaque retour. Un coordinateur intègre l'état commun. Une contribution sur ancienne
révision se réconcilie ; une contradiction ne se résout pas par récence. Cette
convention ne protège pas techniquement contre les écritures concurrentes.

**Clore sans perdre.** Marquer l'état terminé et retirer les éléments obsolètes de la
vue de démarrage. Conserver les sources des décisions et les preuves nécessaires ;
archiver ou référencer une note qui porte encore une information unique. L'absence
de travail restant n'est pas à elle seule un motif pour effacer la mémoire utile.
Une politique de conservation du projet reste possible, explicite et indépendante.

## Exemple de résultat recherché

Codex produit un correctif et une preuve sur l'état A. Pi reprend depuis les fichiers,
constate une décision B remplaçant A sur un point, poursuit le travail et revalide ce
qui est touché. DeepSeek Harness reçoit le projet et un retour tardif fondé sur A :
il retrouve B, conserve le retour sans le promouvoir, distingue les preuves encore
utiles des preuves périmées et poursuit la mission courante. Aucun lecteur n'a besoin
d'accéder à l'interface ou au stockage de sessions du harness précédent.

Il s'agit d'un scénario cible, pas d'un comportement déjà qualifié sur ces outils.

## Hypothèses distinctes à tester

- Portabilité : les informations critiques suffisent sans accès à la session native.
- Canon : la source applicable est retrouvée malgré une proposition récente ou du legacy.
- Fraîcheur : le destinataire relie preuves et état réel, sans PASS hérité aveuglément.
- Sélectivité : l'entrée utile évite une lecture exhaustive sans masquer une contrainte.
- Entretien : produire et intégrer cette mémoire coûte moins que reconstruire le travail.

La présence de documents ou leur conformité syntaxique ne démontre aucune de ces
hypothèses. Le complément minimal peut rester une convention documentaire ; un outil
ne se justifie que par une opération répétée et coûteuse observée durant les essais.
