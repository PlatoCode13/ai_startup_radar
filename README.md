# 🔍 AI Startup Radar

This project provides a lightweight and automated market scan of trending **AI startups** by analyzing their GitHub repositories. It extracts and visualizes signals like repository stars, forks, and programming language trends, and compiles a professional **PDF report** from the findings.


## 📄 Project Overview

- 📈 Scrapes and processes GitHub data from a curated list of AI startups
- 📊 Visualizes GitHub stars and forks using `seaborn` and `matplotlib`
- 🧾 Generates a clean, exportable **PDF report** with charts and tabular data
- 📁 Project structure optimized for reproducibility and modularity


## 📦 Features

| Metric              | Description                                   |
|---------------------|-----------------------------------------------|
| ⭐ GitHub Stars       | Indicates popularity and developer interest   |
| 🍴 GitHub Forks       | Reflects how often the repo is adapted        |
| 🐍 Language Trends    | Dominant languages in AI startup tooling      |


## 🗂️ File Structure

ai_startup_radar/
├── src/
│ ├── github_lookup.py # Fetches and enriches GitHub metadata
│ ├── plot_metrics.py # Generates bar charts from GitHub data
│ ├── generate_report.py # Compiles the PDF report
│ ├── ai_startup_focus_list.csv
│ └── reports/
│ └── AI_Startup_Radar_Report.pdf ✅
├── outputs/ # Automatically created during runtime
├── requirements.txt
└── README.md



## 📊 Sample Visualizations

Plots are generated automatically from the GitHub metadata.

- ![Stars per Startup](outputs/stars_per_startup_fixed.png)
- ![Forks per Startup](outputs/forks_per_startup_fixed.png)


## 📄 PDF Report

👉 You can download the full report [here](src/reports/AI_Startup_Radar_Report.pdf).


## 🔧 Installation & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run the pipeline
bash
Copy
Edit
cd src/
python github_lookup.py       # Step 1: Collect and save GitHub stats
python plot_metrics.py        # Step 2: Generate bar plots
python generate_report.py     # Step 3: Build the final PDF report
```
🧠 Motivation
This project is built for data curiosity and market awareness, useful for:

Trendspotters in AI

Investors tracking open-source traction

Competitive analysts

✅ Requirements
See requirements.txt

💡 Credits
Created by Zhimon – feel free to fork or adapt this pipeline for other tech sectors (e.g., Robotics, BioTech, LLMs).