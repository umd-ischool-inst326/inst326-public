#renamed the csv to mdcovid.csv
covid = open("mdcovid.csv")

probcounties = set()
counties = set()

for line in covid:
    data = line.split(',')
    counties.add(data[2])
    if data[1] < '2020/12/11':
        probcounties.add(data[2])

print("Bad Counties:\n", probcounties, '\n')
print("Good Counties:\n", counties - probcounties)
