data = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv','r', encoding = 'utf-8')
responsible_counties = set()
all_counties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    
    all_counties.add(county)
    if date < "2020/12/11":
        responsible_counties.add(county)

print("Responsible for Problem:", responsible_counties, "\n") 
print("Not Responsible for Problem:", (all_counties - responsible_counties))
