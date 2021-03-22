data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

all_counties = set()
bad_counties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        bad_counties.add(county)

# Prints a list of all counties. Then a list of the "bad" counties that are producing the incorrect dates. 
# Then a list of "good" counties that are producing the correct dates.

print('All', all_counties)
print('Bad', bad_counties)
print('Good', all_counties - bad_counties)