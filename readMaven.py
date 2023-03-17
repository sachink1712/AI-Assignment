import csv

time = []
altitude = []
latitude = []
longitude = []
density = []

filename = "mavenAr20170910.csv"
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #this is the first line. It describes the data
            header = row
            line_count += 1
        else:
            #fill our lists (remember to convert string to float)
            time.append(row[0])
            altitude.append(float(row[7]))
            density.append(float(row[15]))

### Add code below this point.
for i,j in zip(altitude,density):
    print('Altitude: {:.3f} km, Density: {:.3f} #/cm3'.format(i,j))