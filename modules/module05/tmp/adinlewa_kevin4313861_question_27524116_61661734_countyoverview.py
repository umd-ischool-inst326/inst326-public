file_opener = open('MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv')
counties = set()
bad_counties = set()
for line in file_opener:
   listMaker = (line.split(','))
   vaccineDates = listMaker[1]
   countiesAffected = listMaker[2]

   counties.add(countiesAffected)

   if vaccineDates < '2020/12/11':
      bad_counties.add(countiesAffected)

print('ALL COUNTIES: ', counties)
print('------------------------------------------------')
print('COUNTIES RESPONSIBLE: ', bad_counties)
print('------------------------------------------------')
print('NOT RESPONSIBLE: ', counties - bad_counties)