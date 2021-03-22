#Opens Vaccination csv File
data=open('/Users/ryanmoore/Documents/INST326_VSCODE/MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')

#Creates sets
bad_counties=set()
all_counties=set()

#Creates set of all Maryland Counties that will be used later
real_counties=frozenset(("Allegany","Anne Arundel", "Baltimore", "Baltimore City",
"Calvert", "Caroline", "Carroll", "Cecil", "Charles", "Dorchester",
"Frederick", "Garrett", "Harford", "Howard", "Kent", "Montgomery",
"Prince George's", "Queen Anne's", "St. Mary's", "Somerset", "Talbot",
"Washington", "Wicomico", "Worcester"))

for line in data:
    #Makes each row into a list
    row=line.split(",")

    #Retrieves the date which is in indice 1 of each list
    date=row[1]

    #Retrieves the county which is in indice 2 of each list
    county=row[2]

    #Adds county to bad_counties set if they added data before the vaccine was released
    if date<"2020/12/11":
        bad_counties.add(county)

    #Adds each county in the file to the all_counties set once
    all_counties.add(county)

#Creates a good_counties set for counties that didn't prematurely add vaccinations
good_counties=set((all_counties.difference(bad_counties)))

#Prints counties that have recorded a vaccination before 12/11/2020
print("Counties that have recorded a vaccination before 12/11/2020:\n",sorted(bad_counties),"\n")

#Prints counties that haven't recorded a vaccination before 12/11/2020
print("Counties that haven't recorded a vaccination before 12/11/2020:\n",sorted(good_counties),"\n")

#Creates new set for bad counties that discards any strings that are not counties (Ex: 'Unknown')
real_bad_counties=real_counties.intersection(bad_counties)
print("Real counties that have recorded a vaccination before 12/11/2020:\n", sorted(real_bad_counties),"\n")

#Creates new set for good counties that discards any strings that are not counties (Ex: 'County')
real_good_counties=set((good_counties.intersection(real_counties)))
print("Real counties that haven't recorded a vaccination before 12/11/2020:\n", sorted(real_good_counties))



