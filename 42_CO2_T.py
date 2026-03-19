# 42_CO2_T.py 
v = "42d2" # 
# Thomas Boettcher
# part 1 configure 
# part 2.2 plot CO2 Mauna Loa
# part 2.3 plot23_Glen_CO2 = 3
#
# part 3.4 plot34_CO2_emission summed
#
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
#
# part 71 plot temperature with right y axis
# part 72 plot temperature ECS = 8°C with right y axis
# part 73 plot temperature ECS = 4.5°C with right y axis
#
# part 8 print headline, axis numbers. around figue
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
plot22_CO2_Mauna_Loa = 2 # 1, 2 print in line 2 # 0 no plot CO2 # 1 Mauna Loa 
c22 = "blue" # plot1 color
plot23_Glen_CO2 = 3 # 2, 3 print in line 2, 3, 0 keine Kurve Glen , 1 = 0.013t² - 51t + 49,536 in dark blue  
c23 = "#4554A8C6"   # c23 = "#4B3FD1"

plot25_long_CO2 = 3 # 2, 3 print -800 000 years ppm CO2 file
# https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data

plot34_CO2_emission = 43 # 34 row3 mode 4, 42 row 4 mode 2   cumulative CO2 emissions 1750 to 2024
c34 = "purple"
c34 = "#942296C5" 
# no part 4
plot52_delta_CO2_red_bars = 0 # 8 0 7 4 keine delta_CO2 , 1 = delta_CO2 in rot , 7,8 mit Beschriftung   
plot53_CO2_orange2025 = 0 # 3, 4, 0 orange Glen , 1 = 0.013t² - 51t + 49,536 in rot 3 works plot53_CO2_orange2025
plot54_Glen_delta_on = 0 #  4, 0 print row 4 # green Glen diff print in line 4
plot55_population_on = 0 # 4, 5 row 5 # 0=no print , 1 = population in green
# no part 6
plot71_temperature = 0 # 4,5, 0 quadratic T
plot72_AESS_T= 0      # 4,5,0 apparent Earth system sensitivity (AESS=7.7°C)
plot73_ECS_T= 0       # 6,5 #  Earth Climate sensitivity (ECS=4.5°C)
parameter84_save_png = 8 # save png

c71 = "red" # plot71 color c71 = "green" 
if plot71_temperature < 1:    c72 = "red" # plot72 color
else:                         c72 = "#DD3646A3" # plot72 color
if plot71_temperature < 1 and plot72_AESS_T < 1:
   c73 = "red" # plot73 color
else:   
   c73 = "#B9184E84" # plot73 color
   c73 = "orange"

C280=280 # CO2 concentration 1750 275 ppm

# 1.3.1 scale the left Y axis
y_min = 280 # 300 # min value 280
y_max = 480 # 1300 # min value 440 70

# 1.3.2 scale the right Y axis
y_Tmin = 0 # min value °C
y_Tmax = 5 # 4 # max value C

x_anf = -2000 # 1960 2000 -33000
x_end = 2050 # 2200 2026 

# 1.4.5 scale the text rows below the plot field
tr1x = -0.09 # text row 1 x value -.3...1 -0.12
tr2x = 0.01 # text row 2 x value -.3...1 -0.08

tr1y = -.19 # text row 1 y end value -.3...1 -.15
tr2y = -.26 # text row 2 y end value -.3...1 -.24
# 1.5 scale the text rows below the plot field
tr3y = -.33 # text row 1 y end value -.3...1 -.32
tr4y = -.40 # text row 1 y end value -.3...1 -.40
tr5y = -.48 # text row 1 y end value -.3...1 -.48
tr6y = -.56 # text row 1 y end value -.3...1 -.56
trs = 20 # trs = 16 # fontsize=14

# 1.6 scale the legend lines below the plot field
lr2x1 = 0.065 # line row 2 x value begin 0.065
lr2x2 = 0.085 # line row 2 x value end 0.085
lr1y = 0.248 # line row 1 y value begin 
lr2y = 0.211 # line row 2 y value begin 0.215
lr3y = 0.168 # line row 3 y value begin 0.17
lr4y = 0.129 # line row 4 y value begin 0.124
lr5y = 0.082 # line row 5 y value begin 0.08
lr6y = 0.034 # line row 6 y value begin 0.08

# 1.7 Plot (x-width, y-width) Size of the figure in inches
scale_mode = 10 # 10 inches high. 13 inches wide
if scale_mode == 7:
   fig, ax1 = plt.subplots(figsize=(13, 7))
elif scale_mode == 8:
   fig, ax1 = plt.subplots(figsize=(13, 8))
elif scale_mode == 10:
   fig, ax1 = plt.subplots(figsize=(13, 10))
else:
   fig, ax1 = plt.subplots(figsize=(13, 7))

# yr1 = int(yr1+0.49) # cast to integer result = 2 (int)

# 1.8 Parameter strig
header_parameter = f"{plot22_CO2_Mauna_Loa}" # 1960 number inside string
header_parameter = header_parameter + f"{plot23_Glen_CO2}" # 
header_parameter = header_parameter + f"{plot34_CO2_emission} " # 

