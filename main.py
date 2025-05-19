import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# 1. Load player data from CSV file
df = pd.read_csv("player_data.csv")

# 2. Convert Grid column from format "4x4" to numeric (4)
df['Grid'] = df['Grid'].str.replace('x', '').astype(int)

# 3. Encode the Theme column into numeric values
label_encoder = LabelEncoder()
df['Theme_encoded'] = label_encoder.fit_transform(df['Theme'])

# 4. Select relevant features for clustering
X = df[['Grid', 'Theme_encoded', 'Time', 'Attempts', 'Score']]

# 5. Apply KMeans clustering to group players
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# 6. Print recommendations for low-performing players
print("🔍 Recommendations:")
for i, row in df.iterrows():
    if row['Score'] < 75:
        print(f"- {row['Player']} is struggling with grid size {row['Grid']}x{row['Grid']} and theme '{row['Theme']}'. Consider simplifying this part of the game.")

# 7. Plot Time vs Score with clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Time', y='Score', hue='Cluster', palette='Set2', s=100)
plt.title("Player Performance Clustering (Time vs Score)")
plt.xlabel("Time Taken (seconds)")
plt.ylabel("Score (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
