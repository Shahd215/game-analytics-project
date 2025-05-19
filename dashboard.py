import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Page settings
st.set_page_config(page_title="Player Analytics - Memory Match", layout="wide")

st.title("🎮 Player Performance Dashboard - Memory Match Game")

# Load data
df = pd.read_csv("player_data.csv")

# Convert 'Grid' from "4x4" to numeric value
df['Grid'] = df['Grid'].str.replace('x', '').astype(int)

# Encode 'Theme' to numeric values
label_encoder = LabelEncoder()
df['Theme_encoded'] = label_encoder.fit_transform(df['Theme'])

# Select features for clustering
X = df[['Grid', 'Theme_encoded', 'Time', 'Attempts', 'Score']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Display the dataset
st.subheader("📋 Player Data")
st.dataframe(df[['Player', 'Grid', 'Theme', 'Time', 'Attempts', 'Score', 'Cluster']])

# Scatter plot: Time vs Score colored by Cluster
st.subheader("📊 Player Clustering Based on Performance")

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='Time', y='Score', hue='Cluster', palette='Set2', s=100, ax=ax)
plt.title("Clustering of Players Based on Time and Score")
plt.xlabel("Time (seconds)")
plt.ylabel("Score (%)")
plt.grid(True)
st.pyplot(fig)

# Display recommendations based on low performance
st.subheader("🧠 Design Recommendations")

for i, row in df.iterrows():
    if row['Score'] < 75:
        st.warning(f"⚠️ {row['Player']} is struggling with Grid {row['Grid']}x{row['Grid']} and Theme '{row['Theme']}'. Consider simplifying this level.")

st.success("✅ Analysis completed. Use these insights to improve game design.")
