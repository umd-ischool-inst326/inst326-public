data = open('vaxData.csv')

all_counties = set()
bad_counties = set()
for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    all_counties.add(county)

    if date < "2020/12/11":
        bad_counties.add(county)
    
print('GOOD', all_counties - bad_counties)

print('BAD', bad_counties)

