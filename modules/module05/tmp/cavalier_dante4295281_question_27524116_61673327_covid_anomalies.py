csv_file = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

counties = set()
problem_counties = set()

for line in csv_file:
    column = line.split(",")

    date = column[1]
    county = column[2]

    counties.add(county)

    if date < "2020/12/11":
        problem_counties.add(county)
        
print('All counties:', counties)
print()
print('Counties with errors:', problem_counties)
print()
print('Counties without errors:', counties - problem_counties)