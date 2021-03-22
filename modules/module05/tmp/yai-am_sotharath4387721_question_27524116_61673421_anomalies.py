""" Sotharath Yai Am 3/7/2021 """

data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

""" Creates set for all counties and incorrect reporting counties. """

all_counties = set()
bad_counties = set()

""" Reads the data and compares it to the condition to determine which are the incorrect reports. """

for line in data: 
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        bad_counties.add(county)

""" Prints all of the counties and then prints the counties that incorrectly and correctly reported data. """

print('ALL REPORTING COUNTIES', all_counties)
print()
print('INCORRECTLY REPORTED', bad_counties)
print()
print('CORRECTLY REPORTED', all_counties - bad_counties)