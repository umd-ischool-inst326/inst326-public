data = open('DATA.csv')

set1 = set()
bad_counties = set()

for line in data:
    col = line.split(",")
    date = col[1]
    MDcounty = col[2]
    set1.add(MDcounty)

    if date < "2020/12/11":
        bad_counties.add(MDcounty)
    
print(set1)
print(bad_counties)