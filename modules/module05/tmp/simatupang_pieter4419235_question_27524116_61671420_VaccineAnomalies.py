data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

bad_counties = set()
all_counties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    all_counties.add(county)
   
    if date < "2020/12/11":
        bad_counties.add(county)


print()
print('Bad Counties: ', bad_counties)
print()
print('Good Counties: ', all_counties - bad_counties)
print()
print('All Counties: ', all_counties)
