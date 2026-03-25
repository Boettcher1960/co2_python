Welcome to the python_CO2_chart wiki!

# CO₂ and Climate Analysis Tool

## 42_CO2_T.py - A Comprehensive Climate Data Visualization Tool

### Overview
This Python script provides a comprehensive platform for visualizing and analyzing climate data, including CO₂ concentrations, Earth Energy Imbalance (EEI), temperature anomalies, and population trends. The tool integrates multiple datasets to create publication-quality plots with customizable parameters.

### Author
Thomas Boettcher

### Version
42t1

### Features

#### 1. CO₂ Data Visualization
- **Mauna Loa CO₂ Measurements** (1960-2025)
  - Annual mean CO₂ concentrations from NOAA
  - Blue dots visualization with data points
  
- **Glen CO₂ Model** (Quadratic Formula)
  - Formula: `0.0132251t² - 51.0337t + 49,536.7`
  - Historical CO₂ concentration modeling

- **Long-term CO₂ Data**
  - 800,000 years of ice core data
  - Our World in Data integration

#### 2. Emissions Data
- **Cumulative CO₂ Emissions** (1750-2024)
  - Multiple data modes (GtCO₂, GtC)
  - Carbon Brief and Our World in Data sources

#### 3. Earth Energy Imbalance (EEI)
- **CERES TOA Flux Data**
  - March 2000 - January 2026
  - Net TOA flux measurements
  - 12-month and 48-month running averages
  - Multiple averaging methods (centered, trailing)

#### 4. Temperature Models
- **Quadratic Temperature Model** (@reescatophuls.bsky)
  - Formula: `0.000618t² - 2.459t + 2446.058`
  
- **Earth System Sensitivity (ESS)**
  - AESS: 8°C × log₂(CO₂/280)
  - ECS: 4.5°C × log₂(CO₂/280)
  
- **GIS Temperature Data**
  - NASA GISTEMP (1880-2027)
  - Hansen linear fit (2015-2026)

#### 5. Additional Features
- **Population Data** (1960-2026)
  - UN World Population Prospects
  - Worldometers data integration
  
- **Delta CO₂ Analysis**
  - Yearly CO₂ increase calculations
  - Model comparison with quadratic fit

### Data Sources

| Dataset | Source | Time Range |
|---------|--------|------------|
| Mauna Loa CO₂ | NOAA GML | 1960-2025 |
| Glen CO₂ Model | X.com @Gergyl | 1960-2100 |
| Long-term CO₂ | Our World in Data | 800,000 years |
| Cumulative Emissions | Our World in Data | 1750-2024 |
| CERES TOA Flux | NASA | 2000-2026 |
| GIS Temperature | NASA GISTEMP | 1880-2027 |
| Population | UN WPP | 1960-2026 |

### Configuration Parameters

