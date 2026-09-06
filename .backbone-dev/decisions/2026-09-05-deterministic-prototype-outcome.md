# U05 — deux opérations déterministes prototypées en interne

Date : 2026-09-05. Brice demande d'enchaîner sur les outils après le cadrage DSH.
La tranche passe du seul protocole à un prototype local isolé ; aucun L2 ni installateur.

Besoin : supprimer les comparaisons à baseline implicite et rendre visibles les pertes
mécaniques de transmission, sans donner aux empreintes une autorité qu'elles n'ont pas.

[Prototype et rapport](../experiments/deterministic-tools/report.md) :
- `compare` : baseline déclarée nommée, chemins explicites, tailles/empreintes et statuts.
- `inventory` : fichiers et références requis source/destination, résolution des commits Git.

Les oracles précèdent l'implémentation ; 20 tests locaux passent et deux exemples CLI
produisent les différences attendues. Les omissions sémantiques restent non calculables
à partir de la seule liste. Aucun appel modèle ni comparaison manuel/outils exécuté.

Décision bornée : conserver l'instrument comme candidat au prochain micro-pilote. Les
entrées provisoires ne constituent pas un contrat produit. Aucun gain de tokens/temps
ou fidélité n'est établi ; coût humain de développement/maintenance non chronométré.

Le développement local des opérations peut avancer indépendamment de DSH. Le préalable
DSH/AGENTS/mémoire reste requis avant la comparaison impliquant les trois harnesses.
Le [protocole antérieur](../evaluations/deterministic-next/protocol.md) conserve son statut
historique préparatoire ; un gel exécutable complet de la comparaison reste à constituer.
