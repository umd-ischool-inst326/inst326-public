data_file = open("MD_COVID_DATA.csv")

all_counties = set()
improper_counties = set()

for line in data_file:
    row = (line.split(","))
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        improper_counties.add(county)

print('All', all_counties)
print()
print('Improper', improper_counties) 
print()
print('Good', all_counties - improper_counties)