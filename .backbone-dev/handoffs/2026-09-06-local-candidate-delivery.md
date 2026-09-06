# Candidat local minimal livré — Vibe Backbone V2 rc.5

Archive : [vbb-0.1.0-rc.5.tar.gz](../releases/vbb-0.1.0-rc.5.tar.gz).
SHA256 : `47ed2462fae12e8b0365c3c45e32e4516137d331b43b79914d2c36df2580beb1`.
[Audit du mandat](../evaluations/final-audit/verdict.md), [contrôles consolidés](../evaluations/final-audit/checks.json).

## Utilisable maintenant

Deux commandes locales Python standard, compare et inventory, mesurent des sélections explicites. Installation/répétition/update/inspection/retrait sont disponibles dans un projet distinct. L'accord de continuité est court et optionnel (activé par installation), les sources métier restent au projet et aux spécialistes choisis. Aucun service, moteur modèle, secret, profil privé ou conducteur d'évaluation dans l'archive. Six fichiers distribués.

## Essai local isolé

Depuis cette factory, avec un Python 3.10+ (3.11 effectivement testé) :

```sh
essai_vbb=$(mktemp -d /tmp/vbb-essai.XXXXXX)
tar -xzf .backbone-dev/releases/vbb-0.1.0-rc.5.tar.gz -C "$essai_vbb"
mkdir "$essai_vbb/projet"
python3 -B "$essai_vbb/vbb-0.1.0-rc.5/vbb.py" install --project "$essai_vbb/projet"
python3 -B "$essai_vbb/vbb-0.1.0-rc.5/vbb.py" inspect --project "$essai_vbb/projet"
```

Lancer ensuite le harness natif depuis ce projet avec ses permissions appropriées. Lire README.md/profiles.md du paquet pour les deux commandes, les sélections et les bornes de sécurité. Aucun profil global n'est configuré par VBB. En particulier, ne pas lancer DSH en mode permissif seul : les essais utilisaient une enveloppe externe privée qualifiée, non distribuée.

Pour retirer les fichiers gérés :

```sh
python3 -B "$essai_vbb/vbb-0.1.0-rc.5/vbb.py" remove --project "$essai_vbb/projet"
```

Les documents projet restent. Un résidu divergent/inconnu est signalé et conservé ; ne pas effacer un reçu pour forcer son retrait. Le paquet ne doit pas être installé sur cette factory.

## Preuves de valeur et limites

[Comparatif six cellules](../evaluations/value-2026-09-06/report.md) : les sorties des deux instruments sont conservées et reproductibles ; inventory maintient explicitement une ambiguïté que la baseline native a mal interprétée sur un cas. Aucun gain global de temps/tokens, aucun résultat statistique ; la convention seule ne démontre pas de bénéfice propre.

[PARCEL-95](../evaluations/qualification-rc2/report.md) avance/corrige sous A, reçoit B, traite un retour A et transmet Git/preuves ; faux décompte de résumé et timeout de lecture conservés. Après [revue](../evaluations/parcel95-remediation/report.md) et [clarification déclarée](../evaluations/parcel95-chronology/report.md), une [lecture indépendante finale](../evaluations/final-memory-reader/report.md) restitue fidèlement les faits et limites depuis le projet retiré. Ce résultat ne garantit pas l'autonomie sans revue.

## État des trois profils

- Codex CLI 0.153.0-alpha.5 / gpt-6-astra low : travail/correction/revue, lecture finale et deux outils rc.5 observés.
- Pi 0.84.2 / Qwen3.8-27B off : reprise/adaptation, conservation brute, deux outils rc.5 ; erreurs de résumé et boucle d'un lecteur, reprise améliorée après remédiation. Pas de support sans réserve.
- DSH 0.1.0-rc.8 / même Qwen local off : traitement du retour, mesures/transmission et outils rc.5 ; erreurs de chronologie/provenance puis amélioration, imprécisions narratives conservées. Profil expérimental avec auxiliaires concurrents désactivés, pas d'équivalence de sécurité présumée.

[Compatibilité native rc.5 exacte](../evaluations/candidate-rc5-native/report.md). Versions/paramètres/limites détaillés dans product/profiles.md, inclus dans l'archive.

## Fichiers et vérifications

Sources : product/vbb.py, continuity.py, agreement.md, README.md, profiles.md et bundle.json. Assemblage explicite : tooling/distribution.json et build_candidate.py. [Rapport rc.5](../evaluations/candidate-rc5/report.md), [revue finale ciblée](../evaluations/candidate-rc5-review/report.md). 47 tests +24 contrôles CLI additionnels du reviewer ; upgrades réels depuis rc.2/3/4 et retrait exact, anciennes archives et défauts conservés.

Aucun nouveau commit, push ou publication. Les modifications préexistantes et nouveaux artefacts sont sur disque dans le checkout courant, sans suppression/requalification des anciens gels. Tous les modèles sont terminés et les secrets privés nettoyés.

Le candidat local et sa qualification bornée sont réalisés. Adoption sur projets réels, publication, qualification multiplateforme et amélioration de la fiabilité autonome constituent des suites possibles hors de cette livraison ; aucune décision humaine bloquante n'est nécessaire pour l'essai isolé ci-dessus.