header_parameter = header_parameter + f"5({plot52_delta_CO2_red_bars}" # plot52_delta_CO2_red_bars number inside string
header_parameter = header_parameter + f"{plot53_CO2_orange2025}" # plot53_CO2_orange2025 number inside string
header_parameter = header_parameter + f"{plot54_Glen_delta_on}" # plot54_Glen_delta_on number inside string
header_parameter = header_parameter + f"{plot55_population_on}" # plot55_population_on number inside string

header_parameter = header_parameter + f" 7({plot71_temperature}" 
header_parameter = header_parameter + f"{plot72_AESS_T}" 
header_parameter = header_parameter + f"{plot73_ECS_T} " 
# header_parameter = header_parameter + f"{parameter84_save_png} " 
# end part 1


# -----------------------------
#  part 2   plot CO2 
#  part 2.2 plot CO2 Mauna Loa
blue22_text="blue dots: CO2 measured at Mauna Loa ( 2025 = 427.35 ppm ) 22"
# -----------------------------
# 2.2.1 years 1960–2025 x_years_22_list = [1960, 1961, 1962, ..., x_end - 1]
if x_end > 1961:
   x_years_22_list = list(range(1960, x_end+1)) # list of years 1960...
else:
   x_years_22_list = list(range(1960, 2026)) # list of years 1960...

# 2.2.2 Select only 2018–2025
if x_anf < 1960:
   start_of_x_index = x_years_22_list.index(1960)
else:
   start_of_x_index = x_years_22_list.index(x_anf)    
if x_end > 2025:
   end_of_x_index = x_years_22_list.index(2025)
elif x_end < 1960:
   end_of_x_index = 1
else:
   end_of_x_index = x_years_22_list.index(x_end)

x_years_22_list_subset = x_years_22_list[start_of_x_index:end_of_x_index]
# -----------------------------
# 2.2.3 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# https://gml.noaa.gov/ccgg/trends/mlo.html
# https://gml.noaa.gov/ccgg/trends/global.html
# -----------------------------
co2_values22 = [
316.91, 317.64, 318.45, 318.99, 319.62, 320.04, 321.38, 322.16, 323.04, 324.62, # 1960–1969
325.68, 326.32, 327.46, 329.68, 330.19, 331.13, 332.03, 333.84, 335.41, 336.84, # 1970–1979
338.76, 340.12, 341.48, 343.15, 344.87, 346.35, 347.61, 349.31, 351.69, 353.20, # 1980–1989
354.45, 355.70, 356.54, 357.21, 358.96, 360.97, 362.74, 363.88, 366.84, 368.54, # 1990–1999
369.71, 371.32, 373.45, 375.98, 377.70, 379.98, 382.09, 384.02, 385.83, 387.64, # 2000–2009
390.10, 391.85, 394.06, 396.74, 398.81, 401.01, 404.41, 406.76, 408.72, 411.66, # 2010–2019
414.24, # 2020
416.41, # 2021
418.53, # 2022
421.08, # 2023
424.61, # 2024
427.35  # 2025 = 427.35  ppm
]
# 2.2.4 Kurve1 CO₂ 
#  https://gml.noaa.gov/webdata/ccgg/trend_of_x_indexs/co2/co2_annmean_mlo.txt
# 2.2.4 Mauna_Loa 13.3.2026
# plot22_CO2_Mauna_Loa https://gml.noaa.gov/ccgg/trends/global.html
# 2.2.5 subset skip the old years
co2_values22_subset = co2_values22[start_of_x_index:end_of_x_index]
df2 = pd.DataFrame({  # make a DataFrame with two columns:"x_22_years" → years (x-axis) "y_22_CO2_ppm" → CO₂ values (y-axis)
     "x_22_years": x_years_22_list_subset,
     "y_22_CO2_ppm": co2_values22_subset })
# 2.2.6 add more space below plot
fig.subplots_adjust(bottom=0.30) # 0.25 = 25% margin at bottom

# end part 2.2 Mauna Loa CO2 measurements


