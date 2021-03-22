data_file = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

all_counties = set()
responsible_counties = set()

"""
accessing the date/county from the dataset and 
checking if it's a county responsible or not responsible for the problem
"""
for line in data_file:
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        responsible_counties.add(county)

print('Counties That Are Responsible:', responsible_counties) 
print()
print('Counties That Are Not Reponsible:', all_counties - responsible_counties)