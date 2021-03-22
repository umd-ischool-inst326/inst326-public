import csv

appr_date = '2020/12/11 15:00:00+00'
non_resp_counties = set()
resp_counties = set()

with open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv') as f:
    reader = csv.reader(f, delimiter=',')
    # Skip first line of CSV headers
    next(reader)
    # Iterate over each line in the data set
    for row in reader:
        # Skip empty lines
        if row:
            county = row[2]
            if row[1] >= appr_date:
                non_resp_counties.add(county)
            else:
                resp_counties.add(county)
    # Print which counties fall into what category
    non_resp_counties -= resp_counties
    print(f'Responsible Counties:\n{resp_counties}')
    print(f'\nOther Counties:\n{non_resp_counties}')