# -----------------------------
# 2.3 plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
# source a plot with the formula explained in a thread
# source https://x.com/Gergyl/status/1810632238230589564
# -----------------------------
# text_plot23_Glen="blue dashed @gergyl.bsky atmosphere ppm = 0.0132251t² - 51.0337t + 49,536"
text_plot23_Glen="calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"
# CO₂ function CO2 = 0.013t² - 51t + 49,536
def co3_ppm(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7
# 2.3.2 years as x values 1960 to 3000
years23 = np.arange(x_anf, x_end +1 )
co23_values = co3_ppm(years23)
# 2.3.3. Create DataFrame for convenience
df23 = pd.DataFrame({
      "Year3": years23,
      "Modeled3": co23_values
       })
# 2.3.4 assign ax1  
if plot22_CO2_Mauna_Loa > 0:
   ax1.plot(df2["x_22_years"], df2["y_22_CO2_ppm"], marker="o", markersize=5, color="blue", linewidth=2, label=" ")
elif plot23_Glen_CO2 > 0:
   ax1.plot(df23["Year3"], df23["Modeled3"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c23, linewidth=3)
# 2.3.7
if plot23_Glen_CO2 > 0:
   ax23 = ax1.twinx()
   ax23.spines.right.set_position(("outward", 90))
   ax23.spines["right"].set_visible(False) # remove right y-Achse
   ax23.tick_params(right=False, labelright=False) # remove Zahlen
# 2.3.8
if plot23_Glen_CO2 > 0:
   ax23.plot(df23["Year3"], df23["Modeled3"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c23, linewidth=3)
   ax23.tick_params(axis="y", labelcolor="green")
   ax23.set_ylim(y_min, y_max) # scale
   ax23.spines.right.set_position(("outward", 60))
# end part 2.3 CO2


# plot25_long_CO2 = 3 # 2, 3 print -800 000 years ppm CO2 file
# https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data
# Data sources: NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026)EPA 
# based on various sources (2022) – with major processing by Our World in Data
# -----------------------------
#  part 2.5 plot CO2 Mauna Loa
blue25_text="blue: CO2 measured at Mauna Loa ( 2025 = 427.35 ppm ) 22"
if plot25_long_CO2 > 0:
      df25 = pd.read_csv("csv_25_ppm_long.csv") # our world in data file
      long_co25 = (
         df25[df25["Entity"] == "World"][["Year25", "ppm25"]]
         .query("-10 <= Year25 <= 2026")
         .sort_values("Year25")
         .reset_index(drop=True)
         )
print(long_co25.head(5))

# part 3.4 plot34_CO2_emission summed
# co2_cumul.csv
# https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
# 3.4.0 Entity,Code,Year,Cumulat
#       World,OWID_WRL,1750,9305937
if plot34_CO2_emission > 0:
   print34_text ="purple dots: cumulative CO2 emissions Carbon Brief 34 mode "
   # plot34_CO2_emission_mode = 1, read self made csv 2000 GtCO2
   # plot34_CO2_emission_mode = 2, read csv 2000 000 000 000 tCO2
   # plot34_CO2_emission_mode = 3, read csv 2000 GtCO2 csv_34a3_cumulative-co-emissions.csv 1750 to 2024
   # plot34_CO2_emission_mode = 4, read csv 2000 GtCO2
   # plot34_CO2_emission_mode = 5
   first_digit = int(str(plot34_CO2_emission)[0]) # print in row
   second_digit = int(str(plot34_CO2_emission)[1])
   plot34_CO2_emission = first_digit
   plot34_CO2_emission_mode = second_digit
   print34_text = print34_text + str(plot34_CO2_emission_mode)
   # 3.4.mode 1 
   if plot34_CO2_emission_mode == 1:
      df34a = pd.read_csv("csv_34a1_co2_world_generated.csv") # processed file
   elif plot34_CO2_emission_mode == 2:   # 3.4.mode 2
      df34b = pd.read_csv("csv_34a2_co2_sum.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year34", "Cumulat"]]
         .query("1960 <= Year34 <= 2026")
         .sort_values("Year34")
         .reset_index(drop=True)
         )
      # 3.4.2 in Gt CO2
      co2_sum_world["GCumulat"] = co2_sum_world["Cumulat"] / 1e9
      print("co2_cumul 2  df34b")
      print(co2_sum_world.head(2))
   elif plot34_CO2_emission_mode == 3:  # 3.4.mode 3
      df34b = pd.read_csv("csv_34a3_cumulative-co-emissions.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year", "Cumulat"]]
         .query("1750 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
         )
      # 3.4.3 in Gt CO2
      co2_sum_world["GCumulat"] = (co2_sum_world["Cumulat"] / 1e9).astype(int)
      x34years = df34b["Year"]
      cumulative_gt = co2_sum_world["GCumulat"]
   elif plot34_CO2_emission_mode == 4:  # 3.4.mode 5
      df34b = pd.read_csv("csv_34a3_cumulative-co-emissions.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year", "Cumulat"]]
         .query("1750 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
         )
      # 3.4.4 in Gt C    round GCumulat to integer
      co2_sum_world["CCumulat"] = (co2_sum_world["Cumulat"] / 1e9 * 12 / 44 )
      x34_year = df34b["Year"]
      y_sum_gt = co2_sum_world["CCumulat"]
   else:  # 3.4.mode 9
      df34b = pd.read_csv("co2_cumul.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year34", "Cumulat"]]
         .query("1960 <= Year34 <= 2026")
         .sort_values("Year34")
         .reset_index(drop=True)
         )
      # print("plot34_CO2_emission_mode 0  df34b")
      # print(co2_sum_world.head(10))
      # 3.4.4 in Gt CO2
      co2_sum_world["GCumulat"] = co2_sum_world["Cumulat"] / 1e9
      print(co2_sum_world.head(2))
      #   Year34       Cumulat   GCumulat
      # 0    1960  308396160000  308.39616
      # 1    1961  317811160000  317.81116
      # how to save co2_sum_world with column GCumulat as csv file
      # save CSV
      # co2_sum_world.to_csv("co2_sum_world.csv", index=False)
      #end 3.4

