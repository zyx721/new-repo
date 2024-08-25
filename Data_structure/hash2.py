zyx = {}

import  csv
with open(r'C:\12\Desktop\nyc_weather.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)
    next(csv_file)
    for row in csv_reader:
        zyx[row[0]]=row[1]
print(zyx['Jan 4'])