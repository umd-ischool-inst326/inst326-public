#!/usr/bin/env python3

import csv

bad_counties = set()
all_counties = set()

for row in csv.DictReader(open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv', 'r')):
    print(row)
    if row['VACCINATION_DATE'] < '2020/12/11':
        bad_counties.add(row['County'])
    all_counties.add(row['County'])

print(all_counties - bad_counties)