# no part 4

# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# 5.2.2 ΔCO₂ berechnen (per pandas) Balken
# df2["CO2"].diff() Calculates the difference between consecutive CO₂ values
# -----------------------------
if plot52_delta_CO2_red_bars > 0:
   df2["Delta_CO2"] = df2["CO2"].diff().fillna(0)  
   # This line creates a new column in your DataFrame called Delta_CO2.
   ax52 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
# growth data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt

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
2015: 401.01, 2016: 404.41, 2017: 406.76, 2018: 408.72, 2019: 411.66, 
2020: 414.24, 2021: 416.41, 2022: 418.53, 2023: 421.08, 2024: 424.61 , 2025: 427.35 
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
      "Difference Mauna Loa - Glen-parabol (ppm)  (plot 54)",
      color="green",
      fontsize=14,
      labelpad=-4   # smaller = closer to axis
      )
   ax54.tick_params(axis="y", labelcolor="green")
   #ax54.set_ylim(-1, 13) # scale
   ax54.set_ylim(-yr0, yr1) # scale
   ax54.set_ylim(0, 4) # scale
   if plot54_Glen_delta_on > 2:
      ax54.spines.right.set_position(("axes", 1))
   # end 5.4


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
# 5.5.3 read csv_55_population.csv
if plot55_population_on > 0:
   green55_text="Green line: Earth Population in billion"
   df55 = pd.read_csv("csv_55_population.csv")
   pop_world = (
         df55[df55["Entity"] == "World"][["Year", "Population"]]
         .query("1960 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
      )
   # 5.5.4 in Milliarden
   pop_world["Population_Mrd"] = pop_world["Population"] / 1e9
# 5.5.5 plot55_population_on=1
if plot55_population_on > 0:
   ax55 = ax1.twinx()
   #end 5.5. plot55_population_on

# no part 6

# 7 part 1
# red71_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
red71_text="red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C"
# 7.1 plot71_temperature @reescatophuls.bsky.social
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
def T_model71(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
# 7.1.2 years scale x axis
years71 = np.arange(x_anf, x_end + 1 )
T_71values = T_model71(years71)
# 7.1.3. Create DataFrame for convenience
df7 = pd.DataFrame({
      "Year71": years71,
      "Modeled71": T_71values })
# 7.1.4 plot71_temperature
if plot71_temperature > 0:
   ax71 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax71.plot(df7["Year71"], df7["Modeled71"], '--', label="T formula CO2=  K6", color=c71, linewidth=3)
   ax71.tick_params(axis="y", labelcolor=c71)
   ax71.set_ylim(y_Tmin, y_Tmax) # scale
# end 7.1 


# plot72_AESS_T= 4 # apparent Earth system sensitivity (AESS=7.7°C)
red72_text="AESS_T Apparent Earth System Sensitivity = 8°C * log2(CO2/C0)"
# 7.2 plot72_AESS_T # dT=ECS*log2(C/C0) # T560ppm=AESS*log2(560/280) 
# AESS=7.7°C  # (Judd 2024)
# https://www.science.org/doi/10.1126/science.adk3705) 
# 2025
# https://www.annualreviews.org/content/journals/10.1146/annurev-earth-032320-064209
#
def T_model72(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   log2_value = np.log2(CO2/C280)
   AESS=8 # apparent Earth system sensitivity (AESS=7.7°C)
   temp72=AESS * log2_value
   return temp72
# 7.2.2 years scale x axis
years72 = np.arange(x_anf, x_end + 1 )
T_72values = T_model72(years72)
# 7.2.3. Create DataFrame for convenience
df72 = pd.DataFrame({
       "Year72":      years72,
       "Modeled72": T_72values })
# 7.2.4 plot72_temperature
if plot72_AESS_T > 0:
   ax72 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax72.plot(df72["Year72"], df72["Modeled72"], '--', label="T formula CO2=  K72", color=c72, linewidth=3)
   ax72.tick_params(axis="y", labelcolor=c72)
   ax72.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.2 plot72_AESS_T


# plot73_ECS_T Earth Climate sensitivity 
# 7.3  dT=ECS*log2(C/C0) # T560ppm=ECS*log2(560/280) 
# 
def T_model73(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   log2_value = np.log2(CO2/C280)
   ECS = 4.5
   temp73 = ECS * log2_value
   return temp73

# 7.3.2 years scale x axis
years73 = np.arange(x_anf, x_end + 1 )
T_73values = T_model73(years73)
# 7.3.4. Create DataFrame for convenience
df73 = pd.DataFrame({
       "Year73": years73,
       "Modeled73": T_73values })
# 7.3.6 plot_ax73_temperature
if plot73_ECS_T > 0:
   ax73 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax73.tick_params(axis="y", labelcolor=c73)
   ax73.set_ylim(y_Tmin, y_Tmax) # scale
   

# part 8
# 8.1 scale the plot area
# 8.2 print the headline above the plot
# 8.3 print the left y axis 
# 8.4 print the vertical lines CO2=constant
# 8.5 print the right y axis
# 8.6 print the x axis 
# 8.7 print the horizontal lines year 2026

# 8.1 scale the plot area
# 8.1.2 scale the x axis
plt.xlim(x_anf, x_end)
# 8.1.3 scale the Y axis
ax1.set_ylim(y_min, y_max)
# 8.1.4 enable grid
ax1.grid(True)

# 8.2 print the headline above the plot
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
     color=c23, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.48, 1.05,
     f"--> Δ Temperature calculated °C year {x_end}",
    color=c71, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
else:   
   header = f"CO2 measured at Mauna Loa up to 2024. Print {x_anf}" # 1960 number inside string
   header = header + f" to {x_end} " # 2026 number inside string
   # 8.2.8 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
            # end 8.2


# 8.3 print the left y axis 
# 8.3.1 write "CO₂ in ppm" left Axis upwards
ax1.set_ylabel("CO₂ in ppm", color=c22, fontsize=20) # y achse links
# 8.3.2 write the numbers left of plot field
ax1.tick_params(axis="y", labelcolor=c22, labelsize=20) # Achsenbeschriftung
# 8.3.3 scale the left Y axis
if y_max - y_min < 11:
   y_mayor_ticks = 2
   y_minor_ticks = 0.2
elif y_max - y_min < 21:
   y_mayor_ticks = 5
   y_minor_ticks = 1
elif y_max - y_min < 50:
   y_mayor_ticks = 10
   y_minor_ticks = 2
elif y_max - y_min < 101:
   y_mayor_ticks = 20
   y_minor_ticks = 2
elif y_max - y_min < 201:
   y_mayor_ticks = 40
   y_minor_ticks = 5
elif y_max - y_min < 500:
   y_mayor_ticks = 50
   y_minor_ticks = 10
elif y_max - y_min < 1100:
   y_mayor_ticks = 100
   y_minor_ticks = 20
   y_minor_grid  = 10
elif y_max - y_min < 3100:
   y_mayor_ticks = 500
   y_minor_ticks = 100
   y_minor_grid  = 10
elif y_max - y_min < 5100:
   y_mayor_ticks = 1000
   y_minor_ticks = 200
else: 
   y_mayor_ticks = 200 # Hauptstriche y axis
   y_minor_ticks = 50
# 8.3.5  scale the right Y axis
if y_Tmax - y_Tmin < 1:
   y_Tmayor_ticks = 2
   y_Tminor_ticks = 0.2
elif y_Tmax - y_Tmin < 7:
   y_Tmayor_ticks = 1
   y_Tminor_ticks = 0.2
elif y_Tmax - y_Tmin < 11:
   y_Tmayor_ticks = 2
   y_Tminor_ticks = 0.2
elif y_Tmax - y_Tmin < 21:
   y_Tmayor_ticks = 2
   y_Tminor_ticks = 0.5
else:
   y_Tmayor_ticks = 2
   y_Tminor_ticks = 0.2
# 8.3.8 scale the Y axis 50ppm main items
ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))   # 50 Hauptstriche
ax1.tick_params(axis='y', which='major', length=12, width=1.5)
# 8.3.9 scale the Y axis 10ppm minor items
ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))   # 10 Nebenstriche
ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')

