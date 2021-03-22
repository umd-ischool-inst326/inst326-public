data = open('data.csv')

inaccurate_counties = set()
all_counties = set()

for line in data: 
    r = line.split(",")
    date = r[1]
    county = r[2]

    all_counties.add(county)

    if date <"2020/12/11":
        inaccurate_counties.add(county)
print('all counties in MD:', all_counties)  
print()   
print('counties that are inaccurate:', inaccurate_counties)
print()
print('counties that are accurate:', all_counties - inaccurate_counties)