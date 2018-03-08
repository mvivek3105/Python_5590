#Importing csv, numpy, lda
import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
x_axis = []
y_axis = []
# Writing the data into x_axis and y_axis
with open("lab3data.csv") as f:
    csvfile = csv.reader(f, delimiter=',')
    next(csvfile)
    for line in csvfile:
        temp = float(line[0])
        relative_humidity = float(line[1])
        wind = float(line[2])
        precipitation = float(line[3])
        area = 1 if float(line[4]) > 0 else 0
        x_axis.append([temp, relative_humidity, wind, precipitation])
        y_axis.append(area)
# Converting the data in x_axis and y_axis  into numpy array
np_x = np.array(x_axis)
np_y = np.array(y_axis)
# Performing LDA
model = LinearDiscriminantAnalysis()
model.fit(np_x, np_y)
# prediction that rainfall may  occur
temp = 40; relative_humidity = 85; wind = 8 ; precipitation = 0.1
print("With the following weather conditions: temperature [%f] in Celcius, relative humidity [%f] of percent, wind speed [%f] in km/h, and  precipitation [%f] in mm/m2" % (temp, relative_humidity, wind,  precipitation))
if model.predict([[temp, relative_humidity, wind,  precipitation]])[0]:
    print("Rain fall may occur.")
else:
    print("Rain fall may not occur.")
# prediction that rainfall may not occur
temp = 6; relative_humidity = 30; wind = 0.8; precipitation = 5.3
print("With the following weather conditions: temperature [%f] in Celcius, relative humidity [%f] of percent, wind speed [%f] in km/h, and  precipitation [%f] in mm/m2" % (temp, relative_humidity, wind,  precipitation))
if model.predict([[temp, relative_humidity, wind,  precipitation]])[0]:
    print("Rain fall may occur.")
else:
    print("Rain fall may not occur.")