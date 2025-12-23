# VEILLE_OBSERVABILITE.md

## Phase 0 – Veille & Concepts d’Observabilité

### 1️⃣ Monitoring vs Observabilité

**Question :** Quelle est la différence entre monitoring et observabilité ?

**Réponse :**

- **Monitoring** : Permet de savoir **quand** un problème survient.  
  - Exemples : alertes sur downtime, CPU > 90%, erreurs HTTP 5xx.  
  - Approche réactive, dashboard fixe.
- **Observabilité** : Permet de comprendre **pourquoi** un problème survient.  
  - Exemples : corrélation logs, traces distribuées, analyse de goulots.  
  - Approche proactive, exploration ad‑hoc.

---

### 2️⃣ Les 3 piliers de l’observabilité

1. **Métriques (Metrics)**  
   - Données numériques dans le temps.  
   - Exemples : CPU %, requêtes/sec, latence P95.  
   - Usage : dashboards temps réel, alertes, capacity planning.

2. **Logs**  
   - Événements horodatés textuels.  
   - Exemples : `ERROR [db] Connection pool exhausted`.  
   - Usage : investigation d’erreurs, debugging, audit.

3. **Traces**  
   - Suivi d’une requête à travers plusieurs services.  
   - Exemple : API Gateway → Auth → DB, avec temps de chaque étape.  
   - Usage : microservices, détecter services lents.

> Focus de cette formation : **Métriques**.

---

### 3️⃣ Prometheus

**Définition :** Base de données time-series open-source spécialisée dans les métriques.

**Architecture : Pull vs Push**

- **Pull (Prometheus)**  
  - Prometheus scrappe `/metrics` toutes les X secondes.  
  - Avantages : détection automatique si l’app est down, app n’a pas besoin de connaître Prometheus.
  
- **Push (StatsD, autres)**  
  - L’application envoie ses métriques à un collector.  
  - Inconvénients : surcharge réseau possible, app doit connaître le collector.

**Caractéristiques clés :**

| Caractéristique | Détail |
|-----------------|--------|
| Base time-series | Stocke timestamp et valeur |
| Pull HTTP | Scrape `/metrics` |
| Format texte | Lisible par humain |
| PromQL | Langage de requête |
| Rétention | Configurable |
| Stockage local | Pas de dépendance externe |

---

### 4️⃣ Types de métriques Prometheus

| Type | Description | Exemple | Usage |
|------|------------|--------|-------|
| Counter | Ne fait qu’augmenter | `http_requests_total` | Nombre de requêtes, erreurs |
| Gauge | Monte et descend | `memory_usage_bytes` | Utilisation mémoire, connexions actives |
| Histogram | Distribution avec buckets | `http_request_duration_seconds_bucket` | Latences, tailles |
| Summary | Percentiles calculés côté app | `http_request_duration_seconds{quantile="0.95"}` | Latences, P50, P95, P99 |

> Recommandation : **Histogram** plutôt que Summary pour flexibilité et agrégation.

---

### 5️⃣ Grafana

- **Rôle :** Visualisation des métriques Prometheus.  
- **Fonctionnalités :**
  - Dashboards personnalisables
  - Multi-sources
  - Alerting
  - Collaboration
- **Types de visualisations :** Time series, Gauge, Stat, Heatmap, Pie chart

---

### 6️⃣ PromQL

**Fonctions essentielles :**

| Fonction | Usage | Exemple |
|----------|-------|---------|
| `rate()` | Calcule le taux de changement par seconde d’un compteur | `rate(http_requests_total[5m])` → taux de requêtes/sec sur 5 minutes |
| `increase()` | Calcul de l’augmentation totale d’un compteur | `increase(http_requests_total[1h])` → nombre total de requêtes sur 1h |
| `sum()` | Somme de plusieurs séries | `sum(rate(http_requests_total[5m]))` → total toutes instances |
| `avg()` | Moyenne de plusieurs séries | `avg(memory_usage_bytes)` → moyenne mémoire sur toutes instances |
| `histogram_quantile()` | Calcul de percentile sur un histogramme | `histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))` → P95 latence |
| `{label="value"}` | Filtrer par label | `http_requests_total{status="200"}` → uniquement 200 OK |

---

### 7️⃣ Questions et réponses intégrées

1. **Quelle est la différence entre `rate()` et `increase()` ?**  
   - `rate()` donne le **taux par seconde** d’un compteur (dérivé).  
   - `increase()` donne **le nombre total** de changements sur l’intervalle.  

2. **Comment filtrer des métriques par label ?**  
   - Avec `{label="value"}`. Exemple : `http_requests_total{method="GET", status="200"}`.

3. **Que fait `histogram_quantile()` ?**  
   - Calcule un **percentile (P50, P95, P99, etc.)** à partir des buckets d’un histogramme.  

4. **Comment nommer correctement une métrique Prometheus ?**  
   - Forme : `<nom>_<unité>_<type>`  
   - Exemple : `http_requests_total`, `memory_usage_bytes`.  

5. **Quand utiliser des labels vs plusieurs métriques ?**  
   - **Labels** : quand la dimension varie (status, method, region).  
   - **Métriques séparées** : quand c’est conceptuellement différent ou indépendant.  

6. **Quels dashboards Grafana éviter (anti-pattern) ?**  
   - Dashboards surchargés (>10 graphes par page).  
   - Graphes avec trop de séries superposées.  
   - Graphes statiques sans mise à jour fréquente.

---

### ✅ Livrable

- Document **complété** avec toutes les réponses et notes personnelles.
