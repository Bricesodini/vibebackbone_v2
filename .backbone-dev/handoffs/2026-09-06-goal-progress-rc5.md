# Reprise rc.5

Goal actif, aucune nouvelle décision humaine nécessaire. Dernière tranche : upgrades rc.2/rc.3 → rc.4 réussis ; revue fraîche rc.4 a exécuté 45 tests et vérifié archive, aucun nouveau défaut conservation ; deux P3 d'entrée invalide reproduits et corrigés rc.5. Lire [rapport rc.5](../evaluations/candidate-rc5/report.md). Archive SHA256 `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`.

27 tests (22 lifecycle+3 frontière+2 CLI d'entrée invalide), 20 mesures et CLI exact passent ; deux nouveaux tests échouent sur rc.4. Upgrades réels rc.2/rc.3/rc.4 → rc.5 puis retrait préservent exactement AGENTS, mémoire et données. Outils source `continuity.py` change : fsencode validation et RuntimeError de resolve convertis en InputError. Cycle de vie inchangé depuis rc.4 ; profils documentent delta.

Prochaine action : revue fraîche ciblée des deux corrections et archive rc.5 exacte, avec sources de tests. Une revue générale complète rc.4 existe ; ne pas prétendre qu'elle portait sur rc.5. Après corrections revues, auditer mandat intégral : bénéfice comparatif, noyau conditionnel, mission/reprise/remédiation/limites réelles, versions/profils, archive/distribution/secret, lifecycle exact et données préservées, restitution utilisable. Revoir les instructions initiales, ne pas marquer goal complet faute d'autres idées ni renommer réussite universelle les résultats expérimentaux.

Aucun modèle actif : reviewer rc.4 terminé normalement en 175 s, idle confirmé, home auth nettoyé, copie read-only vérifiée. Aucun commit/push, aucune suppression de travaux préexistants, anciennes archives et gels conservés. Le [handoff rc.4](2026-09-06-goal-progress-rc4.md) et [PARCEL-95](2026-09-06-goal-progress-parcel95.md) donnent les limites antérieures. Modèles strictement séquentiels, titres/delegation désactivés dans profils privés. Ne pas installer sur factory.

## Avancement suivant

Revue ciblée rc.5 exécutée : [rapport](../evaluations/candidate-rc5-review/report.md), aucun défaut actionnable, 47 tests +24 contrôles CLI natifs et archive vérifiés. Fin/readonly/nettoyage confirmés.

Contrôle rc.5 installé réellement par Codex/Pi/DSH : [rapport](../evaluations/candidate-rc5-native/report.md), 6 résultats outils natifs extraits et validés, code0, trois projets inchangés. 23,87 /25,55 /30,92 s. Profils gelés, streams séquentiels, homes/templates nettoyés. Aucun modèle actif.

Prochaine action concrète : finir [audit du mandat](../evaluations/final-audit/requirements.md). Matrice préparée mais pas de verdict global encore : vérifier intégrité consolidée archives/gels/secrets, juger explicitement la portée des imprécisions narratives vs exigences (pas de qualification universelle), puis rédiger restitution locale utilisable. Ne pas relancer encore une revue de code sans nouveau besoin : revue générale rc4 et corrections rc5 examinées, tests suffisants sur changements connus.
