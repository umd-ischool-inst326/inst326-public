data=open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv',)

good_counties=set()
bad_counties=set()

for line in data:
    newLine=line.split(',')
    date=newLine[1]
    county=newLine[2]

    if date<"2020/12/11":
        bad_counties.add(county)

    good_counties.add(county)
print("the good counties:", good_counties-bad_counties)
print("the bad counties: ", bad_counties)