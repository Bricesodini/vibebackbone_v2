# U04 — réception AGENTS observée, qualification commune stricte non acquise

Date : 2026-09-05. Besoin V2 : transmettre un accord de continuité commun sans recopier
ses obligations dans les prompts. Autorisation de Brice : expérimentation isolée sur les
vrais Codex, Pi et DSH ; modèles strictement séquentiels ; aucun L2/installateur ; seulement
préparer le protocole déterministe suivant.

Deux gels distincts, sources et oracles antérieurs à leurs collectes :
- [Premier gel](../evaluations/agents-common/report.md) : Codex 3 comportements conformes ;
  Pi/DSH indisponibles à cause d'une redirection incompatible avec la protection. Erreur de
  conducteur isolée sans appel modèle, résultat conservé.
- [Second gel technique](../evaluations/agents-common-v2/report.md) : neuf comportements
  de loader conformes, AGENTS exact dans les premières requêtes Pi/DSH ; mais DSH lance
  une requête auxiliaire de titre concurrente. **Contrainte de séquence non respectée
  à l'intérieur de DSH.** Aucune phase mémoire exécutée, aucune qualification stricte commune.

Décision : conserver AGENTS racine court comme candidat reçu sur ces profils ; ne pas
l'adopter comme mécanisme de continuité qualifié. Ne pas inférer que les permissions,
priorités d'overrides ou rafraîchissements sont identiques. Pas de promotion MP ni produit.

Le préflight doit inspecter la composition effective des appels modèles auxiliaires et
reproduire les redirections réelles sous protection. Une fin de processus et des slots
inactifs entre sessions ne prouvent pas l'absence de concurrence interne. Le profil DSH
actuel doit être requalifié avec le provider de titre LLM retiré dans un home expérimental,
sans changement global ; aucune nouvelle collecte dans cette tranche close.

La mémoire création → actualisation → lecteur neuf reste à exécuter après ce préalable.
Le [micro-pilote déterministe](../evaluations/deterministic-next/protocol.md) est préparé,
non exécuté : comparaison à baseline nommée et inventaire de transmission, contrôle manuel
loyal, nouveaux contre-exemples, coûts complets. Il ne peut pas démarrer sur la seule base
des réponses correctes aux marqueurs. Le gel exécutable de ce prochain pilote reste à faire.

## Orientation complémentaire de Brice après le bilan

Prendre en compte le statut developer preview et la personnalisation de DSH. U04 échoue
sur une composition donnée, pas sur une incapacité intrinsèque du harness. Étudier la
[configuration DSH depuis une référence Pi fonctionnelle](../design/dsh-from-pi-reference.md)
comme stratégie de suite : capacités prouvées Pi, traduction explicite des paramètres et
plugins, puis qualification DSH native. Cette piste dépasse le seul retrait du titre LLM.
Les résultats antérieurs restent inchangés ; aucune nouvelle collecte déclenchée ici.
