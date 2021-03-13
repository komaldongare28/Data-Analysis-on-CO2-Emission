"""
Name: Python Data Analysis
Purpose: Maximum and Minimum emission in Country + Average emission in year

Algorithm:

Step 1: Take the input from user
Step 2: Extracting index of the year
Step 3: Creating the list of emission in year
Step 4: Performing the analysis
Step 5: Printing the data in required format using formatted string

"""

print("A Simple Data Analysis Program")
print()

emission_dict = {}

with open('Emissions.csv', 'r') as file:
    for data in file.read().split('\n'):
        emission_dict.update({data.split(',')[0]: data.split(',')[1:]})

print("All data from Emissions.csv has been read into a dictionary.", end='\n\n')
"""
Step 1: Take the input from user.
"""
input_year = input("Select a year to find statistics (1997 to 2010): ")

index_of = None
lines = []
"""
Step 2: Extracting index of the year
"""
# Loop through First VALUE of Dictionary and if year present in list then set index of VALUE as index_of
for item in next(iter(emission_dict.values())):
    if input_year in item:
        index_of = (item.index(input_year))

total = 0
i = 0
emissions_in_year = []
"""
Step 3: Creating the list of emission in year
"""
# Loop through VALUES of Dictionary
for value in emission_dict.values():
    # For the first loop skip the code because in our case it contains Column Names and Years
    if i != 0:
        # Add VALUE of Emission to total
        total += float(value[index_of])
        # Append the value to emissions_in_year
        emissions_in_year.append(list(emission_dict.values())[i][index_of])
    i += 1


"""
Step 4: Performing the analysis
"""
# Let's try to understand this from inner Single Line loop. We converted String to float and created list, from this
# list we found the maximum and minimum float value, converted that into string and got the index of maximum and
# minimum emission country.
max_country_index = int(emissions_in_year.index(str(max(float(str_value) for str_value in emissions_in_year))))
min_country_index = int(emissions_in_year.index(str(min(float(str_value) for str_value in emissions_in_year))))
average_emissions = total / 195

# Using index value we got the Name of maximum and minimum country name
max_emission = list(emission_dict.keys())[max_country_index + 1]
min_emission = list(emission_dict.keys())[min_country_index + 1]


"""
Step 5: Printing the data in required format using formatted string
"""
print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
      f'and [{max_emission}] respectively.')
print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
print()
