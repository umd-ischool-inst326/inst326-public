import pandas as pd

df = pd.read_csv("MD_COVID19_TotalVaccinationsCountyFirstandSecondDose.csv", parse_dates=['VACCINATION_DATE'])

groups = df.groupby("County", )

for n, group in groups:
    print(f"County {n}, #{len(n)}")
    print("check new dose and cumulative dose, should be all zero")
    print( "FirstDose Diff: ", group['DailyFirstDose'].sum() - group.iloc[-1]['CumulativeFirstDose'] )
    print("SecondDose Diff: ", group['DailySecondDose'].sum() - group.iloc[-1]['CumulativeSecondDose'] )
    print("check vaccination date, should be 1")
    print( "Portion of valid vaccination date", group['VACCINATION_DATE'].map( lambda x: x.year>=2020 ).sum() / len(group) )
    print("---------------------------------------")