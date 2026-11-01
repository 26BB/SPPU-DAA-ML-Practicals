# Practical 4: Artificial Neural Network (MLP)
import os, warnings, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
warnings.filterwarnings("ignore")

df = pd.read_csv("Churn_Modelling.csv" if os.path.exists("Churn_Modelling.csv") else "Practical 4/Churn_Modelling.csv").drop(["RowNumber", "CustomerId", "Surname"], axis=1)
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)
X_tr, X_te, y_tr, y_te = train_test_split(df.drop("Exited", axis=1), df["Exited"], test_size=0.2, random_state=42, stratify=df["Exited"])

scaler = StandardScaler()
X_tr, X_te = scaler.fit_transform(X_tr), scaler.transform(X_te)
mlp = MLPClassifier((16, 8), max_iter=250, random_state=42).fit(X_tr, y_tr)
y_pr = mlp.predict(X_te)

print(f"Data: {df.shape} | Accuracy: {accuracy_score(y_te, y_pr)*100:.2f}% | Epochs: {mlp.n_iter_}\n")
print(classification_report(y_te, y_pr, target_names=["Retained", "Churned"]))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
ax1.plot(mlp.loss_curve_, color="darkorange"); ax1.set_title("Loss Curve"); ax1.grid(True)
ConfusionMatrixDisplay.from_predictions(y_te, y_pr, cmap="Oranges", ax=ax2, colorbar=False); ax2.set_title("ANN Confusion Matrix")
plt.tight_layout(); plt.show()
