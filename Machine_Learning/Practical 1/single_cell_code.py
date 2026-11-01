# Practical 1: Uber Fare Prediction
import os, numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load, engineer distance & split
path = "uber.csv" if os.path.exists("uber.csv") else "Practical 1/uber.csv"
df = pd.read_csv(path).dropna().sample(10000, random_state=42)
df["dist"] = np.hypot(df["dropoff_longitude"] - df["pickup_longitude"], df["dropoff_latitude"] - df["pickup_latitude"]) * 111
X = df[["pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude", "passenger_count", "dist"]]
y = df["fare_amount"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train & Predict
lr, rf = LinearRegression().fit(X_tr, y_tr), RandomForestRegressor(30, max_depth=8, random_state=42).fit(X_tr, y_tr)
p_lr, p_rf = lr.predict(X_te), rf.predict(X_te)

# 3. Output
print(f"Shape: {df.shape} | Train: {X_tr.shape} | Test: {X_te.shape}")
print(f"Linear Regression -> R2: {r2_score(y_te, p_lr):.3f}, RMSE: {np.sqrt(mean_squared_error(y_te, p_lr)):.3f}")
print(f"Random Forest     -> R2: {r2_score(y_te, p_rf):.3f}, RMSE: {np.sqrt(mean_squared_error(y_te, p_rf)):.3f}")
print("\nSample (Actual vs Pred):\n", pd.DataFrame({"Actual": y_te.values[:5], "LR": p_lr[:5].round(2), "RF": p_rf[:5].round(2)}))

# 4. Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
ax1.scatter(y_te[:100], p_lr[:100], alpha=0.5, color="b"); ax1.plot([0, 60], [0, 60], "--r"); ax1.set_title("Linear Reg")
ax2.scatter(y_te[:100], p_rf[:100], alpha=0.5, color="g"); ax2.plot([0, 60], [0, 60], "--r"); ax2.set_title("Random Forest")
plt.tight_layout(); plt.show()
