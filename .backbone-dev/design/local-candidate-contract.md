# Contrat ciblé du candidat local rc.1

Décision : [noyau minimal](../decisions/2026-09-06-minimal-local-core.md). Conception interne, pas une consigne appliquée à la factory.

## Distribution

Six fichiers dans l'archive : vbb.py, continuity.py, agreement.md, README.md, profiles.md, bundle.json. Bundle schema 1, version explicite et SHA256 des cinq fichiers de contenu ; pas de hash autoréférentiel. Liste positive `tooling/distribution.json` contrôlée par check_boundary. Tar racine relative et fichiers ordinaires, ordre/horodatages fixes. Secrets, profils privés, tests, conducteurs, extraits natifs et rapports d'évaluation sont exclus.

## Mesures

Interfaces compare/inventory héritées en code du prototype dont les 20 tests sont réexécutés sur le module extrait. Entrées et limites explicites : taille/hash sur paths, candidates sans déduction, git_refs avec .git répertoire, statuts non-enregistrement/absence/erreur distincts. Codes 0/1/2 n'approuvent rien. Pas de capture ou exécution de modèle dans le produit. L2 n'introduit pas de schéma mémoire imposé.

## Propriété locale et reprise après interruption

Sous-répertoire .vbb réservé au contenu installé et reçu schema 1 ; données projet/mémoire hors de ce sous-répertoire. Le reçu stocke digests souhaités et antérieurs lors d'un changement pending. Préflight complet des divergences avant remplacement. Écritures atomiques par fichier, journal pending avant mutations. Reprendre avec le même paquet ou retirer seulement les octets attribuables. Pas de transaction globale ni de concurrence d'écrivains annoncée.

Bloc AGENTS exact délimité BEGIN/END, segment ajouté enregistré (inclut éventuelle séparation newline). Retrait supprime ce segment exact et conserve le texte utilisateur autour ; si divergent, ne pas le supprimer. Fichiers divergents, liens et objets inconnus conservés en résidus. Répétition du retrait idempotente. Réinstallation sur résidus retired refuse jusqu'à résolution explicite. Aucun force/rollback aveugle. .backbone-dev dans les ancêtres interdit la factory et ses sous-projets comme cibles de cycle de vie ; essais hors factory uniquement.

## Qualification

Archive SHA256 599b6a4ae0a2f5f025fa138bb6fb1599fba109b6d8d162cdc0cf774b5cc281c8 : 17 tests lifecycle sur bytes extraits, 20 tests mesures sur module extrait, CLI install/répétition/inspect/compare/retrait et mémoire+AGENTS utilisateur conservés. Voir candidate-rc1/local-validation.json. Candidat non qualifié par harnesses à ce stade. La revue fraîche du code exact et des limites reste à faire ; toute correction ouvre une nouvelle archive/identité avant requalification.
