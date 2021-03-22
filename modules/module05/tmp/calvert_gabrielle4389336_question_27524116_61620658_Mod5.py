data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

faultyCounties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]

    if date < "2020/12/11":
        faultyCounties.add(county)

print(faultyCounties)