#### Plot Controls
```python
plot22_CO2_Mauna_Loa = 0  # 0=off, 1-3=display mode
plot23_Glen_CO2 = 0       # 0=off, 1-4=display mode
plot25_long_CO2 = 0       # 0=off, 2-4=display mode
plot34_CO2_emission = 0   # 0=off, 1-5=display mode
part41_ceres_eei = 0      # 0=off, 11-50=processing modes
part42_ceres_eei = 0      # 0=off, 1-5=display mode
plot52_delta_CO2_red_bars = 0
plot53_CO2_orange2025 = 0
plot54_Glen_delta_on = 0
plot55_population_on = 0
plot71_temperature = 0
plot72_AESS_T = 0
plot73_ECS_T = 0
plot74_GIS_T = 0
plot76_my_T = 0
Axis Configuration
python
# Left Y-axis modes
yl_mode = 4  # 2=ppm CO₂, 3=Gt CO₂, 4=EEI W/m², 5=Δppm, 7=Temperature

# Right Y-axis modes
yr_mode = 7  # 7=Temperature in °C

# Scale ranges
y_min = 250      # Min CO₂ (ppm)
y_max = 500      # Max CO₂ (ppm)
y_Tmin = 0       # Min Temperature (°C)
y_Tmax = 2.5     # Max Temperature (°C)
y_Emin = 0       # Min EEI (W/m²)
y_Emax = 2       # Max EEI (W/m²)
x_anf = 2005     # Start year
x_end = 2027     # End year
Visualization Settings
python
# Figure size
scale_mode = 10  # 7, 8, or 10 inches height

# Text positioning (bottom of figure)
tr1y = -.19   # Row 1 position
tr2y = -.26   # Row 2 position
tr3y = -.33   # Row 3 position
tr4y = -.40   # Row 4 position
tr5y = -.46   # Row 5 position
tr6y = -.57   # Row 6 position
trs = 20      # Text size
CERES Data Processing Modes
The script includes several functions for processing CERES data:

Mode	Function	Output
11	convert_ceres_to_csv()	Basic CSV conversion
12	save_with_12month_average()	12-month running average
47	create_simple_48month_average()	Simplified 48-month average
48	calculate_48month_average()	Full 48-month average
50	create_running_average_advanced()	Custom window average
Input File Structure
Required CSV Files
csv_25_ppm_long.csv - Long-term CO₂ data (Our World in Data)

csv_34a3_cumulative-co-emissions.csv - Cumulative emissions

csv_74_gis_temperature.csv - GIS temperature data

csv/csv55/csv_55_population.csv - Population data

csv/csv7/csv_75_hansen.csv - Hansen temperature fit

CERES Input Format
text
year month   data
2000 03 5.96
2000 04 1.93
2000 05 -5.93
...
Output Files
The script generates multiple CSV files:

csv_out_ceres_toa_flux.csv - Converted CERES data with decimal years

csv/csv41/csv41g12_ceres.csv - 12-month running average

csv/csv41/csv41g48_ceres.csv - 48-month running average

csv/csv41/csv41g50_ceres.csv - Advanced running average

Usage Examples
1. Plot Mauna Loa CO₂ with GIS Temperature
python
plot22_CO2_Mauna_Loa = 2
plot74_GIS_T = 4
yl_mode = 2
yr_mode = 7
2. Analyze EEI with 48-month Average
python
part41_ceres_eei = 48
plot74_GIS_T = 4
yl_mode = 4
x_anf = 2000
3. Compare Temperature Models
python
plot71_temperature = 5
plot72_AESS_T = 5
plot73_ECS_T = 5
plot74_GIS_T = 5
yl_mode = 7
Dependencies
python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import os
import sys
Installation
Clone the repository:

bash
git clone https://github.com/Boettcher1960/co2_python.git
cd co2_python
Install required packages:

bash
pip install matplotlib pandas numpy
Place data files in the appropriate directories:

csv/ - Main data files

csv/csv41/ - CERES data files

csv/csv55/ - Population data

csv/csv7/ - Temperature model data

Output Visualization
The script generates a comprehensive plot with:

Main plot area: CO₂ concentrations (blue dots) or EEI data

Right Y-axis: Temperature anomalies in °C

Grid lines: Major (50ppm) and minor (10ppm) CO₂ grids

Highlighted areas: 560ppm and 1120ppm CO₂ levels, 1.5-2.0°C temperature band

Legend lines: Up to 6 lines of explanatory text below the plot

Annotations: Data sources and parameter settings

Key Formulas
CO₂ Model (Glen)
text
CO₂ = 0.0132251t² - 51.0337t + 49536.7
Temperature Models
text
Quadratic: T = 0.000618t² - 2.459t + 2446.058
AESS: T = 8°C × log₂(CO₂/280)
ECS: T = 4.5°C × log₂(CO₂/280)
Decimal Year Calculation
text
decimal_year = year + (month - 0.5) / 12
Notes
The script automatically scales axes based on data range

Text below the plot is dynamically positioned based on active plots

CERES data processing includes both centered and trailing averages

Save PNG option creates high-resolution output (300 DPI)

The script handles large time ranges (e.g., 800,000 years of CO₂ data)

Troubleshooting
File not found errors: Ensure all required CSV files are in the correct directories

Missing columns: Check CSV format matches expected structure

Data range errors: Adjust x_anf and x_end parameters for your data

Plot too crowded: Reduce number of active plots using configuration parameters

License
Open source - feel free to use and modify for climate research and education.

Contact
GitHub: Boettcher1960/co2_python

text

This README provides comprehensive documentation for your script, including:
- Overview and features
- Data sources





































#CO2 232
Population growth is less than increase of CO2
CO2 growths more than population
41e7_CO2_T.py
28 4 2
https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mg3ncssf4s2s
https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mg3ngy3pec2s

#CO2 232 2
purple dashed CO2 line is quadratic.
green Population gets lower
blue CO2 Mauna Loa growth needs bigger Y axis????
41e8_CO2_T.py
Population growth is less than increase of CO2
https://github.com/Boettcher1960/co2_python
https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mg3po33qwc2l






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
