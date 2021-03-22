data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

county_issues = set()
all_counties = set()

for line in data:
    splitrow = line.split(",")
    date = splitrow[1]
    county = splitrow[2]

    if date < "2020/12/11":
        county_issues.add(county)
    else:
        all_counties.add(county)

print("Error Counties: ", county_issues)
print()
print("Good Counties: ", all_counties - county_issues)
print()
print("All Counties: ", all_counties)