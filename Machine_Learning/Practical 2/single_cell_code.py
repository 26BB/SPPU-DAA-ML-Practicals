# Practical 2: K-Means Clustering & Elbow Method
import os, pandas as pd, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

X = pd.read_csv("sales_data_sample.csv" if os.path.exists("sales_data_sample.csv") else "Practical 2/sales_data_sample.csv", encoding="unicode_escape")[["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]].dropna()
X_s = StandardScaler().fit_transform(X)

wcss = [KMeans(k, random_state=42, n_init=10).fit(X_s).inertia_ for k in range(1, 11)]
km = KMeans(3, random_state=42, n_init=10)
X["Cluster"] = km.fit_predict(X_s)

print(f"Shape: {X.shape} | Silhouette Score: {silhouette_score(X_s, X['Cluster']):.3f}")
print("Clusters:\n", X["Cluster"].value_counts().to_string())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
ax1.plot(range(1, 11), wcss, "-ob"); ax1.plot(3, wcss[2], "*r", markersize=12, label="Elbow K=3")
ax1.set_title("Elbow Method"); ax1.legend(); ax1.grid(True)
scatter = ax2.scatter(X["QUANTITYORDERED"], X["SALES"], c=X["Cluster"], cmap="viridis", alpha=0.6)
ax2.set_title("Clusters (Qty vs Sales)"); plt.colorbar(scatter, ax=ax2)
plt.tight_layout(); plt.show()
