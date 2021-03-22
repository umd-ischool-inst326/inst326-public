data = open('MD_COVID_Data.csv')

problem_counties = set()
all_counties = set()
for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    all_counties.add(county)

    if date < "2020/12/11":
        problem_counties.add(county)
print("Problem: ", problem_counties)
print()
print("All: ", all_counties)
print()
print("Good: ", all_counties - problem_counties)