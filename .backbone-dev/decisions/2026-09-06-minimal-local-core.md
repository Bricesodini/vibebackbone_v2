# Noyau local candidat après FRET-62 et comparatif

Décision de conception dans le mandat long adopté, non une approbation utilisateur inventée d'un comportement métier. D01–D03 restent structurantes. Produit **candidat à qualifier**, aucune release acquise.

## Justification

[Comparatif six cellules](../evaluations/value-2026-09-06/report.md) : valeur concrète des mesures structurées compare/inventory, données d'entrée constantes, sorties exactes reproductibles, ambiguïté explicite. Coût non systématiquement inférieur ; interprétation et notes encore faillibles. [FRET-62](../evaluations/integrated-2026-09-06/report.md) : mémoire portable techniquement récupérable, mais faux archivage, reconstitution de preuves et mauvaise temporalité. Une revue neuve retrouve A via Git et simplifie l'entrée ; elle ne requalifie pas l'autonomie des passages précédents.

## Retenu pour construction locale ciblée

- Les deux opérations déterministes en lecture seule, sans autorité métier ni promesse de complétude. Pas de validation du mandat à partir d'un code retour.
- Une aide d'usage autonome, sans références vers la factory.
- Une consigne courte, optionnelle et installée explicitement au projet : sources métier chez le projet/spécialiste, mémoire ordinaire hors fichiers gérés, preuves nouvelles plutôt qu'écrasées, résumés distingués des sorties réelles, observations bornées à l'état mesuré. Son efficacité autonome doit encore être qualifiée.
- Adaptations natives documentées et tests sur versions précises ; DSH profil privé sans auxiliaires concurrents dans les essais. Aucune parité de sécurité présumée.
- Packaging local par liste positive et cycle de vie installation/répétition/mise à jour/inspection/retrait. Sous-répertoire géré .vbb ; données/mémoire projet jamais possédées par l'installateur. Entrée AGENTS attribuable, divergences conservées. Tests dans projets jetables seulement.

## Non retenu

Format de mémoire JSON imposé, schéma de canon parallèle, bibliothèque de fiches, scheduler/routeur, service RAG, auto-réparation de preuves, outil supplémentaire de capture, wrappers d'exécution de modèles. Les scripts expérimentaux de collecte/capture ne sont pas distribués. La capture standard des tests peut être fournie par le projet, comme tout runner de tests ; l'agent doit conserver son résultat réel.

## Conditions de qualification restantes

Une mission neuve doit avancer/corriger sous mandat, recevoir une décision B, préserver le prédécesseur et les preuves, traiter un retour A et être relue fidèlement par un lecteur neuf. Essayer le candidat exact installé dans ces fixtures. Protéger le canon/oracles n'autorise pas de cacher un défaut métier. Tester aussi trivial sans mémoire, spécialiste choisi/non choisi, retrait et reprise sans produit. Revue neuve du contenu final et de sa couverture. Ne pas retirer les trois harnesses ou la mémoire portable pour fermer le goal.

Cette décision ouvre la réalisation locale réversible L2 et cycle de vie. Elle n'affirme pas que les limites de fidélité ont disparu, ni qu'une RC est prête. La distribution finale reste conditionnée aux preuves sur le candidat exact ; en cas de régression critique, corriger ou rester candidat non qualifié.
