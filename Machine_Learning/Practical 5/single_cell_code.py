# Practical 5: Spam Detection (KNN vs SVM)
import os, warnings, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
warnings.filterwarnings("ignore")

df = pd.read_csv("emails.csv" if os.path.exists("emails.csv") else "Practical 5/emails.csv")
X_tr, X_te, y_tr, y_te = train_test_split(df.drop(["Email No.", "Prediction"], axis=1), df["Prediction"], test_size=0.2, random_state=42, stratify=df["Prediction"])

scaler = StandardScaler()
X_tr, X_te = scaler.fit_transform(X_tr), scaler.transform(X_te)
p_knn = KNeighborsClassifier(5).fit(X_tr, y_tr).predict(X_te)
p_svm = LinearSVC(dual=False, random_state=42).fit(X_tr, y_tr).predict(X_te)

a_knn, a_svm = accuracy_score(y_te, p_knn), accuracy_score(y_te, p_svm)
print(f"Data: {df.shape} | KNN Acc: {a_knn*100:.2f}% | SVM Acc: {a_svm*100:.2f}%\n")
print("SVM Classification Report:\n", classification_report(y_te, p_svm, target_names=["Ham", "Spam"]))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))
ax1.bar(["KNN", "SVM"], [a_knn*100, a_svm*100], color=["steelblue", "crimson"]); ax1.set_ylim(70, 100); ax1.set_title("Accuracy %")
ConfusionMatrixDisplay.from_predictions(y_te, p_knn, cmap="Blues", ax=ax2, colorbar=False); ax2.set_title("KNN")
ConfusionMatrixDisplay.from_predictions(y_te, p_svm, cmap="Reds", ax=ax3, colorbar=False); ax3.set_title("SVM")
plt.tight_layout(); plt.show()
