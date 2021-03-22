data = open("DataSet_Covid.csv")

data_set1 = set()
data_set2 = set()


for line in data:
    split1 = line.split(',')
    data_vaccination = split1[1]
    MD_county = split1[2]
    data_set1.add(MD_county)


    if data_vaccination < "2020/12/11":
        data_set2.add(MD_county)

print(data_set1)
print(data_set2)


