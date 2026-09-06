# L1 bis — pilote clos, effet de la convention non établi

Date : 2026-09-05. Décision de suite de conception dans le périmètre autorisé du pilote,
pas une nouvelle approbation produit. Sources : [rapport](../evaluations/l1bis/report.md),
[protocole préengagé](../evaluations/l1bis/protocol.md),
[évaluation par critère](../evaluations/l1bis/assessment.json) et
[hypothèses, dont la précision utilisateur](../evaluations/l1bis/hypotheses.md).

Huit essais effectués dans des copies isolées : Codex → Pi → DeepSeek Harness,
plus un lecteur DSH neuf, pour M0 et la convention documentaire minimale MP.
Les passages utilisent réellement ces harnesses ; aucune session Codex n'est
rebaptisée Pi ou DSH. Les notes sont créées, transmises puis, lorsque l'exécution
le permet, actualisées par les agents. Aucun handoff parfait fourni seulement à MP.

Le cycle complet n'est qualifié dans aucune branche. Codex termine les deux créations.
Pi M0 actualise code/tests/mémoire avant timeout ; Pi MP comprend B mais s'arrête sur
une limite de sortie avant d'agir. DSH produit des effets partiels puis atteint les
limites murales ; les deux lecteurs finaux effectuent des contrôles mais ne livrent
pas de restitution complète. Les sources utiles restent présentes, mais les missions
ne sont pas correctement closes. La conservation après clôture demeure inconnue.

La possibilité que Pi/DSH ne disposent pas d'un profil agent fonctionnel pour cette
mission est explicitement conservée à la demande de Brice. Les smokes ne prouvent
pas cette aptitude. Modèle, réglages expérimentaux, plafonds et harness ne sont pas
séparés causalement. Les erreurs documentaires observées restent consignées sans
être toutes imputées à MP ; les arrêts ne démontrent ni son inutilité ni son bénéfice.

## Décision

- Maintenir U03 : besoin de continuité entre harnesses confirmé comme besoin produit.
- Garder M0 comme référence de comparaison, sans le déclarer suffisant en général.
- Conserver MP et ses résultats uniquement dans l'expérience ; aucune promotion ni
  décision de rejet de la mémoire portable fondée sur ces profils insuffisamment qualifiés.
- Avant une nouvelle comparaison, qualifier les profils Pi/DSH sur un cas distinct
  avec modification, contrôle et clôture normale, puis figer des réglages et budgets
  effectifs. Ne pas utiliser le cas déjà examiné comme confirmation aveugle.
- Ne pas engager L2, l'installateur, un importeur/synchroniseur de sessions ou des
  permissions VBB. Les outils du pilote sont internes à l'usine et non distribuables.

Les indisponibilités initiales restent explicites : Ollama local inaccessible,
MiniMax quota atteint, lancement DSH depuis les sources en échec. Les alternatives
réellement utilisées sont épinglées et documentées ; aucun mécanisme global installé.
D01–D03 restent inchangées. Le manifest de distribution reste vide.
