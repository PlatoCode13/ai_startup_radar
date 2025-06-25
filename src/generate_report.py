from fpdf import FPDF
import pandas as pd
import os

# Set correct path
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(base_dir, "outputs")
csv_path = os.path.join(output_dir, "github_ai_startup_stats.csv")

# Load data
df = pd.read_csv(csv_path)

# Plot image paths (assumed already created)
stars_img = os.path.join(output_dir, "stars_per_startup.png")
forks_img = os.path.join(output_dir, "forks_per_startup.png")
ratio_img = os.path.join(output_dir, "stars_forks_ratio.png")  # New plot

# PDF Report Generator
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI Startup Radar - GitHub Market Analysis", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 13)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def add_image(self, path, w=180):
        self.image(path, w=w)
        self.ln(10)

    def add_table(self, dataframe):
        self.set_font("Arial", size=10)
        col_width = self.w / (len(dataframe.columns) + 1)
        self.set_fill_color(240, 240, 240)

        for col in dataframe.columns:
            self.cell(col_width, 8, str(col), border=1, fill=True)
        self.ln()

        for _, row in dataframe.iterrows():
            for item in row:
                self.cell(col_width, 8, str(item), border=1)
            self.ln()
        self.ln(10)

# Build PDF
pdf = PDF()
pdf.add_page()

pdf.section_title("Overview")
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, "This report analyzes key open source signals from trending AI startups by comparing GitHub activity: stars, forks, and a normalized Stars-to-Forks ratio. It was compiled automatically as a data-driven market curiosity project.")

pdf.section_title("1. GitHub Stars")
pdf.add_image(stars_img)

pdf.section_title("2. GitHub Forks")
pdf.add_image(forks_img)

pdf.section_title("3. Stars-to-Forks Ratio")
pdf.add_image(ratio_img)

pdf.section_title("4. Tabular Overview")
pdf.add_table(df[["Startup", "Stars", "Forks", "Last Push", "Language"]])

report_path = os.path.join(output_dir, "AI_Startup_Radar_Report.pdf")
pdf.output(report_path)

print("Report saved to {report_path}")
