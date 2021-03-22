data = open('CovidDATA.csv')

weird_counties = set()
all_counties = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]

    all_counties.add(county)

    if date < "2020/12/11":
        weird_counties.add(county)

print(weird_counties)
print("bad counties above, good counties below")
print(all_counties - weird_counties)
