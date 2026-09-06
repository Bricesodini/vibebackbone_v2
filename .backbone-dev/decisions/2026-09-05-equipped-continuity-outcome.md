# Suite U03 : continuité native équipée, résultat borné et pistes de conception

Date : 2026-09-05. Statut : bilan de collecte et orientations candidates ; aucune
promotion de MP, aucune autorisation L2 ou d'installateur. Autorisation de Brice : rendre
le pilote de continuité opérationnel dans une expérimentation isolée, examiner Pi équipé,
AGENTS.md commun et outils déterministes, puis les sources Backbone-know/VBB/skills.

## Résultat actuel

Les vrais Codex CLI, Pi et DeepSeek Harness ont été utilisés. Codex : gpt-6-astra low.
Pi/DSH : Qwen3.8-27B UD-Q4_K_S local off ; aucun modèle DeepSeek impliqué. Le paquet
pi-subagents déjà présent fournit un reviewer réel, neuf et bloquant. Modèles toujours
sollicités séquentiellement, avec fin observée et trois échantillons de slots inactifs.
La charge extérieure reste inconnue ; aucune conclusion causale de rapidité.

- [Paire M0/MP équipée](../evaluations/continuity-equipped/report.md) : huit fins normales,
  huit oracles métier réussis, création/actualisation/conservation réelles dans les deux
  branches. Échecs stricts : écritures /tmp, Git omis par notre conducteur, erreurs de
  récit et de lecture. M0 est loyalement documenté ; ces défauts ne prouvent pas MP supérieur.
- [Protection native](../evaluations/continuity-confined/report.md) : Pi fonctionne avec
  revue ; deux sandboxes macOS imbriqués rendent le shell DSH indisponible. L'indisponibilité
  est conservée, et la clôture dite dégradée est jugée prématurée.
- [Composition compatible](../evaluations/continuity-confined-v2/report.md) : une seule
  enveloppe macOS obligatoire, shell DSH autorisé à l'intérieur ; tests réellement exécutés,
  mesures produites. Protection et fonctionnement établis sur ce cas, erreurs narratives restantes.
- [Rectification finale bornée](../evaluations/continuity-reviewed/report.md) : les trois
  problèmes donnés en revue sont vérifiés, corrigés par DSH et retrouvés par un DSH neuf.
  Ancienne entrée copiée exactement, historique intact, entrée raccourcie, fait unique conservé.
  Le lecteur produit néanmoins un faux diagnostic d'absence de date dans A : fidélité stricte
  globale non qualifiée. Pas de relance supplémentaire pour effacer ce résultat.

Cette chaîne établit une continuité documentaire réelle et un mode opératoire technique
sur cette machine après remédiations. Elle ne qualifie ni autonomie générale, ni portabilité
de toutes les configurations, ni gain propre de MP. Les corrections guidées MP ne sont pas
une seconde comparaison à M0 : mêmes défauts révélés à l'agent, conditions modifiées.

## Apports de conception proposés

1. [AGENTS.md comme entrée commune](../design/agents-entry-point.md) : accord stable,
   pointeurs conditionnels vers canon et mémoire, sans recopier les journaux. Les trois
   loaders ont des sémantiques distinctes ; l'auto-chargement commun reste à éprouver.
2. [Opérations déterministes bornées](../design/deterministic-continuity.md) : commencer
   par les comparaisons à baseline nommée et les inventaires de transmission. Distinguer
   calcul, preuve d'exécution, interprétation et approbation. Aucun moteur L2 réalisé.
3. [Recherche croisée](../research/2026-09-05-deterministic-continuity/review.md) : sélection
   de contexte et sorties calculées depuis Backbone-know, provenance/revalidation bornée
   depuis VBB, pointeurs et critères d'achèvement depuis mattpocock/skills. Conserver leurs
   limites ; aucun corpus V1 normatif, aucune installation de skill ou méthodologie.

Le [mode opératoire interne](../operations/cross-harness-continuity.md) rend les conditions
reproductibles sans transporter les clés ni confondre sessions et mémoire. Les homes
privés sont nettoyés, réglages globaux et identités natives vérifiés inchangés. La factory
reste sans VBB installé ; manifeste produit vide et contrôle de frontière réussi.

M0 reste la référence tant qu'un gain n'est pas démontré. La prochaine étape de conception
est le protocole indépendant de l'entrée AGENTS et des deux opérations candidates, avec
oracles gelés, coûts complets, cas nouveaux et qualité prioritaire. Elle ne remplace pas
les qualifications de produit différées et ne justifie aucun installateur anticipé.
