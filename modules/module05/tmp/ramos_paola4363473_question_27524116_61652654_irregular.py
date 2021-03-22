data = open("MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv")

all_counties = set()
odd_counties = set()

for line in data: 
    row = (line.split(","))
    date = row[1]
    county = row[2]

    all_counties.add(county)
    
    if date < "2020/12/11":
        odd_counties.add(county)

print('All: ',all_counties)
print()
print('Odd: ', odd_counties)
print()
print('Good: ', all_counties - odd_counties)
