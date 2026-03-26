# 📊 Script d'Analyse de Données de Jeu Vidéo

## Description
Ce script Python analyse les données de performance de joueurs dans les jeux vidéo. Il combine l'exploration de données avec la visualisation graphique pour fournir des insights business sur les joueurs, leurs plateformes et leurs performances.

## 📋 Dépendances
Le script utilise les bibliothèques suivantes :
- **pandas** : Manipulation et analyse des données
- **numpy** : Calculs numériques et matrices
- **matplotlib** : Visualisation statique (graphiques simples)
- **plotly** : Visualisation interactive (graphiques dynamiques)

## 🔧 Fonctionnalités

### 1. **Lecture des Données**
```python
df = pd.read_excel("gaming_data_2000_rows.xlsx")
```
- Charge un fichier Excel contenant 2000 lignes de données de joueurs
- Les données incluent : score, plateforme, durée de session, morts, etc.

### 2. **Exploration Initiale**
- **`df.head()`** : Affiche les 5 premières lignes du dataset
- **`df.describe()`** : Fournit des statistiques (moyenne, min, max, écart-type, etc.)

### 3. **Analyse Métier**
#### Top 3 des joueurs par score
```python
top_joueurs = df.sort_values(by='score', ascending=False).head(3)
```
- Trie les joueurs par score décroissant
- Affiche les 3 meilleurs joueurs

#### Score moyen par plateforme
```python
avg_platform = df.groupby('platform')['score'].mean()
```
- Regroupe les données par plateforme
- Calcule le score moyen pour chaque plateforme

### 4. **Création de KPI (Indicateurs Clés de Performance)**
```python
df['skill_ratio'] = df['score'] / (df['deaths'] + 1)
```
- Calcule un ratio de compétence : `Score / (Morts + 1)`
- Le +1 évite les divisions par zéro
- Crée une nouvelle colonne dans le dataset
