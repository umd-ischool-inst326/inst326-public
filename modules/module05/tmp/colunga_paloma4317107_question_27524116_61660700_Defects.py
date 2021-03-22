data = open('VaccinatedCounties.csv')

invalid_counties = set()
valid_counties = set()

'''For loop that filters what data will be used'''
for line in data:
    row = line.split(",")
    date = row[1]
    county = row[2]
    
    ''' Determines if a county has valid/invalid vaccination data '''
    if date < "2020/12/21":
        invalid_counties.add(county)
    else:
        valid_counties.add(county)
        
    ''' Displays counties that have valid or invalid vaccination data entries.'''      
print("COUNTIES WITH INVALID VACCINATIONS",
      invalid_counties,
      "COUNTIES WITH VALID VACCINATIONS",
      valid_counties)
    
