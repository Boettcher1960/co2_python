# 41m9_CO2_T.py 
# Thomas Boettcher
# part 1 configure 
# part 2 plot CO2 Mauna Loa
# part 3 plot3_Glen_CO2 = 3
#
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
#
# part 71 plot temperature with right y axis
# part 72 plot temperature ECS = 7.7°C with right y axis
# part 73 plot temperature ECS = 4.5°C with right y axis
#
# part 8 print headline in figue
# part 9 print line 1 to 5 below the figure 

# -----------------------------
# part 1 configure  variables
# -----------------------------
# 1.1 imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import os
import sys

# 1.2 Parameter decide which curves to plot
plot1_CO2_Mauna_Loa = 2 # 2 print in line 2 # 0 no plot CO2 # 1 Mauna Loa 
c1 = "blue" # plot1 color
plot3_Glen_CO2 = 3 # 3 print in line 3, 0 keine Kurve Glen , 1 = 0.013t² - 51t + 49,536 in rot  
c3 = "green" # plot3_Glen_CO2 color
c3 = "#4554A8C6"
# c3 = "#4B3FD1"
# no part 4
plot52_delta_CO2_red_bars = 0 # 3 4 0 7 8 keine delta_CO2 , 1 = delta_CO2 in rot , 7,8 mit Beschriftung   
plot53_CO2_orange2025 = 0 # 3, 4, 0 orange Glen , 1 = 0.013t² - 51t + 49,536 in rot 3 works plot53_CO2_orange2025
plot54_Glen_delta_on = 0 #  4, 0 print row 4 # green Glen diff print in line 4
plot55_population_on = 0 # 5 row 5 # 0=no print , 1 = population in green
# no part 6
plot71_temperature = 0 # 5,4, 0
c71 = "red" # plot7 color
plot72_AESS_T= 4 # 5,0 apparent Earth system sensitivity (AESS=7.7°C)
c72 = "orange" # plot72 color
plot73_ECS_T= 5 # 4.5 #  Earth Climate sensitivity (ECS=4.5°C)
c73 = "#2AC99E84" # plot73 color
parameter84_save_png = 8 # save png

# 1.3.1 scale the left Y axis
y_min = 300 # 300 # min value 280
y_max = 1300 # 1300 # min value 440 70

# 1.3.2 scale the right Y axis
y_Tmin = 0 # min value °C
y_Tmax = 20 # 4 # max value C

x_anf = 1960 # 1960 2000 
x_end = 2200 # 2200 2026 

ydiff = (y_max - y_min) / 10 # for y axis scale print
xdiff = (x_end - x_anf) / 10 # for legend print

scale_mode = 10 # 0 7 8 10 hansen 10
# -----------------------------
# 1.4 Plot (x-width, y-width) Size of the figure in inches 
# -----------------------------
y_grid_CO2 = 10
if scale_mode == 7:
   fig, ax1 = plt.subplots(figsize=(13, 7))
elif scale_mode == 8:
   fig, ax1 = plt.subplots(figsize=(13, 8))
elif scale_mode == 10:
   fig, ax1 = plt.subplots(figsize=(13, 10))
   y_grid_CO2 = 50
else:
   fig, ax1 = plt.subplots(figsize=(13, 7))


# 1.4.5 scale the text rows below the plot field
tr1x = -0.09 # text row 1 x value -.3...1 -0.12
tr1y = -.16 # text row 1 y end value -.3...1 -.15
tr2x = 0.01 # text row 2 x value -.3...1 -0.08
tr2y = -.24 # text row 2 y end value -.3...1 -.24

# 1.5 scale the text rows below the plot field
tr3y = -.32 # text row 1 y end value -.3...1 -.32
tr4y = -.40 # text row 1 y end value -.3...1 -.40
tr5y = -.48 # text row 1 y end value -.3...1 -.48
tr6y = -.56 # text row 1 y end value -.3...1 -.56
trs = 20 # trs = 16 # fontsize=14

# 1.6 scale the legend lines below the plot field
lr2x1 = 0.065 # line row 2 x value begin 0.065
lr2x2 = 0.085 # line row 2 x value end 0.085
lr2y = 0.215 # line row 2 y value begin 0.215
lr3y = 0.17 # line row 3 y value begin 0.17
lr4y = 0.124 # line row 4 y value begin 0.124
lr5y = 0.078 # line row 5 y value begin 0.08

# 1.7 scale the right y axis
yr0=ydiff/8
yr0 = int(yr0+0.49) # cast to integer result = 2 (int)
yr1=ydiff-yr0
yr1=4
yr1 = int(yr1+0.49) # cast to integer result = 2 (int)

