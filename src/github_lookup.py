import pandas as pd
import requests
from datetime import datetime

def get_github_info(repo_url):
    try:
        owner_repo = repo_url.replace("https://github.com/", "")
        api_url = f"https://api.github.com/repos/{owner_repo}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return {
                "Stars": data["stargazers_count"],
                "Forks": data["forks_count"],
                "Last Push": data["pushed_at"],
                "Language": data["language"]
            }
        else:
            print(f"Failed to fetch {repo_url}: {response.status_code}")
            return {"Stars": None, "Forks": None, "Last Push": None, "Language": None}

    except Exception as e:
        print(f"Error with {repo_url}: {e}")
        return {"Stars": None, "Forks": None, "Last Push": None, "Language": None}

# === Load CSV ===
df = pd.read_csv("ai_startup_focus_list.csv")

# === Clean Columns ===
if "Stars" in df.columns and df["Stars"].isnull().all():
    df = df.drop(columns=["Stars", "Forks", "Last Push", "Language"])

# === Apply GitHub Lookup ===
metrics = df["GitHub"].apply(get_github_info)
metrics_df = pd.DataFrame(metrics.tolist())

# === Merge Results ===
df = pd.concat([df, metrics_df], axis=1)

# === Save Clean Output ===
df.to_csv("../outputs/github_ai_startup_stats.csv", index=False)
print(" Updated and saved to outputs/github_ai_startup_stats.csv")
