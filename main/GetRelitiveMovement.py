import csv
import pandas as pd


LinkToCSV = (r'RecoilRecordings\ak47.csv')

LinkToRelCSV = (r'RecoilRecordings\RelitiveMovement_ak47.csv')
df = pd.read_csv(r'RecoilRecordings\ak47.csv')

rel = []
for i in range(0,len(df)-1):
        z = i
        xarr = df["x"].to_numpy()[z+0]-df["x"].to_numpy()[z+1]
        yarr = df["y"].to_numpy()[z+0]-df["y"].to_numpy()[z+1]
        print(xarr)
        print(yarr)
        x = [xarr,yarr]
        rel.append(x)


        

print(rel)
df1=pd.DataFrame(rel)
df1.to_csv(LinkToRelCSV,index=False)
               