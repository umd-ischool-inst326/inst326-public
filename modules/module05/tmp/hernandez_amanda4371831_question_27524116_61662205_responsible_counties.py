data_file = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

all_counties = set()
responsible_counties = set()

for line in data_file:
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        responsible_counties.add(county)


print("All Counties: " , all_counties)
print()
print("Counties responsible for the problem: " , responsible_counties)
print()
print("Counties handling the problem well: " , all_counties - responsible_counties)