# 1.8 Parameter strig
header_parameter = f"{plot1_CO2_Mauna_Loa}" # 1960 number inside string
header_parameter = header_parameter + f"{plot3_Glen_CO2} " # plot55_population_on number inside string

header_parameter = header_parameter + f"{plot52_delta_CO2_red_bars} " # plot52_delta_CO2_red_bars number inside string
header_parameter = header_parameter + f"{plot53_CO2_orange2025}" # plot53_CO2_orange2025 number inside string
header_parameter = header_parameter + f"{plot54_Glen_delta_on}" # plot54_Glen_delta_on number inside string
header_parameter = header_parameter + f"{plot55_population_on}" # plot55_population_on number inside string

header_parameter = header_parameter + f"{plot71_temperature}" 
header_parameter = header_parameter + f"{plot72_AESS_T}" 
header_parameter = header_parameter + f" {plot73_ECS_T} " 
header_parameter = header_parameter + f"{parameter84_save_png} " 
# header_parameter = f" parameter= {plot1_CO2_Mauna_Loa}" # 1960 number inside string
# end part 1

# -----------------------------
#  part 2 plot CO2 Mauna Loa
# -----------------------------
# 2.1 years 1960–2025
years21 = list(range(1960, x_end))

# 2.1.2 Select only 2018–2025
if x_anf < 1960:
   start = years21.index(1960)
else:
   start = years21.index(x_anf)    
end = years21.index(2025) + 1
years21_subset = years21[start:end]


# -----------------------------
# 2.2 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# https://gml.noaa.gov/ccgg/trends/mlo.html
# https://gml.noaa.gov/ccgg/trends/global.html
# -----------------------------
co2_values1 = [
316.91, 317.64, 318.45, 318.99, 319.62, 320.04, 321.38, 322.16, 323.04, 324.62, # 1960–1969
325.68, 326.32, 327.46, 329.68, 330.19, 331.13, 332.03, 333.84, 335.41, 336.84, # 1970–1979
338.76, 340.12, 341.48, 343.15, 344.87, 346.35, 347.61, 349.31, 351.69, 353.20, # 1980–1989
354.45, 355.70, 356.54, 357.21, 358.96, 360.97, 362.74, 363.88, 366.84, 368.54, # 1990–1999
369.71, 371.32, 373.45, 375.98, 377.70, 379.98, 382.09, 384.02, 385.83, 387.64, # 2000–2009
390.10, 391.85, 394.06, 396.74, 398.81, 401.01, 404.41, 406.76, 408.72, 411.66, # 2010–2019
414.24, # 2020
416.41, # 2021
418.53, # 2022
421.08, # 2023 421.08
424.61, # 2024
428.26 # 2025 = 424.61 + 3.69 ppm
]
# 2.2 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_clobal.txt
# 2.2.2 world data not found
# https://gml.noaa.gov/ccgg/trends/global.html

# 2.3 subset skip the old years
co2_values1_subset = co2_values1[start:end]
df = pd.DataFrame({
"Jahr": years21_subset,
"CO2": co2_values1_subset
})


# 2.4.1 add more space below plot
fig.subplots_adjust(bottom=0.30) # 0.25 = 25% margin at bottom
# 2.4.2 print blue Mauna Loa
ax1.plot(df["Jahr"], df["CO2"], marker="o", markersize=5, color="blue", linewidth=2, label=" ")
ax1.set_xlabel("year", fontsize=16 )
plt.xticks(fontsize=16)
# write "CO₂ in ppm" left Axis upwards
ax1.set_ylabel("CO₂ in ppm", color=c1, fontsize=20) # y achse links
# 2.6 write the numbers left of plot field
ax1.tick_params(axis="y", labelcolor=c1, labelsize=20) # Achsenbeschriftung
ax1.grid(True)

