import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

rng = np.random.default_rng(42)
n = 1000
max_temp = rng.uniform(18, 42, n)
min_temp = max_temp - rng.uniform(4, 12, n)
humidity = rng.uniform(20, 100, n)
pressure = rng.uniform(990, 1025, n)
wind = rng.uniform(0, 45, n)
cloud = rng.integers(0, 9, n).astype(float)
rain_today = rng.integers(0, 2, n).astype(float)
# Generative rain logit: high humidity, low pressure, heavy cloud cover and
# rain today raise tomorrow's rain chance; hot dry days lower it.
logit = (-4.2 - 0.06*max_temp + 0.055*humidity - 0.045*(pressure - 1008)
         + 0.02*wind + 0.45*cloud + 0.9*rain_today)
p = 1/(1+np.exp(-logit))
y = (rng.random(n) < p).astype(int)
X = np.column_stack([max_temp, min_temp, humidity, pressure, wind, cloud, rain_today])
names = ["max_temp_c","min_temp_c","humidity_3pm_pct","pressure_9am_hpa","wind_speed_kmh","cloud_cover_oktas","rain_today"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu)/sd
model = LogisticRegression(max_iter=1000, C=1.0).fit(Xs, y)
kf = StratifiedKFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf)
proba_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf, method="predict_proba")[:,1]
acc = float(accuracy_score(y, pred_cv)); auc = float(roc_auc_score(y, proba_cv))
base = float(max(y.mean(), 1-y.mean()))
print(f"CV accuracy={acc:.3f} AUC={auc:.3f} rain_rate={y.mean():.3f} baseline={base:.3f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_[0].tolist(), "intercept": float(model.intercept_[0]),
      "metrics": {"cv_accuracy": acc, "cv_auc": auc, "rain_rate": float(y.mean()), "baseline_accuracy": base, "n": n}}
with open("model.json","w") as f: json.dump(mj, f, indent=1)
def predict(v):
    z = (np.array(v)-mu)/sd
    return float(1/(1+np.exp(-(model.intercept_[0] + z @ model.coef_[0]))))
samples = [[32,22,85,998,25,7,1],[38,26,35,1018,8,1,0],[28,20,90,995,30,8,1],[36,25,55,1012,12,3,0],[30,21,75,1002,18,6,0]]
for s in samples: print(s, round(predict(s),4))
