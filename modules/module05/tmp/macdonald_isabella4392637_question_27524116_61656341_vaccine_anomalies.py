data = open('md_covid_data.csv')

# initiate the set objects
all_counties = set()
bad_counties = set()

for line in data:
    row = line.split(",")

    # create the date and county variables 
    date = row[1]
    county = row[2]

    # add counties to the all_counties set
    all_counties.add(county)

    # if the date is pre December, add it to the bad_counties set
    if date < "2020/12/11":
        bad_counties.add(county)

# this checks if there are any dates recorded that have no daily first doses or daily second doses given. That would mean that no one
# was given a vaccine, which is an error.
for line in data:
    row = line.split(",")

    # create the daily first doses and daily second doses variables
    daily_first_doses = row[3]
    daily_second_doses = row[5]

    all_counties.add(county)

    # if both the daily first doses and daily second doses are zero, add it to the bad_counties set
    if daily_first_doses == "0" and daily_second_doses == "0":
        bad_counties.add(county)


# finally, print out all of the counties, the problem counties, and the good counties
print('All Counties:', all_counties)
print('Problem Counties:', bad_counties)
print('Good Counties:', all_counties - bad_counties)

