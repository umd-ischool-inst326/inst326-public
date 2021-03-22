dataset = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv', 'r', encoding='utf-8')

all_counties = set()
outlier_counties = set()

for line in dataset:
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        outlier_counties.add(county)

print("all counties", all_counties)
print()
print("outlier counties", outlier_counties)
print()
print("good counties", all_counties - outlier_counties)
