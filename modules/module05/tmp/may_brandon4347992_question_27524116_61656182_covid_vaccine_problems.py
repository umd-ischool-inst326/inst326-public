df = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

md_counties = set()
prob_counties = set()

for line in df: 
    row = line.split(',')
    date = row[1]
    county = row[2]

    md_counties.add(county)

    if date < '2020/12/11': 
        prob_counties.add(county)

print('ALL MD COUNTIES:', md_counties)
print()
print ("PROBLEM COUNTIES:", prob_counties) 
print()
print('GOOD COUNTIES:', md_counties - prob_counties)