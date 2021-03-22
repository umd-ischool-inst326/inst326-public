dataset = open('dataset.csv')

set1 = set()
set2 = set()
set3 = set()

for line in dataset :
    split1=line.split(',')
    dateofvaccination = split1[1]
    countyinMD = split1[2]
    set1.add(countyinMD)

    if dateofvaccination < "2020/12/11":
        set2.add(countyinMD)
    elif dateofvaccination > "2020/12/11":
        set3.add(countyinMD)

set1.remove("Unknown")
set2.remove("Unknown")
set3.remove("Unknown")


print(f"all the counties:{set1}")
print()
print(f"down bad counties:{set2}")
print()
print(f"good counties: {set3}")