# 2.7 scale the Y value 280 ppm to 440 ppm y_grid_CO2 = 20
if scale_mode == 10:
   ax1.set_ylim(y_min, y_max)
   ax1.yaxis.set_major_locator(MultipleLocator(100))   # Hauptstriche
   ax1.yaxis.set_minor_locator(MultipleLocator(20))    # Nebenstriche
   ax1.tick_params(axis='y', which='major', length=12, width=1.5)
   ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')
   # 2.8 scale the X value time = 20
   ax1.xaxis.set_major_locator(MultipleLocator(20))   # Hauptstriche
   ax1.tick_params(axis='x', which='major', length=12, width=2) # all 2 years
   ax1.xaxis.set_minor_locator(MultipleLocator(10))   # Nebenstriche
   ax1.tick_params(axis='x', which='minor', length=4,  width=1)
   # ax1.grid(True, which="major", color="darkblue", alpha=1) # big net 20 ppm
   ax1.grid(True, which="minor", color="lightblue", alpha=0.64)
   # Separate horizontal and vertical grid lines
   for line in ax1.get_xgridlines():   # vertical lines
       line.set_color('grey')            # vertical color
       line.set_alpha(0.9)
       line.set_linestyle('-')         # optional '--'
       line.set_linewidth(1.3)   # <-- thickness
   for line in ax1.get_ygridlines():   # horizontal lines
       line.set_color('blue')           # horizontal color
       line.set_alpha(0.4)
       line.set_linestyle('-')          # optional
       line.set_linewidth(1.1)   # <-- thickness
   y_block = (y_max - y_min) / y_grid_CO2  # 120 / 20 = 6 y_block
else:
  ax1.set_ylim(y_min, y_max)
# end part 2 Mauna Loa

