mddata = open('MDData.csv')

all_counties =set()
bad_counties = set()
good_counties =set()

for line in mddata:
    row = line.split(",")
    date =row[1]
    county =row[2]
    all_counties.add(county)

    if date < "2020/12/11":
        bad_counties.add(county)
        

    
print('Bad',bad_counties)
print()
print('All', all_counties)
print()
print('Good', all_counties - bad_counties)
