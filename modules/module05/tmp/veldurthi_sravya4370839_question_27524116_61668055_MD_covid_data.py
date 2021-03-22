data = open('csv_MD_COVID19.csv')

all_counties = set()
outlier_counties = set()

for line in data:
    obs = line.split(",")
    date = obs[1]
    county = obs[2]

    all_counties.add(county)
    all_counties.discard('County')

    if date < "2020/12/11":
        outlier_counties.add(county)


print(" ")
print("all MD testing counties: ", all_counties)
print(" ")
print("invalid/outlier MD testing counties: ", outlier_counties)
print(" ")
print("valid MD testing counties: ", all_counties-outlier_counties)