data = open('data.csv')

all_counties = set()
bad_counties = set()

for line in data:
    row = (line.split(","))
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        bad_counties.add(county)

print('all', all_counties)
print()
print('bad', bad_counties)
print()
print('good', all_counties - bad_counties)