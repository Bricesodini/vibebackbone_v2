# Profils natifs — qualification expérimentale locale

VBB ne lance aucun modèle et ne configure aucun harness. Exécution, permissions, sessions et secrets restent natifs. Les observations ci-dessous concernent un environnement précis, pas une équivalence de sécurité ni une garantie de fidélité.

## Capacités observées

| Profil | Versions observées | Résultats et limites |
|---|---|---|
| Codex CLI | 0.153.0-alpha.5, gpt-6-astra, effort low | Réponse triviale sans outil/document ; correction métier avec captures réelles, préparation de mémoire et revue fraîche. Fin du processus natif observée ; fin serveur cloud non directement observable. |
| Pi | 0.84.2, Node 24.14.1, Qwen3.8-27B UD-Q4_K_S, thinking off | Reprise et adaptation à une décision approuvée, preuves brutes conservées. Erreur de décompte dans un résumé ; un lecteur après retrait a bouclé jusqu'au timeout. Après revue et clarification explicites, lecteur neuf terminé et faits essentiels récupérés. |
| DeepSeek Harness | 0.1.0-rc.8 compilé, Node 24.14.1, même Qwen local off | Outils installés compare/inventory utilisés, retour ancien confronté au canon, information hors mandat conservée. Confusions de chronologie et de provenance dans des lectures ; récupération des faits essentiels après clarification, avec imprécisions de références dans la prose. |

Les trois profils ont répondu à une demande triviale sans modifier de fichier. La mission de qualification a utilisé le code et l'accord du candidat rc.2 ; rc.3 ne changeait que cette documentation ; rc.4 corrige ensuite deux frontières d’interruption du cycle de vie. Rc.5 corrige le traitement de deux entrées invalides des mesures (chemin non encodable, boucle symbolique de racine). L’accord commun et la sémantique des mesures valides restent identiques. Les profils ne sont pas qualifiés comme autonomes sans revue. Les vérifications de fichiers ne certifient pas les affirmations du modèle. Conserver les captures natives, recompter les résultats cités et vérifier les références déterminantes. Une chronologie courte peut éviter de confondre défaut initial, correction et changement de décision ; elle ne constitue pas un deuxième canon métier.

La mission utilisait un reporter de tests propre au projet qui écrit des captures nouvelles, avec empreintes avant/après. Cette capacité n'est pas fournie par VBB. La mémoire est restée disponible après retrait ; les reprises réussies ont nécessité une revue puis une clarification déclarées. Ces interventions ne sont pas une réussite autonome rétroactive. Aucun gain général de temps ou de tokens n'est établi.

## Réglages des essais

Homes privés neufs, sans configuration globale modifiée. Pi : mode headless JSON, offline, sans extensions/skills/templates/thèmes ni session persistante. Provider local explicite, modèle Qwen ci-dessus ; poids `Qwen3.8-27B-UD-Q4_K_S.gguf`, révision du dépôt de poids `4ca720788d1e01f1bff70c033e0d0028fd02e502`. Le modèle employé dans DSH n'est pas un modèle DeepSeek.

Pi/DSH : contexte déclaré 131072, sortie maximale 8192, thinking off envoyé, retries zéro. Endpoint et credentials configurés dans les homes privés du harness, jamais dans la mémoire du projet. Ces réglages dépendent du modèle et de l'adaptateur ; ils ne sont pas des valeurs universelles.

DSH : profil natif `headless`, `DSH_HOME` privé et télémétrie désactivée. La composition expérimentale désactive les identifiants suivants : `session-title-llm`, `tool-subagent`, `tool-subagent-fork`, `tool-subagent-control`, `tool-subagent-list-agents`, `tool-subagent-report`, `tool-workflow`, `tool-ralph`, `tool-web`, `web-search-deepseek`, `goal-round-driver`, `tool-goal`, `command-goal`, `session-telemetry-otel`. Vérifier la composition effective sur la version utilisée : retirer les requêtes auxiliaires demande davantage que lancer les processus dans l'ordre.

