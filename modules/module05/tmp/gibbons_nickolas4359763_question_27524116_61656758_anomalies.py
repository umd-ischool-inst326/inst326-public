data = open("MD_covid_vaccines") 

all_counties = set()
bad_counties = set()

for line in data:
    row = line.split(",")
    data = row[1]
    county = row[2]
    
    all_counties.add(county)
    
    if date < "2020/12/11":
        bad_counties.add(county)
        
print("all", all_counties)
print("bad", bad_counties)
print("good", all_counties - bad_counties)
