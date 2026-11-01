# Practical 3: KNN Classification
import os, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

df = pd.read_csv("diabetes.csv" if os.path.exists("diabetes.csv") else "Practical 3/diabetes.csv")
for c in ["Glucose", "BloodPressure", "BMI"]: df[c] = df[c].replace(0, df[df[c] != 0][c].median())
X_tr, X_te, y_tr, y_te = train_test_split(df.drop("Outcome", axis=1), df["Outcome"], test_size=0.2, random_state=42, stratify=df["Outcome"])

scaler = StandardScaler()
X_tr, X_te = scaler.fit_transform(X_tr), scaler.transform(X_te)
knn = KNeighborsClassifier(5).fit(X_tr, y_tr)
y_pr = knn.predict(X_te)

print(f"Shape: {df.shape} | Accuracy: {accuracy_score(y_te, y_pr)*100:.2f}%\n")
print(classification_report(y_te, y_pr, target_names=["Negative", "Positive"]))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
ConfusionMatrixDisplay.from_predictions(y_te, y_pr, cmap="Blues", ax=ax1, colorbar=False); ax1.set_title("Confusion Matrix")
ax2.plot(range(1, 15), [1 - accuracy_score(y_te, KNeighborsClassifier(k).fit(X_tr, y_tr).predict(X_te)) for k in range(1, 15)], "-or")
ax2.set_title("Error vs K"); ax2.grid(True)
plt.tight_layout(); plt.show()
