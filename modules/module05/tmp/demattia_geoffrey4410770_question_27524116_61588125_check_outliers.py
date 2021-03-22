data = open("data_file.csv")

odd_counties = set()

inline_county = set()

for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    inline_county.add(county)
    if date < "2020/12/11":
        odd_counties.add(county)
    
print("Bad", odd_counties)
print("All", inline_county)
good_county = inline_county - odd_counties
print("Good", good_county)