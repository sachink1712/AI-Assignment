import csv


'''Script to read and process weather data from NOAA NCEI.
    Data must be downloaded in csv format. Functionality may
    depend on specific output selected at checkout on the NCEI site
'''

#csv to be read should be in the same directory as this program
filename = '1992829.csv'

#initialize lists to fill later
tmax = []
tmin = []
date = []
pcrp = []

#open the csv file and read then save data to python lists
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #this is the first line. It describes the data
            header = row
            line_count += 1
        else:
            if line_count == 1:
                #Only save the stationId and name once
                #since they dont change
                stationID = row[0]
                stationName = row[1]

            #fill our lists (remember to convert string to int)
            date.append(row[2])
            tmax.append(int(row[6]))
            tmin.append(int(row[7]))
            pcrp.append(float(row[3]))

#-----------------------------------------------
#You should only need to add code to the lines below
print('The first maximum temperaturen recorded was {} and the' .format(tmax[0]))
print('first inimum temperature recorded was {}'.format(tmin[0]))
print('The length of tmax is {} and the length of tmin is {}'.format(len(tmax), len(tmin)))
print('The maximun recorded temperature was {} and the minimun recorded temperature was {}'.format(max(tmax),min(tmin)))
print('Types- tmin: {}, tmin[]: {}, date: {}, date[10]: {}\n'.format(type(tmin),type(tmin[10]),type(date),type(date[10])))

print('Date of last recorded measurement: {}'.format(date[-1]))
lowest_temperature = tmin.index(-18)
print('The lowest temperature in 2009 was {} and occurred on {}'.format(min(tmin),date[lowest_temperature]))
print(lowest_temperature)
lowest_temperature_week = tmin[27:34]
lowest_temperature_week
print('Low temperature during the week of {} were: {}'.format(date[lowest_temperature],lowest_temperature_week))
index = date.index('2019-11-13')
print(index)
print('{}: The minimum temperature was {} and the maximun temperature was {}'.format(date[316],tmin[316],tmax[316]))
print(pcrp)
