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