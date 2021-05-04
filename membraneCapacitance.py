import csv
import os
import pandas as pd
import sys
from cmMeas import cm_meas

# Make sure that pyabf and numpy are installed before continuing
try:
    import pyabf
    import numpy
except ValueError:
    print('You need pyabf to run the cmMeas program!')

#Making a loading bar to show that things are running
load_bar = ['-','\\','|','/']

# Get the user's path to the csv file w/ the information about their abf files...
path = input('Enter path to your csv file: ')
file_name = input('Enter the name of your csv file (DO NOT INCLUDE THE EXTENSION!): ')

# ...and make sure that path exists
if os.path.isfile(f'{path}/{file_name}.csv') == True:
    print('Path exists... now I need column info about where your abf files are written')
else:
    print('Invalid path and/or file name, please check your entries and try again')
    sys.exit()

# Now load the csv file and then begin the analysis
csv_file = f'{path}/{file_name}.csv'
start = int(input('In which column is your starting file number?: '))
end = int(input('In which column is your ending file number?: '))
freq = int(input('And finally, what was the frequency [Hz] at which you were collecting?: '))

cm_values = []
tmin_values = []
tmax_values = []

with open(csv_file, "r") as input:
    reader = csv.reader(input)
    next(reader)
    count = 0 #Wil determine which part of the loading bar is printed when

    for row in reader:
        #Print load bar
        load = count % 4
        print(load_bar[load], end='\r') #\r makes it so whatever is printed is replaced on the next output
        count += 1 #Next part of loading bar will be printed on the next loop

        Cm, t1, t2 = cm_meas(path, row[start], row[end], freq)
        cm_values.append(Cm)
        tmin_values.append(t1)
        tmax_values.append(t2)

df = pd.read_csv(f'{path}/{file_name}.csv')
df['Cm'] = cm_values
df['tmin'] = tmin_values
df['tmax'] = tmax_values

df.to_csv(f'{path}/{file_name}_output.csv')