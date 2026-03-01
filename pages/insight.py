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
Mewtwo and Rayquaza are the strongest Pokémon in the dataset, both scoring 780 — the highest possible in this list. Right behind them are Kyogre and Groudon at 770.
Most Pokémon in this top 10 are legendaries, which makes sense since they're intentionally designed to be rare and overpowered compared to regular Pokémon.
The last four spots (Tyranitar, Salamence, Metagross, and Latias) all tie at 700 — these are "pseudo-legendaries," 
meaning they're not true legendaries but still among the most powerful non-legendary Pokémon you can get.
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
Dragon-type Pokémon are the strongest on average with a base total around 520, followed closely by Steel and Psychic types.
This is no surprise — Dragon types are famously hard to obtain and are usually late-game powerhouses.
On the flip side, Bug-type Pokémon are the weakest on average, 
which matches the experience of most players since Bug types tend to be the first ones you encounter early in the game and never quite keep up later on.
Overall, the gap between the strongest and weakest types isn't massive (roughly 520 vs 380), 
but your Pokémon's type does have a noticeable impact on how strong it's likely to be.
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
Hypothesis: Legendaries are intentionally designed with a "power floor"

**Interpretation:**  
Legendary Pokémon are significantly stronger than regular ones. The typical legendary sits around a base total of 600, while the typical non-legendary is around 420. 
What's also interesting is that legendaries are more consistent — most of them cluster tightly between 580 and 680, 
meaning Game Freak deliberately keeps them in a high power bracket. 
Non-legendaries, on the other hand, are all over the place, ranging from weak early-route Pokémon all the way up to near-legendary strength. 
The two dots on the legendary side (around 200 and 400) are likely outliers like weaker legendary forms or baby legendaries.
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
Pokémon haven't gotten dramatically stronger over the generations, but there's a slight upward trend. 
Generations 1–3 hover around a median of roughly 420, while Generations 4–7 sit a bit higher, closer to 450–480. 
It's not a huge jump, but it suggests Game Freak gradually introduced slightly stronger Pokémon over time — a phenomenon fans often call "power creep."
The overall spread (weakest to strongest) stays pretty similar across all generations, 
meaning every generation still has its weak early-route Pokémon and its powerful endgame ones. 
The outlier dots at the top of Gen 1 and Gen 3 are likely the legendaries like Mewtwo and Rayquaza pulling the ceiling up.
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
Hypothesis: Pokémon type plays a bigger role in weight than height does. 

**Interpretation:**  
Taller Pokémon tend to weigh more — but it's not a strict rule. 
The correlation score of 0.63 means there's a moderate positive relationship, so height and weight do move together, just not perfectly. 
Most Pokémon are clustered in the bottom-left corner, meaning the majority are small and light. 
As height increases, weight generally goes up too, but with a lot of exceptions.
The outliers are the most interesting part. 
Some Pokémon are extremely heavy despite being short (likely bulky Rock or Steel types like Steelix or Cosmoem), 
while others are very tall but surprisingly light (likely Flying or Ghost types whose bodies aren't dense). 
The dot at 14 meters wide with only ~400kg is a great example — that's almost certainly Wailord, famously one of the largest yet lightest Pokémon, basically a giant balloon.
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
Hypothesis: Egg steps are less about balance and more about gatekeeping. 

**Interpretation:**  
Stronger Pokémon generally take longer to hatch — and the cluster at 30,000 steps makes this very obvious. 
The correlation of 0.50 means it's a moderate relationship. 
Most Pokémon hatch between 1,000–10,000 steps and span all power levels, but the standout group is the far-right column at ~30,000 steps, 
which contains almost exclusively high base total Pokémon. 
Those are almost certainly legendaries, which the game deliberately makes hardest to hatch as a way of reinforcing how rare and special they are.
The wide vertical spread in the early egg step range (left side) tells an interesting story too — low hatch times don't guarantee a weak Pokémon, 
since plenty of strong ones also hatch quickly. So while long hatch time is a good signal of a powerful Pokémon, 
a short hatch time doesn't necessarily mean weak.
""")
