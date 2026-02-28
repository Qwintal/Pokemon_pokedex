# Pokémon  – Interactive Web App

## Overview
This project is an **interactive Pokémon Pokedex web application** built with Streamlit.\
It allows users to **search, filter, compare, and analyze Pokémon data** in a user-friendly interface.\
The app is designed for both casual Pokémon fans and data enthusiasts, providing insights through visualizations and comparisons.\
It also showcases how Python can be used for **data handling, visualization, and web deployment**.

## Scope:
This project focuses just on Python-based exploratory data analysis and interactive visualization.

## Features
- **Advanced Search** – Filter Pokémon by type, stats, and other attributes.
- **Compare Tool** – Compare multiple Pokémon side by side.
- **Insights Dashboard** – Visualize Pokémon distributions, top stats, and trends.
- **Game Feature** – Small interactive element for engagement.
- **View All Page** – Browse the full dataset (to be improved/removed in future updates).  

**Live Demo:** [Click Here](https://pokemon-pokedex.streamlit.app/)

## Tech Stack
- **Python** – Core programming language
- **Streamlit** – Web app deployment
- **Matplotlib** – Data visualization
- **Pandas & NumPy** – Data processing & calculations  

## Installation Guide
### Prerequisites
- Python 3.8+
- pip

### Steps
1. Clone the repository  
   ```bash
   git clone https://github.com/Qwintal/pokemon.git
   cd pokemon
   ```
2. ``` bash
   pip install -r requirements.txt
   ```
3. ``` bash
   streamlit run pokemon.py
   ```

## Future Updates
- Add up-to-date Pokémon (latest generations & forms).
- Add a Team Builder page to analyze team weaknesses and suggest improvements.

## Key Engineering Decisions
- Selected Streamlit for rapid prototyping and simplified deployment.
- Structured the application to separate data loading, filtering logic, and visualization components for maintainability.
- Structured filtering logic to support exploratory analysis rather than static reporting.
- Separated preprocessing and visualization logic to maintain modular code structure.

## Inspiration & References
[Click Here](https://pokemondb.net/)
