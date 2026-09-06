# L1 bis proposé — continuité d'un projet entre harnesses

Statut historique : plan expérimental proposé après [U03](../decisions/2026-09-05-cross-harness-memory.md).
Au moment de la proposition : aucun run effectué, aucun déploiement engagé, aucun oracle de L1 modifié.
Mise à jour du 2026-09-05 : [pilote L1 bis exécuté](../evaluations/l1bis/report.md) et
[décision de suite](../decisions/2026-09-05-l1bis-outcome.md). Huit essais réels, cycle
complet non qualifié et effet de MP non concluant ; aptitude des profils Pi/DSH à
qualifier avant une nouvelle comparaison. Le plan historique ci-dessous est conservé.
Ce pilote examine le besoin D03/U03 avant L2 ; il ne remplace pas la qualification
complète des profils L3 ou des mécanismes de mémoire L4.

## Question

Une convention minimale de mémoire projet améliore-t-elle une succession de travaux
Codex / Pi / DeepSeek Harness, par rapport à une documentation ordinaire correctement
maintenue, sans que le lecteur ait accès aux sessions natives des autres outils ?

## Deux variantes loyales

M0 utilise les harnesses natifs et les documents ordinaires du projet ; ses agents
peuvent rédiger, organiser et actualiser les notes dont ils ont besoin. La variante
expérimentale ajoute une convention ciblée de localisation du canon, transmission,
provenance et conservation, décrite dans [la conception](../design/cross-harness-memory.md).

Même mission, exigences, faits, décisions et contrôles ; mêmes profils d'exécution
au sein de chaque paire. Le code et les documents produits évoluent naturellement
avec le travail : ne pas fournir seulement à VBB un handoff préfabriqué parfait.
M0 reçoit le même objectif de reprise inter-harness et de conservation. Aucun format
obligatoire caché dans l'oracle, aucun score fondé sur un nom de fichier.

## Chaîne bornée proposée

Choisir un projet d'essai représentatif et isolé. Épingler les versions, modèles,
capacités et modalités de transfert réellement disponibles, sans mutation globale.

1. Un premier harness reçoit la mission et les faits initiaux, réalise une première
   étape et produit sa propre documentation de transmission.
2. Un deuxième reprend uniquement depuis les artefacts partagés. Une décision de
   projet explicitement sourcée modifie une contrainte ; le travail continue dans
   ce nouveau mandat, avec preuves sur l'état modifié.
3. Un troisième reprend et reçoit une contribution fondée sur l'état antérieur.
   Il doit conserver sa provenance, résoudre ce qui est encore applicable et clore
   sans supprimer les sources utiles. Une nouvelle session vérifie ensuite la
   récupérabilité de l'état final et des décisions.

Premier ordre candidat : Codex → Pi → DeepSeek Harness. Un second ordre et un cas
distinct ne se justifient qu'après un signal utile, pour distinguer effet d'ordre,
effet de modèle et effet de la convention. Une chaîne seule reste exploratoire.
Si un harness est indisponible, conserver ce statut ; ne pas rebaptiser trois
sessions Codex en preuve inter-harness. Une simulation documentaire peut préparer
les fixtures, mais ne démontre pas le passage réel.

## Observations et décision, à figer avant collecte

Définir les faits critiques, sources approuvées, modifications de mandat, octets
protégés et critères d'acceptation avant les essais. Distinguer reprise, intégration
et conservation après clôture ; expliciter dans les deux variantes les obligations
de conservation pour éviter l'ambiguïté de L1.

Mesurer exactitude de la reprise, autorité appliquée, reconnaissance du legacy,
fraîcheur des preuves, retours anciens intégrés à tort, pertes d'information,
contexte lu, temps de rédaction/mise à jour/intégration/reconstruction et interventions
humaines. Conserver les valeurs inconnues ; ne pas les convertir en coût nul.
Les traces et artefacts sont évalués, pas la qualité du récit final. Séparer les
cas de développement des cas utilisés pour confirmer une amélioration.

Si M0 satisfait le besoin sans coût évitable identifié, retenir les conventions
ordinaires. Si le complément corrige un manque reproductible à un coût acceptable,
retenir seulement cette partie. Envisager L2 uniquement pour une opération documentaire
répétitive dont les essais montrent le coût ; un gain de mémoire ne justifie pas
à lui seul tout le plan d'outillage ou l'installateur.
