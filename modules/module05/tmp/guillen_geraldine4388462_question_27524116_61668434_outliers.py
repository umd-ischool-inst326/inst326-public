data = open('data.csv')

all_counties = set()
wrong_counties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    all_counties.add(county)

    if date < "2020/12/11":
     wrong_counties.add(county)

print('all', all_counties)
print()
print('wrong', wrong_counties)
print()
print('good', all_counties - wrong_counties)