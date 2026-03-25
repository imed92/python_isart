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

### 5. **Visualisations**

#### 📊 Graphique en barres (Matplotlib)
- **Type** : Diagramme en barres statique
- **Contenu** : Répartition des joueurs par plateforme
- **Couleur** : Bleu ciel
- **Utilité** : Voir rapidement le nombre de joueurs par plateforme

#### 🎯 Nuage de points (Plotly)
- **Axes** : Durée de session (X) vs Score (Y)
- **Taille des points** : Nombre de morts
- **Couleur** : Plateforme
- **Interactivité** : Survol pour voir l'ID du joueur
- **Utilité** : Analyser la corrélation entre temps de jeu et performance

#### 🔥 Heatmap (Plotly)
- **Grille** : 7 jours x 24 heures
- **Contenu** : Nombre de joueurs connectés par heure et par jour
- **Couleur** : Gradient représentant l'activité
- **Utilité** : Identifier les pics d'activité du serveur

## 📁 Fichiers Requis
- **`gaming_data_2000_rows.xlsx`** : Fichier Excel avec les données de jeu
  - Colonnes attendues : `score`, `platform`, `session_duration`, `deaths`, `player_id`

## 🚀 Utilisation
```bash
python scriptt.py
```

Le script :
1. Charge les données du fichier Excel
2. Affiche les statistiques descriptives
3. Affiche le top 3 des joueurs
4. Affiche les scores moyens par plateforme
5. Crée la colonne `skill_ratio`
6. Affiche le dataset complet avec la nouvelle colonne
7. Ouvre 3 fenêtres de visualisation (Matplotlib et Plotly)

## 💡 Cas d'Usage
Ce script est idéal pour :
- 📈 Analyser les performances des joueurs
- 🎮 Comparer les plateformes de jeu
- 📊 Générer des rapports de performance
- 🔍 Identifier les tendances d'activité
- 🏆 Créer des classements de joueurs

## ⚠️ Notes Importantes
- Le fichier Excel `gaming_data_2000_rows.xlsx` doit être présent dans le même répertoire
- Les données de la heatmap sont générées aléatoirement (simulation)
- Les graphiques Plotly s'ouvrent dans le navigateur par défaut
