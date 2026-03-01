import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analytical Insights")
st.logo("Sprits/pokeball.png")

df =pd.read_csv("pokemon.csv")

# Top 10 pokemon with higest base stats total
st.subheader("Top 10 Pokémon with Highest Base Stats Total")
top_10 = df.nlargest(10, "base_total")[["name", "base_total"]]
st.write("Here are the top 10 Pokémon based on their total base stats:")
st.dataframe(top_10)
st.markdown("""
**Interpretation:**  
These Pokémon represent the highest aggregate stat profiles in the dataset.  
They typically include legendary or pseudo-legendary species, reflecting intentional game balance design around rarity and power.
""")

# Average Base total by type
st.subheader("Average Base Total by Type")
avg_base_total = df.groupby("type1")["base_total"].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
avg_base_total.plot(kind="bar", ax=ax)
ax.set_title("Average Base Total by Type")
ax.set_ylabel("Average Base Total")
ax.set_xlabel("Type")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
st.markdown("""
**Interpretation:**  
Some primary types exhibit consistently higher average base totals.  
This suggests structural design differences between types, where certain archetypes are inherently stronger in aggregate stats.
""")

# Legendary vs Non-Legendary
st.subheader("Legendary vs Non-Legendary Base Total Comparison")
legendary = df[df["is_legendary"] == 1]["base_total"]
non_legendary = df[df["is_legendary"] == 0]["base_total"]
fig, ax = plt.subplots(figsize=(6, 6))
ax.boxplot([legendary, non_legendary], labels=["Legendary", "Non-Legendary"])
ax.set_title("Base Total Distribution")
ax.set_ylabel("Base Total")
st.pyplot(fig)
st.markdown("""
**Interpretation:**  
Legendary Pokémon show a clear upward shift in base total distribution.  
The variance also tends to be tighter, indicating deliberate power scaling within this category.
""")

# Base total by Generation 
st.subheader("Base Total Distribution by Generation")
generations = sorted(df["generation"].unique())
data = [df[df["generation"] == gen]["base_total"] for gen in generations]
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(data, labels=generations)
ax.set_title("Base Total by Generation")
ax.set_xlabel("Generation")
ax.set_ylabel("Base Total")
st.pyplot(fig)
st.markdown("""
**Interpretation:**  
Changes in distribution across generations may reflect evolving game balance philosophy.  
Later generations may introduce broader stat variance or stronger average profiles.
""")

# Correlation between height and weight
st.subheader("Correlation Between Height and Weight")
corr_hw = df["height_m"].corr(df["weight_kg"])
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["height_m"], df["weight_kg"], alpha=0.5, color="skyblue")
ax.set_xlabel("Height (meters)")
ax.set_ylabel("Weight (kg)")
ax.grid(True, linestyle="--", alpha=0.7)
st.pyplot(fig)
st.write(f"Pearson correlation coefficient: **{corr_hw:.2f}**")
st.markdown("""
**Interpretation:**  
A positive correlation here would align with real-world expectations: larger (taller) Pokémon are likely heavier due to increased mass. 
            Outliers might include lightweight tall Pokémon (e.g., flying types) or heavy short ones (e.g., rock types).
""")

# Correlation between egg steps and base total
st.subheader("Correlation Between Egg Steps and Base Total")
corr_egg = df["base_egg_steps"].corr(df["base_total"])
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["base_egg_steps"], df["base_total"], alpha=0.5, color="lightcoral")
ax.set_xlabel("Base Egg Steps")
ax.set_ylabel("Base Total")
ax.grid(True, linestyle="--", alpha=0.7)
st.pyplot(fig)
st.write(f"Pearson correlation coefficient: **{corr_egg:.2f}**")
st.markdown("""
**Interpretation:**  
In Pokémon games, egg steps often reflect a Pokémon’s rarity or power. 
            A positive correlation would suggest that stronger Pokémon (higher base total) take longer to hatch, aligning with species like legendaries or pseudo-legendaries.
            A low or negative correlation might indicate design balance or exceptions like weak Pokémon with long hatch times.
""")
