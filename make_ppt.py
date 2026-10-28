from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
def slide(title, bullets, sub=None):
    s = prs.slides.add_slide(BLANK)
    t = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(1))
    t.text_frame.word_wrap = True; t.text_frame.text = title
    t.text_frame.paragraphs[0].font.size = Pt(36); t.text_frame.paragraphs[0].font.bold = True
    y = 1.6
    if sub:
        b = s.shapes.add_textbox(Inches(0.6), Inches(y), Inches(12), Inches(0.7)); b.text_frame.word_wrap=True; b.text_frame.text=sub; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.9
    for line in bullets:
        b = s.shapes.add_textbox(Inches(0.8), Inches(y), Inches(11.8), Inches(0.8)); b.text_frame.word_wrap=True; b.text_frame.text="•  "+line; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.85
    return s
slide("RainCast", ["Rain Tomorrow Predictor"], "An AI/ML project by Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University")
slide("The Problem", ["People plan travel, farming and outdoor events without knowing if it will rain tomorrow", "Weather apps show forecasts, but rarely explain which of today's conditions drive them", "A simple, transparent model makes weather prediction easy to understand and learn from"])
slide("The Solution", ["RainCast predicts tomorrow's rain chance (0–100%) from 7 of today's weather readings", "Max/min temperature, humidity at 3 PM, pressure at 9 AM, wind speed, cloud cover, rain today", "Interactive demo: change any reading, see the rain chance instantly — fully in the browser"])
slide("Tech Stack", ["Python + scikit-learn: logistic regression", "Synthetic dataset: 1,000 weather days (seed 42)", "HTML + CSS + vanilla JavaScript demo", "GitHub + Vercel hosting"])
slide("Architecture", ["Inputs: 7 weather features → standardization (train mean / std) → logistic regression → sigmoid → rain probability", "Model exported as model.json; the browser demo reproduces it exactly", "Strongest drivers: humidity, cloud cover and falling pressure"])
slide("Demo", ["Try the presets: humid stormy day, hot dry day, mild cloudy day", "Humid stormy day (85% humidity, 7 oktas cloud, rain today) → 96.7% rain chance", "Hot dry day (35% humidity, high pressure) → 1.3% rain chance"])
slide("Results", ["5-fold cross-validated accuracy = 76.5%", "AUC = 0.85 (majority-class baseline: 50.6% — about 1.5x better)", "Rain rate in training data: 49.4%", "Strongest drivers: humidity, cloud cover and pressure — matching real weather behaviour"])
slide("Future Scope", ["Train on real weather-station data for a city like Hyderabad", "Add more signals: wind direction, dew point, yesterday's pressure trend", "Show a 7-day rain outlook instead of just tomorrow", "Explain each prediction: which reading pushed the chance up or down"])
slide("Thank You", ["RainCast — will it rain tomorrow? Now you can check in seconds."], "Vikranth Reddy · github.com/HVRGAMING2705/raincast")
out = "/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_RainCast_2026-10-28.pptx"
prs.save(out); print("saved", out, "slides:", len(prs.slides._sldIdLst))
