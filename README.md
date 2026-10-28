# RainCast — Rain Tomorrow Predictor

Logistic regression (scikit-learn) trained on 1,000 synthetic weather days:
max/min temperature, humidity at 3 PM, pressure at 9 AM, wind speed,
cloud cover, rain today.

- 5-fold CV accuracy: 76.5%, AUC: 0.85 (majority-class baseline: 50.6%)
- `train.py` trains the model and exports `model.json`
- `index.html` is a single-page demo: the same coefficients run in JavaScript,
  so the browser demo reproduces the Python model exactly — no backend needed.

Live demo: https://raincast.vercel.app

By Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University.
