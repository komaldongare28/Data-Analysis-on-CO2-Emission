"""
Name: Python Data Analysis
Purpose: Plotting comparison graph for two countries

Algorithm:

Step 1: Take two comma-separated countries input from user
Step 2: Extracting the Index number for both countries
Step 3: Passing the value to plot function and setting up label for country

"""

import matplotlib.pyplot as plt


print("A Simple Data Analysis Program")
print()

emission_dict = {}

with open('Emissions.csv', 'r') as file:
    for data in file.read().split('\n'):
        emission_dict.update({data.split(',')[0]: data.split(',')[1:]})

print("All data from Emissions.csv has been read into a dictionary.", end="\n\n")

input_year = input("Select a year to find statistics (1997 to 2010): ")

index_of = int()
lines = []

for item in emission_dict.values():
    if input_year in item:
        index_of = (item.index(input_year))

total = 0
i = 0
emissions_in_year = []

for value in emission_dict.values():
    if i != 0:
        total += float(value[index_of])
        emissions_in_year.append(list(emission_dict.values())[i][index_of])
    i += 1

max_country_index = int(emissions_in_year.index(str(max(float(str_value) for str_value in emissions_in_year))))
min_country_index = int(emissions_in_year.index(str(min(float(str_value) for str_value in emissions_in_year))))
average_emissions = total / 195

max_emission = list(emission_dict.keys())[max_country_index + 1]
min_emission = list(emission_dict.keys())[min_country_index + 1]

print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
      f'and [{max_emission}] respectively.')
print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
print()


visualize_country = input("Select the country to visualize: ")

number = list(emission_dict.keys()).index(visualize_country)
plt.plot(list(map(float, list(emission_dict.values())[0])),
         list(map(float, list(emission_dict.values())[number])))
plt.title("Year vs Emissions in Capita")
plt.xlabel("Year")
plt.ylabel("Emissions in " + visualize_country.title())
plt.show()
print()

"""
Step 1: Take two comma-separated countries input from user
"""
country1, country2 = input("Write two comma-separated countries for which you want to visualize data: ").split(", ")

"""
Step 2: Extracting the Index number for both countries
"""

index_num_1 = list(emission_dict.keys()).index(country1)
index_num_2 = list(emission_dict.keys()).index(country2)

"""
Step 3: Passing the value to plot function and setting up label for country
"""

# In this task we combined two plots in one and given the label to identify.
plt.plot(list(map(float, list(emission_dict.values())[0])),
         list(map(float, list(emission_dict.values())[index_num_1])), label=country1)
plt.plot(list(map(float, list(emission_dict.values())[0])),
         list(map(float, list(emission_dict.values())[index_num_2])), label=country2)
plt.title("Year vs Emissions in Capita")
plt.xlabel("Year")
plt.ylabel("Emissions")
plt.legend()
plt.show()
print()