Sur le macOS des essais, le mode interne permissif était toujours placé dans une enveloppe externe `sandbox-exec` vérifiée avec commandes et redirections réelles. Elle limitait les écritures au projet d'essai/home privé, protégeait les sources choisies et interdisait les écritures projet des lecteurs. **Ce paquet ne fournit pas cette enveloppe. Ne pas reproduire le mode permissif seul.** Utiliser les permissions natives adaptées et les qualifier avant l'essai ; aucune équivalence avec le sandbox d'un autre système n'est affirmée.

Les requêtes locales internes étaient observées : un seul appel actif et streams terminés, fin locale et trois observations serveur inactif aux frontières. Un serveur partagé inactif n'est pas réservé. Après timeout de fin inconnue, suspendre les appels dépendants ; ne pas supposer qu'arrêter le client arrête toute requête serveur.

Après une commande échouée, examiner son résultat, changer d'approche ou signaler la limite ; ne pas répéter à l'identique sans progrès. Pour Git, préférer `révision:chemin` à la recopie manuelle d'identifiants. En lecture seule, conclure à partir des preuves vérifiées en nommant ce qui reste inconnu. Ces consignes aident la reprise ; elles n'en garantissent ni la terminaison ni l'exactitude.

## Nouvelle campagne runtime — préparation rc.6

Rc.6 actualise les conditions expérimentales ; l'accord de continuité et les deux mesures restent inchangés. Aucune qualification complète de mission du site n'est encore acquise.

Versions revalidées : Codex embarqué 0.153.4 (le binaire PATH 0.147.0 est distinct et n'est pas substitué), Pi 0.84.2, DSH compilé 0.1.0-rc.8 ; Node24.14.1, Python3.11.11, Playwright1.62.1, Chromium151.0.7922.34. Les sessions Codex de cette campagne sont neuves, multi_agent désactivé ; la coordination de sous-agents de fabrication est observée séparément. Pi n'offre pas de sous-agent natif dans la composition installée.

Le nouveau profil privé DSH conserve spawn/fork natifs mais impose foreground one-shot, enableRunInBackground=false, maxDepth=1 et maxParallelToolCalls=1. Les titres LLM, workflows, ralph, web et conducteur goal restent désactivés. Une délégation spawn réelle a été observée : parent puis enfant puis parent, sept requêtes complètes sans chevauchement. Fork n'est pas qualifié par ce passage. La compaction native reste activée : elle est attendue entre étapes dans les sources inspectées, mais son déclenchement n'a pas été exercé dans ce court essai. Toute compaction pendant mission doit être identifiée et vérifiée, pas présumée.

Les essais Pi/DSH utilisent une enveloppe externe privée limitant les sorties réseau au point de capture modèle local et au serveur de test navigateur possédés par l'essai. Le point de capture relaie vers un amont fixe, sans modifier les corps des requêtes, sans ordonnanceur ni décision de modèle ; il mesure tous les appels de cette chaîne et leur terminaison. Il n'est pas distribué par VBB. Des sondes sans inférence ont vérifié le refus des accès directs au serveur modèle, aux autres services locaux et d'un contournement Python. Le réseau de Codex reste natif et distinct ; aucun accès métier externe n'est autorisé dans le mandat de test.

Deux gels précédents de diagnostic restent échoués : un appel serveur supplémentaire n'était pas attribuable avec leur observation ciblée. La nouvelle enveloppe ferme ce défaut de couverture pour la chaîne contrôlée ; elle ne réserve pas le serveur partagé et ne requalifie pas les gels précédents. Les trois observations serveur idle aux frontières, les fins locales, les appels internes et les coûts confondus par une charge tierce restent distincts. Le bon résultat d'une délégation de calcul n'est pas une qualification de mission métier ou de mémoire.
