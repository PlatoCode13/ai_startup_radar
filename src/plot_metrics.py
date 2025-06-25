import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and sort data
df = pd.read_csv("../outputs/github_ai_startup_stats.csv")
df = df.sort_values(by="Stars", ascending=False)

# Apply styling
sns.set(style="whitegrid")
plt.rcParams.update({'font.size': 11})

# --------- GitHub Stars ---------
plt.figure(figsize=(10, 6))
df_stars = df.sort_values(by="Stars", ascending=False)
ax = sns.barplot(data=df_stars, x="Stars", y="Startup", palette="viridis")
plt.title("GitHub Stars per AI Startup")
plt.xlabel("Stars")
plt.ylabel("Startup")

for i, patch in enumerate(ax.patches):
    width = patch.get_width()
    y = patch.get_y() + patch.get_height() / 2
    ax.text(width + 1000, y, f'{int(df_stars.iloc[i]["Stars"]):,}', va='center')

plt.tight_layout()
plt.savefig("../outputs/stars_per_startup.png")
plt.close()


# --------- GitHub Forks ---------
plt.figure(figsize=(10, 6))
df_forks = df.sort_values(by="Forks", ascending=False)
ax = sns.barplot(data=df_forks, x="Forks", y="Startup", palette="rocket")
plt.title("GitHub Forks per AI Startup")
plt.xlabel("Forks")
plt.ylabel("Startup")

for i, patch in enumerate(ax.patches):
    width = patch.get_width()
    y = patch.get_y() + patch.get_height() / 2
    ax.text(width + 500, y, f'{int(df_forks.iloc[i]["Forks"]):,}', va='center')

plt.tight_layout()
plt.savefig("../outputs/forks_per_startup.png")
plt.close()

# --------- plot_stars_forks_ratio ---------
df_ratio = df[df["Forks"] > 0].copy()
df_ratio["Stars/Forks Ratio"] = df_ratio["Stars"] / df_ratio["Forks"]
df_sorted = df_ratio.sort_values("Stars/Forks Ratio", ascending=True)

plt.figure(figsize=(10, 6))
sns.barplot(data=df_sorted, x="Stars/Forks Ratio", y="Startup", palette="flare")
plt.title("Stars-to-Forks Ratio by AI Startup")
plt.xlabel("Stars / Forks")
plt.ylabel("Startup")
plt.tight_layout()
plt.savefig("../outputs/stars_forks_ratio.png")
plt.close()
