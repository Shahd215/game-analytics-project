# 🧠 Memory Match Game - Player Analytics using Machine Learning

This project analyzes player behavior from the **Memory Match HTML5** game using Python, data visualization, and machine learning (ML). It identifies gameplay patterns, classifies players into performance clusters, and generates smart design recommendations to enhance the user experience.

---

## 🎯 Project Overview

- 🎮 **Game Analyzed:** [Memory Match HTML5 on Y8](https://ar.y8.com/games/memory_match_html5)
- 🧪 **Objective:** Analyze how players perform in different game grid sizes and themes to detect difficulty levels and recommend design improvements.
- 📊 **Dashboard:** Built with Streamlit to provide an interactive and visual overview.
- 🤖 **Machine Learning:** KMeans clustering to group players based on their performance data.

---

## 🚀 Key Features

- 📥 Custom player dataset with performance stats (time, attempts, score, grid, theme)
- 📈 Clustering players by behavior using unsupervised ML (KMeans)
- ⚠️ Auto-generated design suggestions for struggling players
- 📋 Data table and 🖼️ interactive visualization via Streamlit
- 🔍 Real-time insights into time vs score patterns

---

## 📁 Project Structure
## memory-analytics
- player_data.csv # Player performance data (time, attempts, score, grid, theme)
- main.py # Python script for machine learning analysis (KMeans clustering)
- dashboard.py # Streamlit web app to visualize the data and recommendations
- requirements.txt # List of required Python libraries to run the project
- README.md # Project description, setup instructions, and documentation
- assets/ # (Optional) Folder for dashboard screenshots and visual

---

## 📷 Screenshots

### 🎯 Clustering Players by Performance
![Clustering Plot](assets/clusters.png)

### 📋 Interactive Data Table
![Data Table](assets/table.png)

> You can capture screenshots from the Streamlit app and save them in the `assets/` folder.

---

## ⚙️ Installation

To install the required libraries, use:
```
pip install -r requirements.txt
## Or install manually
pip install pandas matplotlib seaborn scikit-learn streamlit
```
---

## How to Run the Dashboard
1. Clone or download the project
-git clone https://github.com/Shahd215/game-analytics-project.git
cd game-analytics-project
2. Run the Streamlit app
-streamlit run dashboard.py ##These were used
3. Open my browser
-The app will open automatically at: http://localhost:8501

---

## 🧠 Sample Recommendation Output
⚠️ Omar is struggling with Grid 10x10 and Theme "Realistic". Consider simplifying this level.
⚠️ Yazan is struggling with Grid 8x8 and Theme "Realistic". Try adding a tutorial element.

## 🎥 Demo Video 
https://www.loom.com/share/a7326f05b9594ccdb198e76041e65efc?sid=fc4ccca9-1eb9-4a66-abc1-9007dd065475
https://www.loom.com/share/c71331d1bca3402dbace05b1dacb9999?sid=dc0db6f6-06b5-463d-a41f-4d73ba3f5ace

## 🙋 The student
👤 Shahd Majed Mlitat
🏫 Submitted for: [Ms. Zeina Saad El-Din, Artificial Intelligence and its Role in Game Programming]
📅 Date: 21 May 2025 ##It's my birthday 🙂‍↔️

