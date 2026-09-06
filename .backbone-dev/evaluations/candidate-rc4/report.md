# Candidat rc.4 — deux frontières d'interruption corrigées

Archive exacte SHA256 `0846c70222ea55bc779076cc20d251e9d4b9e554d5300519c592fb4f2bbc8165`, six fichiers produit. Rc.1, rc.2 et rc.3 conservés. Aucun paquet installé sur la factory.

La revue fraîche de rc.3 a exécuté les 23 tests présents et reproduit deux défauts supplémentaires : temporaire AGENTS à la racine non déclaré après os._exit ; interruption entre suppression du reçu et rmdir laissant un dossier vide impossible à retirer par répétition. Traces dans `../candidate-rc3-review/runs/02-review`. Première tentative refusée avant modèle faute de Git dans la copie de revue ; gel 2 distinct après git init, sans modification des fichiers examinés. Lecture seule et nettoyage credential vérifiés.

Rc.4 conserve désormais tous les temporaires dans `.vbb`, y compris pour AGENTS. Un temporaire restant est inspecté et déclaré comme résidu, jamais supprimé par supposition fondée sur le préfixe. Ce choix garde une attribution conservative sans introduire un journal récursif des journaux ; un arrêt brutal peut donc nécessiter l'examen manuel d'un résidu, explicitement documenté. Il ne nettoie pas rétroactivement les temporaires racine produits par les anciennes versions.

Un `.vbb` totalement vide est inspecté `empty` et remove peut retirer ce dossier vide sans reçu. Aucun fichier n'est alors attribué/supprimé ; cette règle vaut aussi pour un dossier vide préexistant. Fichiers inconnus non vides toujours conservés/refusés conformément au cycle de vie.

Deux tests supplémentaires utilisent réellement un sous-processus os._exit avant remplacement AGENTS et une interruption finale avant rmdir. Ils échouent sur rc.3 (preuve conservée), passent sur rc.4. Résultat : 22 tests lifecycle + 3 frontière, 20 tests de mesure sur le module extrait, parcours CLI install/répétition/inspect/compare/retrait/répétition passent. Le compteur ancien 20 lifecycle du rapport de génération a été corrigé à 22 ; première sortie conservée, aucune requalification d'un gel.

Les profils distribués documentent désormais les versions, paramètres, frontières de sécurité, échecs et remédiations observés. Les deux outils de mesure et l'accord commun sont identiques à rc.2. Le cycle de vie et les docs ont changé ; la nouvelle revue de rc.4 et une mise à jour réelle depuis rc.2/rc.3 restent à vérifier. Les qualifications de lecture restent expérimentales et ne promettent pas une autonomie sans revue. Goal non accompli ; audit intégral encore requis.