# 8.4 print the vertical lines CO2=constant
# 8.4.1 horizontal line at 1120 ppm
ax1.axhspan(4 * C280 -2, 4 * C280 +2, color=c23, alpha=0.25, zorder=0)      # 1120 ppm horicontal stripe
# 8.4.2 horizontal line at 560 ppm
ax1.axhspan(2 * C280 -2, 2 * C280 +2, color=c23, alpha=0.3, zorder=0)        # 560 ppm horicontal stripe
# 8.4.3 horizontal major grid all 50ppm
for line in ax1.get_ygridlines():    # horizontal lines
       line.set_color('blue')           # horizontal color
       line.set_alpha(0.5)
       line.set_linestyle('-')          # optional
       line.set_linewidth(1.1)   # <-- thickness
# 8.4.4 horizontal minor grid all 10ppm
ax1.grid(True, which="minor", axis="y", color="lightblue", alpha=0.94)   # horizontal
# 8.4.5 draw blue 1.5°C bar
if plot71_temperature > 0:
   ax71.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen
elif plot72_AESS_T > 0:
   ax72.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen
elif plot73_ECS_T > 0:
   ax73.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen


# 8.5 print the right y axis
# 8.5.1 plot71 Achse und Beschriftung
if plot71_temperature > 0:
   if plot54_Glen_delta_on > 2:
      ax71.spines.right.set_position(("outward", 50))
   else:
      ax71.spines.right.set_position(("outward", 5))
   ax71.set_ylabel (
         "Δ Temperature in °C 71",
         color=c71,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
          )
   ax71.tick_params(axis="y", labelcolor=c71, labelsize=20)
