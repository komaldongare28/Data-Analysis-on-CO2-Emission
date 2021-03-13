"""
Name: Python Data Analysis
Purpose: Read CSV File and store data in dictionary

Algorithm:

Step 1: Opening File in read mode and looping through data
Step 2: Printing the data just to ensure successful read

"""

print("A Simple Data Analysis Program")
print()

scan_file = {}
"""
Step 1: Opening File using with in read mode and looping through data
"""

with open('Emissions.csv', 'r') as file:
    # Read in file object and spiting it with '\n'
    for data in file.read().split('\n'):
        # Updating the dictionary file | Splitting the string by COMMA(,) - Store first value as KEY
        # and Store other value as VALUE
        scan_file.update({data.split(',')[0]: data.split(',')[1:]})

"""
Step 2: Printing the data just to ensure successful read
"""
for x, y in scan_file.items():
    print(x, end=" - ")
    print(y)

print("All data from Emissions.csv has been read into a dictionary.")