import pandas as pd
import numpy as np

# 1. Lecture du fichier Excel
df = pd.read_excel("gaming_data_2000_rows.xlsx")

# 2. Exploration
print(df.head())        # Voir les premières lignes
print(df.describe())    # Moyenne, min, max

# 3. Analyse métier : Top 3 des joueurs par score
top_joueurs = df.sort_values(by='score', ascending=False).head(3)
print("\nTop 3 joueurs :")
print(top_joueurs)

# 4. Groupement : Score moyen par plateforme
avg_platform = df.groupby('platform')['score'].mean()
print("\nScore moyen par plateforme :")
print(avg_platform)

# KPI : Key Performance Indicator
# En fr : Indicateur Clé de Performance
# 5. Calcul KPI : ratio skill
df['skill_ratio'] = df['score'] / (df['deaths'] + 1)

print("\nDataset avec skill_ratio :")
print(df)

import matplotlib.pyplot as plt
import plotly.express as px

# --- Matplotlib (Statique) ---
plt.figure(figsize=(8, 4)) # Créer une nouvelle figure avec les dimensions voulues
# plt.bar(axe x, axe y, theme)
plt.bar(df['platform'].value_counts().index, df['platform'].value_counts().values, color='green')

plt.title("Répartition des joueurs par plateforme")
plt.ylabel("Nombre de joueurs")
plt.xlabel("Plateforme")
plt.show()

# --- Plotly (Interactif) ---
# Analyse de la corrélation Score vs Temps de jeu
# Ci-dessous je créer le graphique grâce à la fonction scatter
fig = px.scatter(df, x="session_duration", y="score", 
                 size="deaths", color="platform",
                 hover_name="player_id", 
                 title="Performance des joueurs (Taille = Morts)")
fig.show()

# --- Heatmap (Activité) ---
# Simulation d'une grille 24h x 7j
activity_data = np.random.randint(0, 100, size=(7, 24))
print(activity_data)
#        0h   1h   2h  ...  23h
# Lun  [ 42,  17,  83, ...,  5 ]
# Mar  [ 61,  90,   3, ..., 44 ]
fig_heat = px.imshow(activity_data, 
                     labels=dict(x="Heure de la journée", y="Jour de la semaine", color="Joueurs Co"),
                     x=[f"{i}h" for i in range(24)],
                     # x=["0h", "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h",
                     #  "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h", "24h"],
                     y=["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"])
fig_heat.show()