# 8.5.2 plot72
elif plot72_AESS_T > 0 and plot71_temperature < 1:
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
# 8.5.3 plot73
elif plot73_ECS_T > 0:
   ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax73.tick_params(axis="y", labelcolor=c73)
   ax73.set_ylim(y_Tmin, y_Tmax) # scale
   if plot71_temperature < 1: # make y axis right only if not exist
      #ax73.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # Hauptstriche
      #ax73.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # Nebenstriche
      ax73.minorticks_off()
      ax73.tick_params(axis='y', labelsize=20) # numbers on right y axis size 20
      ax73.set_ylabel (
         "Δ Temperature in °C (ECS = 4.5°C)73",
         color=c71,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
       )
elif plot52_delta_CO2_red_bars > 0:
   ax52.spines.right.set_position(("outward", 20))
   bars = ax52.bar(df2["x_22_years"], df2["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.bar(df2["x_22_years"], df2["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.set_ylabel("red bars Mauna Loa CO2 increase in ppm", color="red", fontname="Arial",fontsize=16) # fontweight="bold"
   ax52.tick_params(axis="y", labelcolor="red", labelsize=16)
   ax52.set_ylim(y_Tmin, y_Tmax) # scale y axis3 right red   
   # 5.2.8 Add numbers on top of delta CO2 bars
   if plot52_delta_CO2_red_bars > 6:
      ax52.bar_label(bars, fontsize=8, fontname="Arial",padding=1, color="black")
if plot34_CO2_emission > 0:
   ax34 = ax1.twinx()

   # Left axis 2: GtC
   if plot73_ECS_T > 0:
      ax34.spines["left"].set_position(("outward", 60))  # move outward from ax1
      ax34.spines["left"].set_visible(True)
      ax34.spines["right"].set_visible(False)
      ax34.yaxis.set_label_position("left")
      ax34.yaxis.tick_left()
   else:
      ax34.spines.right.set_position(("outward", 4))
      ax34.set_ylabel("CO2 cumulative emission in GtCO2  34", color=c34,
                   fontname="Arial",fontsize=20,
                   labelpad=1   # smaller = closer to y axis
                   )
   if plot34_CO2_emission_mode == 1:       # df34a = pd.read_csv("co2_sum_world.csv")
      ax34.plot(df34a["Year34"], df34a["GCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000) # best scaling 2000 GtCO2
   elif plot34_CO2_emission_mode == 2:
      ax34.plot(df34b["Year34"], df34b["Cumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000000000000) #8
   elif plot34_CO2_emission_mode == 3:
      ax34.plot(co2_sum_world["Year"], co2_sum_world["GCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2500) # best scaling 2000 GtCO2
   elif plot34_CO2_emission_mode == 4:
      ax34.set_ylabel("cumulative emission in GtC  34 mode 4", color=c34,
                   fontname="Arial",fontsize=20,
                   labelpad=1   # smaller = closer to y axis
                   )
      ax34.plot(co2_sum_world["Year"], co2_sum_world["CCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 800) # best scaling 500 GtC
      ax34.set_ylim(0, 1000) # best scaling 500 GtC
      
   else:
      ax34.plot(df34b["Year"], df34b["Cumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000000000000) #8

# 8.5.9 
if plot55_population_on > 0:
   ax55.spines.right.set_position(("outward", 80))
   ax55.set_ylabel("Earth Population in Billion", color="green")
   ax55.plot(pop_world["Year"], pop_world["Population_Mrd"], marker="s", color="green", label="Earth Population in Billion K2")
   ax55.set_ylabel("Earth Population in Billion", color="green")
   ax55.tick_params(axis="y", labelcolor="green")
   ax55.set_ylim(1, 9) #8
   # ax55.set_ylim(4, 9)
   #end print_y2=1 - print population


# 8.6 print the x axis 
# 8.6.1 print year below the year numbers 
ax1.set_xlabel("year", fontsize=20 )
plt.xticks(fontsize=20)
ax1.tick_params(axis="x", labelcolor="black", labelsize=20) # 1960 2020 Achsenbeschriftung
# 8.6.2 scale the x axis major 20 years
if x_end - x_anf < 5:
   x_mayor_ticks = 1
   x_minor_ticks = 0.5
elif x_end - x_anf < 11:
   x_mayor_ticks = 1
   x_minor_ticks = 0.5
elif x_end - x_anf < 21:
   x_mayor_ticks = 5
   x_minor_ticks = 1
elif x_end - x_anf < 70:
   x_mayor_ticks = 10
   x_minor_ticks = 2
elif x_end - x_anf < 120:
   x_mayor_ticks = 20
   x_minor_ticks = 5
elif x_end - x_anf < 220:
   x_mayor_ticks = 50
   x_minor_ticks = 10
elif x_end - x_anf < 320:
   x_mayor_ticks = 100
   x_minor_ticks = 20
elif x_end - x_anf < 520:
   x_mayor_ticks = 100
   x_minor_ticks = 50
elif x_end - x_anf < 1020:
   x_mayor_ticks = 200
   x_minor_ticks = 20
elif x_end - x_anf < 2020:
   x_mayor_ticks = 200
   x_minor_ticks = 50
elif x_end - x_anf < 4020:
   x_mayor_ticks = 500
   x_minor_ticks = 100
elif x_end - x_anf < 10020:
   x_mayor_ticks = 1000
   x_minor_ticks = 500
elif x_end - x_anf < 25060:
   x_mayor_ticks = 5000
   x_minor_ticks = 2000
elif x_end - x_anf < 50020:
   x_mayor_ticks = 10000
   x_minor_ticks = 2000
elif x_end - x_anf < 150020:
   x_mayor_ticks = 10000
   x_minor_ticks = 2000
else:
   x_mayor_ticks = 50
   x_minor_ticks = 10
# 8.6.8 scale the x axis major 20 years
ax1.xaxis.set_major_locator(MultipleLocator(x_mayor_ticks))  # works
ax1.tick_params(axis='x', which='major', length=10, width=2) # all 20 years
# 8.6.9 scale the x axis minor 5 years
ax1.xaxis.set_minor_locator(MultipleLocator(x_minor_ticks))   # no work
ax1.tick_params(axis='x', which='minor', length=7,  width=1)
  
# 8.7 print the horizontal lines year 2026
# 8.7.1 vertical major grid all 20 years
for line in ax1.get_xgridlines():   # vertical lines
       line.set_color('black')          # vertical color
       line.set_alpha(0.5)
       line.set_linestyle('--')        # optional '--'
       line.set_linewidth(1.9)   # <-- thickness
# 8.7.2 vertical minorlines all 5 years        
ax1.grid(True, which="minor", axis="x", color="purple", alpha=0.64)   # work vertical 5 years
# 8.7.3 vertical line at year 2026
ax1.axvspan(2025, 2027, color="#B3D9FF", alpha=0.5, zorder=0) # vertical bar'
# 8.7.4
ax1.axvspan(2065, 2066, color=c23, alpha=0.4, zorder=0) # vertical bar'
ax1.axvspan(2174, 2175, color=c23, alpha=0.25, zorder=0) # vertical bar'
# end part 8


# 9 part 9 print information below the plot field
# 9 part 9 print information below the plot field
trs = 20
# 9 part 9 print information below the plot field
# 9.1.1 print line 1 the text below the figure tr1x = -0.09 # tr1y = -.16 
filename = os.path.basename(sys.argv[0])
if plot22_CO2_Mauna_Loa == 1: #  legende world data plot22_CO2_Mauna_Loa
   line22 = Line2D([lr2x1, lr2x2], [lr1y, lr1y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.1.1 plot the blue text
   plt.text(tr2x, tr1y, blue22_text, color=c22, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
else:
   text_below1 = ""
   # 9.1.2 text_below1 = text_below1 + header_parameter
   text_below1 = text_below1 + "Figure from "
   text_below1 = text_below1 + filename
   text_below1 = text_below1 + " v "
   text_below1 = text_below1 + v
   text_below1 = text_below1 + "  https://github.com/Boettcher1960/co2_python"
   plt.text(-0.1, tr1y, text_below1, color="black", fontname="Arial", fontsize=12,
         transform=plt.gca().transAxes)

# 9.2 print line 2 blue Mauna Loa data below the figure
# 9.2.2 print line 22 below the plot explainations
if plot22_CO2_Mauna_Loa == 2: #  legende world data plot22_CO2_Mauna_Loa
   line22 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.2.2.5 plot the blue text
   plt.text(tr2x, tr2y, blue22_text, color=c22, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
# 9.2.3 print line 23 below the plot explainations
elif plot23_Glen_CO2 == 2: # 
   line23 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   fig.add_artist(line23)
   plt.text(tr2x, tr2y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line23)
elif plot34_CO2_emission == 2: # 
   line34 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr2y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)

elif plot22_CO2_Mauna_Loa == 3: #  legende world data plot22_CO2_Mauna_Loa
   K1_text=" 2 new text )"
   plt.text(tr2x, tr2y, K1_text, color=c22, fontname="Arial", fontsize=18,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
else: # 9.2.2 draw bue line as legend
   line22 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line22)
   plt.text(tr2x, tr2y, "707 no item for line 2", color=c22, fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
# end line 2

# 9.3 print line 3 below the plot explainations
# 9.3.3  print line red Glen 
if plot23_Glen_CO2 == 3: # print in line 3
   line23 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   # 9.3.3 draw bue line as legend
   fig.add_artist(line23)
   # 9.3.3 write blue text
   plt.text(tr2x, tr3y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.4 print line 3 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot34_CO2_emission == 3: # 
   line34 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr3y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)
elif plot52_delta_CO2_red_bars == 3 or plot52_delta_CO2_red_bars == 7:
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.3.4 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.4 write red text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.3.4 plot the red text
   plt.text(tr2x, tr3y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.5 print line 3 orange Glen data below the figure
elif plot53_CO2_orange2025 == 3: # print in line 3 up to 2025
   line3 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.3.5 draw bue line as legend
   fig.add_artist(line3)
   # 9.3.5 write blue text
   red53_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.3.5 plot the blue text
   plt.text(tr2x, tr3y, red53_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
# 9.3.6  print line 3 green Glen 
elif plot54_Glen_delta_on == 3: # print in line4
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.3.6 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.6 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.3.6 plot the green text
   plt.text(tr2x, tr3y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.6_ print line 3 red Glen data below the figure
# 9.3.7 print line 3 plot55_population_on marker="s"
elif plot55_population_on == 3: #  legende world data plot22_CO2_Mauna_Loa
   line55 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.3.7 draw bue line as legend
   fig.add_artist(line55)
   # 9.3.7 write green text
   plt.text(tr2x, tr3y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot73_ECS_T == 3:
   line73 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text         
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0) 73"
   plt.text(tr2x, tr3y, red73_text, color=c73, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)


   # 9.3 end print line 3 below the plot explainations


# 9.4 print line 4 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.4.3_ print line 3 red Glen data below the figure
if plot23_Glen_CO2 == 4: # print in line 3
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   # 9.4.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.4.3 write blue text
   text_plot23_Glen=" dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.4.3 plot the blue text
   plt.text(tr2x, tr4y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot52_delta_CO2_red_bars == 4 or plot52_delta_CO2_red_bars == 8:
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling 52"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.4 work_ print line 4 orange Glen data below the figure
elif plot53_CO2_orange2025 == 4: # print in line 3 up to 2025
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red53_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red53_text, color="orange", fontname="Arial", fontsize=trs,
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
   # 9.4.2 print line 4 plot55_population_on marker="s"
elif plot34_CO2_emission == 4: # 
   line34 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr4y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)
elif plot55_population_on == 4:
   line55 = Line2D([lr2x1, lr2x2], [lr4y, lr4y],
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   fig.add_artist(line55)
   plt.text(tr2x, tr4y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.4.52 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot71_temperature == 4:
   line7 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.4.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.4.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red71_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 4:
   line72 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   plt.text(tr2x, tr4y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot73_ECS_T == 4:
   line73 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text         
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0) 73"
   plt.text(tr2x, tr4y, red73_text, color=c73, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)

# 9.5.2 print line 5 plot55_population_on marker="s"
if plot55_population_on == 5: #  legende world data plot22_CO2_Mauna_Loa
   line55 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line55)
   # 9.5.4 write green text
   plt.text(tr2x, tr5y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot71_temperature == 5:
   line7 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.5.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.5.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   red71_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
   # 9.5.7 plot the blue text
   plt.text(tr2x, tr5y, red71_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 5:
   line72 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   red72_text="AESS_T Apparent Earth Sensitivity=8°C*log2(CO2/C0)"
   plt.text(tr2x, tr5y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   #else: # 9.5.9 draw bue line as legend
   #plt.text(tr2x, tr5y, "Line 5 -0.48", color="white", fontname="Arial", fontsize=trs,
   #transform=plt.gca().transAxes)
elif plot73_ECS_T == 5:
   line73 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text 
   if plot72_AESS_T == 5 and plot73_ECS_T == 5:
      red73_text="ECS=4.5°C*log2(CO2/C0)"
      plt.text(0.71, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
      transform=plt.gca().transAxes)
   else:            
       red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0)"
       plt.text(tr2x, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
# 9.5 end print line 5 

# 9.6 print line 6 
if plot73_ECS_T < 6:
   text6 = f" CO2_min= {y_min}ppm " # y_max number inside string
   text6 = text6 + f" CO2_max= {y_max} " # y_max number inside string
   text6 = text6 + f"  T_max= {y_Tmax}°C    Parameter=" # y_max number inside string
   text6 = text6 + header_parameter
   # 9.6.2 plot line 6
   plt.text(-0.12, -.56, text6 , color="black", fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
   fig.tight_layout()
   plt.tight_layout()
else: # plot73_ECS_T = 6
   line73 = Line2D([lr2x1, lr2x2], [lr6y, lr6y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   fig.add_artist(line73)
   # 9.6.8 write  text 
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0)"
   plt.text(tr2x, tr6y, red73_text, color=c73, fontname="Arial", fontsize=trs,
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
   path = f"/Users/thomasboettcher/Desktop/{filename}"
   fig.savefig(path, dpi=300, bbox_inches="tight")
   path = f"/Users/thomasboettcher/documents/Python/4_Python_CO2/42_CO2_T.png"
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



# Datenquellen:
# 2.2.2 Mauna_Loa 13.3.2026
# plot22_CO2_Mauna_Loa https://gml.noaa.gov/ccgg/trends/global.html
#
# 3.2 https://ourworldindata.org/grapher/cumulative-co-emissions


# https://github.com/zmlabe 
#
