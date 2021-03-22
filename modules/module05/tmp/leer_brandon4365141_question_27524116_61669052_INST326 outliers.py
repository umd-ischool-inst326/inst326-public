fhand = open('data.csv')

bad_counties = set() 
all_counties = set()

for line in fhand:
    row = line.split(",")
    date = row[1]
    county = row[2]
    all_counties.add(county)
    if date < "2020/12/11":
        bad_counties.add(county)
good_counties = all_counties - bad_counties
print("Responsible: ", bad_counties )
print("Not Responsible: ", good_counties)