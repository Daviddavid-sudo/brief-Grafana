# Design de mon Dashboard

## Objectif
Ce dashboard a pour but de fournir une vue d'ensemble en temps réel de la santé et des performances de notre application.  
Il permet de détecter rapidement les problèmes, d’optimiser les performances et de suivre les indicateurs clés liés à l’application et à la base de données.

## Public cible
- Développeurs et ingénieurs DevOps responsables de la maintenance et du monitoring de l’application.  
- Chefs de projet ou product owners souhaitant suivre la performance globale du système.

## Métriques clés à afficher
1. **Taux de requêtes HTTP**  
   *Pourquoi :* Permet de suivre le volume d’utilisation de l’application et détecter les pics de trafic.

2. **Temps de réponse moyen des API**  
   *Pourquoi :* Permet de mesurer la performance de l’application et d’identifier les endpoints lents.

3. **Erreurs 4xx/5xx**  
   *Pourquoi :* Permet de détecter les problèmes dans l’application ou les erreurs côté serveur.

4. **Utilisation CPU et RAM du serveur**  
   *Pourquoi :* Permet de surveiller la charge système et d’anticiper les besoins en ressources.

5. **Statut de la base de données (connexions actives, temps de requête moyen)**  
   *Pourquoi :* Assure que la base de données fonctionne correctement et détecte les goulots d’étranglement.

6. **Stockage Prometheus et Grafana**  
   *Pourquoi :* Permet de s’assurer que les services de monitoring eux-mêmes fonctionnent et n’ont pas de problèmes de capacité.

## Disposition prévue
