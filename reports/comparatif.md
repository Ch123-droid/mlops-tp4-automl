# Comparatif des approches - projet fraude (TP04)

Date de consultation de la documentation cloud : 20/10/2026.
Mesures locales : mon poste, F1 sur le jeu de test (25 %, random_state=42).

| Approche | F1 test | Temps humain | Temps machine | Cout estime (source, date) | Explicabilite | Export / reversibilite |
|---|---|---|---|---|---|---|
| Logistique (ref.) | 0.7407 | ~5 min | ~1 s | 0 (poste local) | Maximale | Total |
| Manuel (TP2) | 0.8669 | ~1 h (essais du TP2) | quelques s par modele | 0 (poste local) | Moyenne/Bonne | Total |
| FLAML 60 s | 0.8409 | ~5 min | 60 s | 0 (poste local) | Moyenne/Basse | Total |
| Vertex AI AutoML | non mesure | ~15 min (console) | budget en node-hours | 21,252 $ par node-hour, entrainement tabulaire (cloud.google.com/vertex-ai/pricing, 20/10/2026) | Bonne | Faible / Verrouillage (Vendor Lock-in) |
| SageMaker Autopilot | non mesure | ~15 min (Canvas ou API) | duree du job AutoML | facturation a l'usage : instances x duree du job (docs AWS + page SageMaker pricing, 20/10/2026) | Bonne | Faible / Verrouillage (Vendor Lock-in) |
| Azure Automated ML | non mesure | ~15 min (Studio) | duree du job | aucun supplement AutoML : seulement le calcul (VM) et le stockage (azure.microsoft.com, pricing, 20/10/2026) | Bonne | Faible / Verrouillage (Vendor Lock-in) |

## Points relevés dans la documentation (E1)

- **Vertex AI** : AutoML tabulaire facturé par node-hour (21,252 $ / node-hour pour l'entrainement en classification/regression). Chaque job d'entrainement ajoute aussi le cout d'un pipeline run gere.
- **SageMaker Autopilot** : l'interface migre vers SageMaker Canvas. Rapports d'explicabilite (SHAP via Clarify) et de performance pour le meilleur candidat, plus notebooks d'exploration des donnees et de definition des candidats modifiables.
- **Azure ML** : pas de frais pour le service lui-meme ; on paie le calcul et les services associes (Blob Storage, Key Vault, Container Registry, Application Insights). Tableau de bord Responsible AI (explicabilite, equite, analyse d'erreurs).

## Commentaire (5 lignes)

1. **Logistique** : point de depart obligatoire et reference de comparaison ; suffit si le besoin est l'interpretabilite maximale (+ audit simple).
2. **Reglage manuel** : justifie quand le modele est critique et qu'on veut comprendre chaque choix ; ici il reste le meilleur (0.8669), mais coute le plus de temps humain.
3. **FLAML local** : tres bon rapport cout/temps pour un premier modele solide en quelques minutes (0.84 des 10 s) sans cout cloud, avec journal des essais.
4. **Plateformes cloud** : pertinentes pour une equipe sans infra, des donnees volumineuses ou deja dans le cloud, et besoin d'explicabilite/deploiement integres ; attention a la facturation a l'heure et au verrouillage.
5. **Dans tous les cas** : aucun AutoML ne detecte une fuite de donnees (bloc D) ; la definition du probleme, des variables disponibles au moment de la decision et du suivi en production reste humaine.