# -----------------------------
# 3.1 Kurve6 Jahre 1960–3025
# -----------------------------
# CO₂ Funktion
def co3_ppm(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7

# 3.2 Jahre von 1960 bis 3000
years3 = np.arange(x_anf, x_end +1 )
co3_values = co3_ppm(years3)

# -- 3.3. Create DataFrame for convenience
df3 = pd.DataFrame({
"Year3": years3,
"Modeled3": co3_values
})
# 3.4
if plot3_Glen_CO2 > 0:
   ax3 = ax1.twinx()
   ax3.spines.right.set_position(("outward", 90))
   ax3.spines["right"].set_visible(False) # remove right y-Achse
   ax3.tick_params(right=False, labelright=False) # remove Zahlen
# 3.5
if plot3_Glen_CO2 > 0:
   ax3.plot(df3["Year3"], df3["Modeled3"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c3, linewidth=3)
   ax3.tick_params(axis="y", labelcolor="green")
   ax3.set_ylim(y_min, y_max) # scale
   ax3.spines.right.set_position(("outward", 60))
# end part 3

# no part 4

# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# 5.2.2 ΔCO₂ berechnen (per pandas) Balken
# df["CO2"].diff() Calculates the difference between consecutive CO₂ values
# -----------------------------
if plot52_delta_CO2_red_bars > 0:
   df["Delta_CO2"] = df["CO2"].diff().fillna(0)  # This line creates a new column in your DataFrame called Delta_CO2.
   ax52 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax52.spines.right.set_position(("outward", 20))
# 5.2.5
if plot52_delta_CO2_red_bars > 0:
   bars = ax52.bar(df["Jahr"], df["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.bar(df["Jahr"], df["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.set_ylabel("red bars Mauna Loa CO2 increase in ppm", color="red", fontname="Arial",fontsize=16) # fontweight="bold"
   ax52.tick_params(axis="y", labelcolor="red", labelsize=16)
   ax52.set_ylim(-yr0, yr1) # scale y axis3 right red

# 5.2.8 Add numbers on top of delta CO2 bars
if plot52_delta_CO2_red_bars > 6:
   ax52.bar_label(bars, fontsize=8, fontname="Arial",padding=1, color="black")

# part 5.3 plot53_CO2_orange2025
# part 5.3.1 -- Quadratic model function
def co53_model(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7

# 5.3.2 Kurve4 . Real Mauna Loa CO₂ annual data 1960–2023
# 2025 = 424.61 + 3.69 ppm = 428.26
data53 = {
1960: 316.91, 1961: 317.64, 1962: 318.45, 1963: 318.99, 1964: 319.62,
1965: 320.04, 1966: 321.37, 1967: 322.18, 1968: 323.05, 1969: 324.62,
1970: 325.68, 1971: 326.32, 1972: 327.46, 1973: 329.68, 1974: 330.19,
1975: 331.12, 1976: 332.03, 1977: 333.84, 1978: 335.41, 1979: 336.84,
1980: 338.76, 1981: 340.12, 1982: 341.48, 1983: 343.15, 1984: 344.85,
1985: 346.35, 1986: 347.61, 1987: 349.31, 1988: 351.69, 1989: 353.20,
1990: 354.45, 1991: 355.70, 1992: 356.54, 1993: 357.21, 1994: 358.96,
1995: 360.97, 1996: 362.74, 1997: 363.88, 1998: 366.84, 1999: 368.54,
2000: 369.71, 2001: 371.32, 2002: 373.45, 2003: 375.98, 2004: 377.70,
2005: 379.98, 2006: 382.09, 2007: 384.02, 2008: 385.83, 2009: 387.64,
2010: 390.10, 2011: 391.85, 2012: 394.06, 2013: 396.74, 2014: 398.87,
2015: 401.01, 2016: 404.41, 2017: 406.76, 2018: 408.72, 2019: 411.66, # 2025 = 424.61 + 3.69 ppm
2020: 414.24, 2021: 417.41, 2022: 418.52, 2023: 421.24, 2024: 424.61 , 2025: 428.26
}
years53 = np.array(list(data53.keys()))
# 5.3.4
co53_actual = np.array(list(data53.values()))
co53_modeled = co53_model(years53)
# 5.3.5 Calculate difference (actual minus model)
difference53 = co53_actual - co53_modeled
# 5.3.6 Create DataFrame for convenience
df53 = pd.DataFrame({
"Year": years53,
"Actual": co53_actual,
"Modeled": co53_modeled,
"Difference": difference53
})
# 5.3.7
if plot53_CO2_orange2025 > 0:
   ax53 = ax1.twinx()
   ax53.tick_params(labelright=False) # removes the right-side numbers
   ax53.set_ylabel("") # removes the axis label
# 5.3.8 Legende oben links
if plot53_CO2_orange2025 > 0:
   ax53.plot(df53["Year"], df53["Modeled"], '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
   ax53.set_ylim(y_min, y_max) # scale glen curve same as Mauna loa
   ax53.spines.right.set_position(("outward", 90))

# part 5.4 plot54_Glen_delta_on
# 5.4 difference Mauna Loa minus Glen_CO2
# 5.4.2 print y axis 5 on right side Twin axis for difference
if plot54_Glen_delta_on > 0:
   ax54 = ax1.twinx()
   ax54.bar(df53["Year"], df53["Difference"], color="green", alpha=0.4, label="Diff (Actual − Model)")
   ax54.set_ylabel(
      "Difference Mauna Loa - Glen-parabol (ppm)  (plot 5)",
      color="green",
      fontsize=14,
      labelpad=-4   # smaller = closer to axis
      )

   ax54.tick_params(axis="y", labelcolor="green")
   #ax54.set_ylim(-1, 13) # scale
   ax54.set_ylim(-yr0, yr1) # scale
   if plot54_Glen_delta_on > 2:
      ax54.spines.right.set_position(("axes", 1))


# part 5.5 plot55_population_on human earth population 
# 5.5.1 population up to 2023 (UN WPP 2024 via OWID)
# url = "https://ourworldindata.org/grapher/population.csv"
# population4.csv
# -----------------------------
# 5.5.2 population 2023 to 2026 
# https://www.worldometers.info/world-population/world-population-by-year/
# 2026	8,300,678,395	0.84%	69,065,325	56
# 2025	8,231,613,070	0.85%	69,640,498	55
# 2024	8,161,972,572	0.87%	70,237,642	55
# 2023	8,091,734,930	0.88%	70,327,738	54
# population1.csv

if plot55_population_on > 0:
   pop_df = pd.read_csv("population1.csv")
   pop_world = (
         pop_df[pop_df["Entity"] == "World"][["Year", "Population"]]
         .query("1960 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
      )
   pop_world_subset = pop_world[start:end]
   # 5.5.4 in Milliarden
   pop_world["Population_Mrd"] = pop_world["Population"] / 1e9
   #end plot55_population_on=1 - print population

# 5.5.5 plot55_population_on=1
if plot55_population_on > 0:
   ax55 = ax1.twinx()
   ax55.spines.right.set_position(("outward", 50))
   ax55.set_ylabel("Earth Population in Billion", color="green")
   # 2.5 Legende oben links
   ax55.plot(pop_world["Year"], pop_world["Population_Mrd"], marker="s", color="green", label="Earth Population in Billion K2")
   ax55.set_ylabel("Earth Population in Billion", color="green")
   ax55.tick_params(axis="y", labelcolor="green")
   # ax55.set_ylim(1, 9) #8
   ax55.set_ylim(4, 9)
   #end print_y2=1 - print population

if plot55_population_on == 2: ax55.set_ylim(6.5, 8.5) # andere Skala
#end 5.5.9 plot55_population_on=1 - print population




# 7 part 1
# 7.1 plot71_temperature @reescatophuls.bsky.social
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
def T_model71(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123

# 7.1.2 years scale x axis
years71 = np.arange(x_anf, x_end + 1 )
T_71values = T_model71(years71)

# -- 7.1.4. Create DataFrame for convenience
df7 = pd.DataFrame({
"Year71": years71,
"Modeled71": T_71values
})

# 7.1.6 plot71_temperature
if plot71_temperature > 0:
   ax71 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax71.plot(df7["Year71"], df7["Modeled71"], '--', label="T formula CO2=  K6", color=c71, linewidth=3)
   ax71.tick_params(axis="y", labelcolor=c71)
   ax71.set_ylim(y_Tmin, y_Tmax) # scale
   Tax1 = 2 # 0.1))   # Hauptstriche
   Tax55 = 0.2 # 0.1))   # Nebenstriche
   ax71.yaxis.set_major_locator(MultipleLocator(Tax1))   # Hauptstriche
   ax71.yaxis.set_minor_locator(MultipleLocator(Tax55))   # Nebenstriche
   ax71.set_ylim(y_Tmin, 3 ) # scale
  
# 7.1.7 plot71 Achse und Beschriftung
if plot71_temperature > 0:
   if plot54_Glen_delta_on > 2:
      ax71.spines.right.set_position(("outward", 50))
   else:
      ax71.spines.right.set_position(("outward", 5))
   ax71.set_ylabel (
         "Δ Temperature in °C ",
         color=c71,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
   )
   ax71.tick_params(axis="y", labelcolor=c71, labelsize=20)

# 7.1.8 plot71_temperature
if plot71_temperature > 0:
   ax71.set_ylim(y_Tmin, y_Tmax) # scale
   ax71.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.25, zorder=0) # color="lightblue" 2°C streifen
   ax71.axvspan(2024, 2026, color="#B3D9FF", alpha=0.25, zorder=0) # vertical bar'

# plot72_AESS_T= 4 # apparent Earth system sensitivity (AESS=7.7°C)
# 7.2 plot72_AESS_T # dT=ECS*log2(C/C0) # T560ppm=AESS*log2(560/280) 
# AESS=7.7°C  # (Judd 2024)
# https://www.science.org/doi/10.1126/science.adk3705) 
# 2025
# https://www.annualreviews.org/content/journals/10.1146/annurev-earth-032320-064209
#
def T_model72(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   C0=280
   log2_value = np.log2(CO2/C0)
   AESS=7.7 # apparent Earth system sensitivity (AESS=7.7°C)
   temp72=AESS * log2_value
   return temp72

# 7.2.2 years scale x axis
years72 = np.arange(x_anf, x_end + 1 )
T_72values = T_model72(years72)

# -- 7.2.4. Create DataFrame for convenience
df72 = pd.DataFrame({
"Year72": years72,
"Modeled72": T_72values
})

# 7.2.6 plot72_temperature
if plot72_AESS_T > 0:
   ax72 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax72.plot(df72["Year72"], df72["Modeled72"], '--', label="T formula CO2=  K72", color=c72, linewidth=3)
   ax72.tick_params(axis="y", labelcolor=c72)
   ax72.set_ylim(y_Tmin, y_Tmax) # scale
   Tax1 = 5 # 0.1))     # Hauptstriche
   Tax55 = 1 # 0.1))   # Nebenstriche
   ax72.yaxis.set_major_locator(MultipleLocator(Tax1))   # Hauptstriche
   ax72.yaxis.set_minor_locator(MultipleLocator(Tax55))  # Nebenstriche
   ax72.set_ylim(y_Tmin, 3 ) # scale
   ax72.minorticks_off()

# 7.2.7 plot7 Achse und Beschriftung if plot71_temperature > 0:
if plot72_AESS_T > 0 and plot71_temperature < 1:
   if plot54_Glen_delta_on > 2:
      ax72.spines.right.set_position(("outward", 50))
   else:
      ax72.spines.right.set_position(("outward", 5))
   ax72.set_ylabel (
         "Δ Temperature calc72 in  °C ",
         color=c72,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
   )
   ax72.tick_params(axis="y", labelcolor=c72, labelsize=20)

# 7.2.8 plot72_temperature
if plot72_AESS_T > 0:
   ax72.set_ylim(y_Tmin, y_Tmax) # scale
   ax72.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.25, zorder=0) # color="lightblue" 2°C streifen
   ax72.axvspan(2024, 2026, color="#B3D9FF", alpha=0.25, zorder=0) # vertical bar'
   ax1.axhspan(1118, 1122, color="green", alpha=0.25, zorder=0)      # 1120 ppm horicontal stripe
   ax1.axhspan(558, 562, color="green", alpha=0.25, zorder=0)        # 560 ppm horicontal stripe
   ax72.axvspan(2068, 2069, color="green", alpha=0.25, zorder=0) # vertical bar'
   ax72.axvspan(2177, 2178, color="green", alpha=0.25, zorder=0) # vertical bar'
   ax72.minorticks_off()

# plot73_ECS_T Earth Climate sensitivity 
# 7.3  dT=ECS*log2(C/C0) # T560ppm=ECS*log2(560/280) 
# 
def T_model73(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   C0=280
   log2_value = np.log2(CO2/C0)
   # AESS=7.7 # apparent Earth system sensitivity (AESS=7.7°C)
   ECS = 4.5
   temp73 = ECS * log2_value
   return temp73

# 7.3.2 years scale x axis
years73 = np.arange(x_anf, x_end + 1 )
T_73values = T_model73(years73)
# 7.3.4. Create DataFrame for convenience
df73 = pd.DataFrame({
"Year73": years73,
"Modeled73": T_73values
})

# 7.3.6 plot_ax73_temperature
if plot73_ECS_T > 0:
   ax73 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax73.tick_params(axis="y", labelcolor=c73)
   ax73.set_ylim(y_Tmin, y_Tmax) # scale
   Tax1 = 1 # 0.1))    # Hauptstriche
   Tax55 = 0.2 # 0.1))   # Nebenstriche
   ax73.yaxis.set_major_locator(MultipleLocator(Tax1))   # Hauptstriche
   ax73.yaxis.set_minor_locator(MultipleLocator(Tax55))   # Nebenstriche
   ax73.set_ylim(y_Tmin, y_Tmax ) # scale
   ax73.minorticks_off()

# Teil 8.1 plot
plt.xlim(x_anf, x_end)

# 8.2 headline part print ablove the plot aerea
# 8.2.1 blue headline part
trs = 20
# header_black = f"CO2 concentration in the atmosphere {x_anf}" # 1960 number inside string
if plot71_temperature > 0: # one temperature active
   # 8.2.3 plot the headline
   # plt.text(-0.1, 1.05, header, color="blue", fontname="Arial", fontsize=18, transform=plt.gca().transAxes)
   plt.text(-0.1, 1.05,
     f"{x_anf}   CO2 Mauna Loa",    # f"More CO2 in atmosphere", 
     color="blue", fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.24, 1.05,
     f"- - CO2 quadratic",
     color=c3, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.48, 1.05,
     f"--> Δ Temperature calculated °C year {x_end}",
    color=c71, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
else:   
   header = f"CO2 measured at Mauna Loa up to 2024. Print {x_anf}" # 1960 number inside string
   header = header + f" to {x_end} " # 2026 number inside string
   # 8.3.3 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
            


# 9 part 9 print information below the plot field
# 9 part 9 print information below the plot field
trs = 20
# 9 part 9 print information below the plot field
# 9.1 print line 1 the text below the figure tr1x = -0.09 # tr1y = -.16 
filename = os.path.basename(sys.argv[0])
text_below1 = ""
# text_below1 = text_below1 + header_parameter
text_below1 = text_below1 + "Figure from "
text_below1 = text_below1 + filename
plt.text(-0.1, tr1y, text_below1, color="black", fontname="Arial", fontsize=trs,
         transform=plt.gca().transAxes)

# 9.2 print line 1 blue Mauna Loa data below the figure
# 9.2 print line 2 below the plot explainations
if plot1_CO2_Mauna_Loa == 3: # 8.5.1 legende world data plot1_CO2_Mauna_Loa
   K1_text=" 2 new text )"
   plt.text(tr2x, tr2y, K1_text, color="blue", fontname="Arial", fontsize=18,
   transform=plt.gca().transAxes)
   # elif plot1_CO2_Mauna_Loa == 1:
else: # 9.2.2 draw bue line as legend
   line1 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color="blue", linewidth=2)
# 9.2.3 draw bue line as legend
fig.add_artist(line1)
# 9.2.4 write blue text
blue_text="Blue line: CO2 measured at Mauna Loa ( 2025 = 424.61ppm + 3.69 ppm )"
# 9.2.5 plot the blue text
plt.text(tr2x, tr2y, blue_text, color="blue", fontname="Arial", fontsize=trs,
transform=plt.gca().transAxes)

# 9.3 print line 3 below the plot explainations
# 9.3.2 print line 3 plot55_population_on marker="s"
if plot55_population_on == 3: # 8.5.1 legende world data plot1_CO2_Mauna_Loa
   line1 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line1)
   # 9.5.4 write blue text
   blue_text="Green line: Earth Population in billion"
   # 9.5.5 plot the blue text
   plt.text(tr2x, tr3y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.3 print line 3 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot52_delta_CO2_red_bars == 3 or plot52_delta_CO2_red_bars == 7:
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write red text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.2.5 plot the red text
   plt.text(tr2x, tr3y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.4 work_ print line 3 orange Glen data below the figure
elif plot53_CO2_orange2025 == 3: # print in line 3 up to 2025
   line3 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line3)
   # 9.2.4 write blue text
   red_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr3y, red_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
# 9.3.5  print line 3 green Glen 
elif plot54_Glen_delta_on == 3: # print in line4
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.3.5 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.5 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.3.5 plot the green text
   plt.text(tr2x, tr3y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.6_ print line 3 red Glen data below the figure
# 9.3.6  print line 6 red Glen 
if plot3_Glen_CO2 == 3: # print in line 3
   line6 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c3, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line6)
   # 9.2.4 write blue text
   red_text="green dashed @gergyl.bsky atmosphere ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   # c3 = "#4B3FD1"
   plt.text(tr2x, tr3y, red_text, color=c3, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3 end print line 3 below the plot explainations


# 9.4 print line 4 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.4.2 print line 4 plot55_population_on marker="s"
if plot55_population_on == 4:
   line1 = Line2D([lr2x1, lr2x2], [lr4y, lr4y],
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   fig.add_artist(line1)
   blue_text="Green line: Earth Population in billion"
   plt.text(tr2x, tr4y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.4.3 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
if plot52_delta_CO2_red_bars == 4 or plot52_delta_CO2_red_bars == 8:
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.4 work_ print line 4 orange Glen data below the figure
if plot53_CO2_orange2025 == 4: # print in line 3 up to 2025
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot54_Glen_delta_on == 4: # print in line4
   line5 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line5)
   # 9.2.4 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.6_ print line 3 red Glen data below the figure
elif plot3_Glen_CO2 == 4: # print in line 3
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c3, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red_text=" dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color=c3, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot71_temperature == 4:
   line7 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.4.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.4.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   red_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 4:
   line72 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   red72_text="AESS_T apparent Earth sys sensitivity=7.7°C*log2(CO2/C0)"
   # 9.5.8 plot the text
   plt.text(tr2x, tr4y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)


# 9.5.2 print line 5 plot55_population_on marker="s"
if plot55_population_on == 5: # 8.5.1 legende world data plot1_CO2_Mauna_Loa
   line1 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line1)
   # 9.5.4 write blue text
   blue_text="Green line: Earth Population in billion"
   # 9.5.5 plot the blue text
   plt.text(tr2x, tr5y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot71_temperature == 5:
   line7 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.5.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.5.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   red_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
   # 9.5.7 plot the blue text
   plt.text(tr2x, tr5y, red_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 5:
   line72 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   red72_text="AESS_T apparent Earth sys sensitivity=7.7°C*log2(CO2/C0)"
   # 9.5.8 plot the text
   plt.text(tr2x, tr5y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
else: # 9.5.9 draw bue line as legend
   plt.text(tr2x, tr5y, "Line 5 -0.48", color="white", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
if plot73_ECS_T > 0:
   line73 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text 
   if plot72_AESS_T == 5:
      red73_text="ECS=4.5°C*log2(CO2/C0)"
      plt.text(0.72, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
      transform=plt.gca().transAxes)
   else:            
       red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0)"
       plt.text(tr2x, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)


# 9.5 print line 5 plot55_population_on
# 9.6 print line 6
text6 = f" CO2_min= {y_min}ppm " # y_max number inside string
text6 = text6 + f" CO2_max= {y_max} " # y_max number inside string
text6 = text6 + f"  T_max= {y_Tmax}°C    Parameter=" # y_max number inside string
text6 = text6 + header_parameter

# 9.6 plot line 6
plt.text(-0.12, -.56, text6 , color="black", fontname="Arial", fontsize=trs,
    transform=plt.gca().transAxes)
fig.tight_layout()
plt.tight_layout()
plt.show()

# 9.7 save the plot line 6
if parameter84_save_png > 0:
   filename = ""
   filename2 = os.path.basename(__file__) # "1234test.py"
   # take only the first 5 characters
   first5 = filename2[:parameter84_save_png]
   filename = filename + first5
   filename = filename + "_"
   filename = filename + header_parameter
   filename = filename + str(x_end)
   #path = f"/Users/thomasboettcher/Desktop/python/{filename}"
   #fig.savefig(path, dpi=300, bbox_inches="tight")
   path = f"/Users/thomasboettcher/documents/Python/4_Python_CO2/41_CO2_T.png"
   fig.savefig(path, dpi=300, bbox_inches="tight")
# 9.9 close the plotted figure
plt.close(fig)

# 7.9 KurveX – Global annual temperature anomaly (°C, relative to baseline)
dataT79 = {
1880: -0.16, 1881: -0.08, 1882: -0.10, 1883: -0.17, 1884: -0.28,
1885: -0.33, 1886: -0.31, 1887: -0.36, 1888: -0.18, 1889: -0.11,
1890: -0.35, 1891: -0.22, 1892: -0.27, 1893: -0.31, 1894: -0.30,
1895: -0.23, 1896: -0.11, 1897: -0.11, 1898: -0.27, 1899: -0.17,
1900: -0.09,
# …
2000:  0.42, 2001:  0.54, 2002:  0.63, 2003:  0.62, 2004:  0.54,
2005:  0.67, 2006:  0.63, 2007:  0.66, 2008:  0.54, 2009:  0.64,
2010:  0.71, 2011:  0.59, 2012:  0.63, 2013:  0.66, 2014:  0.74,
2015:  0.87, 2016:  1.00, 2017:  0.92, 2018:  0.85, 2019:  0.98,
2020:  1.02, 2021:  0.85, 2022:  0.89, 2023:  1.18
}
yearsT79 = np.array(list(dataT79.keys()))
tempsT79 = np.array(list(dataT79.values()))




"""
# Load the annual GISTEMP data
url = "https://datahub.io/core/global-temp/r/annual.csv"
df = pd.read_csv(url)

# Inspect the first rows
print(df.head())

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Mean"], marker="o")
plt.title("Global Annual Temperature Anomalies (GISTEMP)")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(True)
plt.show()
"""
# 8.4 legende Mauna Loa blau plot1_CO2_Mauna_Loa
if plot1_CO2_Mauna_Loa > 6: # 8.5.1 legende world data plot1_CO2_Mauna_Loa
   K1_text=" Blue: CO2 measured at Mauna Loa ( 2025 = 424.61ppm + 3.69 ppm )"
   plt.text(0.02, 0.95, K1_text, color="blue", fontname="Arial", fontsize=16,
   transform=plt.gca().transAxes)
   ax1.plot([x_anf+1, x_anf +2], [y_max -5, y_max -5], marker="o", markersize=5, color="blue", linewidth=2, label="short line")
# 8.5 plot55_population_on = 1 # 0 keine Bevölkerung , 1 = Bevölkerung in grün
if plot1_CO2_Mauna_Loa > 8:
   if plot55_population_on > 0:
      plt.text(0.02, 0.90,"green: Human Population in billion K2", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
# 8.6 legende
if plot1_CO2_Mauna_Loa > 8:
   if plot52_delta_CO2_red_bars > 0:
      plt.text(0.02, 0.86," red bars: Mauna Loa yearly increase. //see right larger ppm scaling", color="red", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -21, y_max -21], marker="_", markersize=5, color="red", linewidth=8)
# 8.7 legende '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
if plot1_CO2_Mauna_Loa > 8:
   if plot53_CO2_orange2025 > 0:
      plt.text(0.02, 0.80," orange: Glen formula ppm = 0.0132 t² - 51 t + 49,536 ", color="orange", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -30.5, y_max -30.5], marker="_", markersize=5, color="orange", linewidth=3)
# 8.8 legend in the plot
if plot1_CO2_Mauna_Loa > 8:
   if plot54_Glen_delta_on > 0:
      plt.text(0.02, 0.29," green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -52, y_max -52], marker="_", markersize=5, color="green", linewidth=8)
# 8.9 legend in the plot
if plot1_CO2_Mauna_Loa > 8:
   if plot3_Glen_CO2 > 0:
      plt.text(0.02, 0.85," Red: Glen formula ppm = 0.0132251t² - 51.0337t + 49,536", color="red", fontname="Arial", fontsize=16,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -12, y_max -12], marker="_", markersize=5, color="red", linewidth=3)


# Datenquellen:
# CO₂: Mauna-Loa/NOAA Jahresmittel (bis 2023), 2024/2025 vorläufig/Schätzung wie zuvor verwendet.
# https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# ppm CO2 = 0.0132251t² - 51.0337t + 49,536.7

