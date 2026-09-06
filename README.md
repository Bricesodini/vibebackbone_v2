# Vibe Backbone V2

Factory de conception et candidat local expérimental. **Validation runtime en cours : NOT_READY.**

Le produit minimal est dans `product/`, la fabrication dans `.backbone-dev/` et `tooling/`. Aucun runtime modèle VBB.

## Reprendre

- `.backbone-dev/runtime-validation/STATUS.md` : mandat et obligations ouvertes.
- `.backbone-dev/runtime-validation/plan-current.md` : état actuel et delta du plan.
- `.backbone-dev/INDEX.md` : historique rc.5, preuves et limites.
- `PUBLICATION.json` : sélection publique, provenance, redactions et exclusions.

Cet export possède un historique public distinct pour ne pas publier les traces privées déjà commitées localement. Les rapports dérivés sont conservés, résultats défavorables compris ; leurs liens vers preuves brutes privées peuvent ne pas résoudre dans cet export. Ce n'est pas une reproduction publique intégrale des expériences. Les originaux, gels, traces, archives et inventaires détaillés sont préservés dans la factory et le dossier privé du mainteneur. Les chemins masqués ne sont pas des commandes exécutables.

Construire rc.7 : `python3 tooling/build_candidate.py`. Tester le paquet reconstruit : `VBB_TEST_ARCHIVE=.backbone-dev/releases/vbb-0.1.0-rc.7.tar.gz python3 -m unittest discover -s tooling/tests`. SHA256 rc.7 : `52bc93ee0cb23152fd90f169d855550fc344f14be277da54474ecee48a64e32a` (en-tête gzip normalisé). Les27 tests publics et20 tests de mesure privés passent ; mise à jour réelle rc.6→rc.7 puis retrait également vérifiés. La conduite rc.7 n'est pas encore qualifiée.

Les dix cellules G1 sont collectées, confirmations insuffisantes conservées. Le diagnostic D1 de12 lectures a motivé une précision du contrat ; il ne remplace pas ces confirmations. Nouveau gel métier encore à préparer. Aucun bénéfice général ni économie démontrés.

Archive historique rc.5 conservée localement : `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1` ; son rebuild gzip diffère malgré un tar identique (REPRODUCTION.json historique). Rc.6 : `d7a4d305704ec180e6870c14000dd93b205bc9bc50fa4d4f1c452a4fc7ac7ff5`, préservée dans l'historique et localement. Les tests et scripts historiques de qualification peuvent dépendre de fichiers privés ou d'archives antérieures non inclus ; ils ne sont pas tous des points d'entrée pour rc.7. Ne pas installer le candidat sur cette factory.
