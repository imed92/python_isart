import pandas as pd

df = pd.read_excel("Exercice_Pandas_Analyse.xlsx", sheet_name="ventes_jeux", header=1)

# ── PARTIE 1 — Chargement & découverte ──────────────────────────

# Q1 - Chargement (déjà fait ci-dessus)

# Q2 - 5 premières lignes
print("Q2 — 5 premières lignes :")
print(df.head())

# Q3 - Dimensions
print("\nQ3 — Dimensions :")
print(df.shape)  # (15, 6)

# Q4 - Statistiques générales
print("\nQ4 — Statistiques générales :")
print(df.describe())

# ── PARTIE 2 — Exploration ───────────────────────────────────────

# Q5 - Plateformes sans doublons
print("\nQ5 — Plateformes disponibles :")
print(df["plateforme"].unique())

# Q6 - Nombre de joueurs par plateforme
print("\nQ6 — Joueurs par plateforme :")
print(df["plateforme"].value_counts())

# Q7 - Joueurs sur PS5
print("\nQ7 — Joueurs sur PS5 :")
print(df[df["plateforme"] == "PS5"])

# Q8 - Joueurs avec score > 5000
print("\nQ8 — Joueurs avec score > 5000 :")
print(df[df["score"] > 5000])

# ── PARTIE 3 — Calculs ───────────────────────────────────────────

# Q9 - Score moyen
print("\nQ9 — Score moyen :")
print(df["score"].mean())

# Q10 - Score max et min
print("\nQ10 — Score max et min :")
print("Max :", df["score"].max())
print("Min :", df["score"].min())

# Q11 - Score moyen par plateforme
print("\nQ11 — Score moyen par plateforme :")
print(df.groupby("plateforme")["score"].mean())

# Q12 - Total heures jouées par jeu
print("\nQ12 — Total heures jouées par jeu :")
print(df.groupby("jeu")["heures_jouees"].sum())

# ── PARTIE 4 — Nouvelles colonnes ────────────────────────────────

# Q13 - skill_ratio
df["skill_ratio"] = df["score"] / (df["morts"] + 1)
print("\nQ13 — Colonne skill_ratio ajoutée :")
print(df[["joueur", "score", "morts", "skill_ratio"]])

# Q14 - niveau
df["niveau"] = pd.cut(
    df["score"],
    bins=[0, 2000, 6000, 9999],
    labels=["Débutant", "Intermédiaire", "Expert"]
)
print("\nQ14 — Colonne niveau ajoutée :")
print(df[["joueur", "score", "niveau"]])

# ── PARTIE 5 — Tri & classement ──────────────────────────────────

# Q15 - Top 3 par score
print("\nQ15 — Top 3 par score :")
print(df.sort_values("score", ascending=False).head(3)[["joueur", "score"]])

# Q16 - Top 3 par skill_ratio
print("\nQ16 — Top 3 par skill_ratio :")
print(df.sort_values("skill_ratio", ascending=False).head(3)[["joueur", "skill_ratio"]])

# Q17 - Sauvegarder
df.to_excel("resultats.xlsx", index=False)
print("\nQ17 — Fichier resultats.xlsx sauvegardé ✅")