# Vibe Backbone V2

Factory de conception et candidat local expérimental. **Validation runtime en cours : NOT_READY.**

Le produit minimal est dans `product/`, la fabrication dans `.backbone-dev/` et `tooling/`. Aucun runtime modèle VBB.

## Reprendre

- `.backbone-dev/runtime-validation/STATUS.md` : mandat et obligations ouvertes.
- `.backbone-dev/runtime-validation/plan-current.md` : état actuel et delta du plan.
- `.backbone-dev/INDEX.md` : historique rc.5, preuves et limites.
- `PUBLICATION.json` : sélection publique, provenance, redactions et exclusions.

Cet export possède un historique public distinct pour ne pas publier les traces privées déjà commitées localement. Les rapports dérivés sont conservés, résultats défavorables compris ; leurs liens vers preuves brutes privées peuvent ne pas résoudre dans cet export. Ce n'est pas une reproduction publique intégrale des expériences. Les originaux, gels, traces, archives et inventaires détaillés sont préservés dans la factory et le dossier privé du mainteneur. Les chemins masqués ne sont pas des commandes exécutables.

Construire le candidat local : `python3 tooling/build_candidate.py`. Tester : `python3 -m unittest discover -s tooling/tests`. L'archive historique rc.5 conservée localement a pour SHA256 `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`. Le rebuild local a un SHA gzip différent malgré un tar décompressé identique (voir `REPRODUCTION.json`) ; ne pas le présenter comme le fichier historique exact. Les 27 tests publics passent. Les tests de mesure historiques peuvent dépendre de fichiers privés non inclus ; la vérification publique de reproduction est documentée séparément. Ne pas installer le candidat sur cette factory.
