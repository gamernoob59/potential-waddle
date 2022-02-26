import csv
data1=[]
data2=[]
with open ("olddata.csv", "r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        row=row[row['column_name'.notna()]]
        data1.append(row)

header1=data1[0]
planet_data1=data1[1:]

with open ("newdata.csv", "r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

header2=data2[0]
planet_data2=data2[1:]

header=header1+header2
planet_data=[]

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open ("final.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)