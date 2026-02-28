Welcome to the python_CO2_chart wiki!

start Visual Studio Code
open folder with Visual Studio Code
open file 41d_CO2_T master.py
run
a CO2 chart is produced as png
Here is your GitHub-ready README.md version — clean Markdown, structured, and ready to paste into your repository.

📈 CO₂ & Temperature Chart (1960–2025)
Python visualization of atmospheric CO₂ concentrations (Mauna Loa) with optional overlays for:

📊 Yearly CO₂ growth (delta bars)

👤 World population

🧮 Modeled CO₂ curves

🌡 Temperature projection

Repository:
👉 https://github.com/Boettcher1960/python_CO2_chart

📌 Overview
This script generates a customizable dual-axis (and optional triple-axis) chart showing:

Annual mean CO₂ concentration (ppm)

Modeled CO₂ curves (quadratic fit)

Year-to-year CO₂ increase

World population trend (optional)

Temperature projection (optional)

Primary time range: 1960–2025

The script is designed for experimentation, visualization, and comparison of atmospheric CO₂ trends.

🛠 Requirements


pip install matplotlib pandas numpy

Python 3.9+ recommended.

▶️ How to Run


python3 "41d_CO2_T master.py"

⚙️ Plot Configuration
At the top of the script, you can enable or disable plot elements using flags:

Variable | Description | Values -- | -- | -- plot1_Mauna_Loa_ | Main CO₂ curve | 0 = off, 1 = on plot3_delta_CO2_red_bars | Yearly CO₂ increase bars | 0 = off, 1 = on Kurve2_population_on | World population overlay | 0 = off, 1 = on plot4_CO2_orange2025 | Quadratic CO₂ model curve | 0 = off, >0 = on Kurve5_Glen_delta_on | Difference curve (actual − model) | 0 = off plot6_Glen_CO2_on | Additional modeled CO₂ curve | 0 = off plot7_temperature | Temperature projection | 0 = off
Example:



plot1_Mauna_Loa_ = 1
plot3_delta_CO2_red_bars = 1
plot7_temperature = 4

📊 Data Sources
CO₂ Data
Annual mean CO₂ values (ppm) from Mauna Loa Observatory (NOAA).

Included directly in the script:



co2_values1 = [316.91, 317.64, 318.45, ..., 424.61, 428.26]

Population Data (Optional)
Loaded from a CSV file (e.g. population4.csv) containing world population in billions.

Temperature Model
The script includes a quadratic approximation:



0.000617965091650558*t² - 2.45858656778789*t + 2446.05792853123

Used to illustrate projected temperature trends.

📐 Mathematical Models Used
CO₂ Quadratic Model


CO₂(t) = 0.0132251 * t² - 51.0337 * t + 49536.7

Used to:

Compare real vs modeled CO₂

Plot difference curves

Project forward trend

🖼 Output Example
The script produces:

Left Y-Axis → CO₂ concentration (ppm)

Optional Right Y-Axis → Population or temperature

Optional bar chart → Annual CO₂ increase

Configurable grid and tick spacing

Multiple axis support via matplotlib.twinx()

📁 File Structure


41d_CO2_T master.py
population4.csv  (optional)
README.md

🔍 How It Works (Execution Flow)
Import libraries (matplotlib, pandas, numpy)

Set configuration flags

Define year range

Load CO₂ values

Build Pandas DataFrame

Create Matplotlib figure and axes

Plot selected curves/bars

Format axes, ticks, legends

Show final visualization

🎯 Purpose
This project is intended for:

Climate data visualization

CO₂ trend analysis

Comparing measured vs modeled curves

Educational demonstration of long-term atmospheric change

📜 License
Add your preferred license here (MIT recommended for open use).

If you'd like, I can also:

Add badges (Python version, license, etc.)

Create a clean project banner image

Refactor your script into a modular version

Convert it into a Streamlit web app 🌍

<textarea class="wcDTda_fallbackTextarea" name="prompt-textarea" autofocus="" placeholder="Stelle irgendeine Frage" data-virtualkeyboard="true"></textarea>
