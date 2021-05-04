# Bulk-Capacitance-Calculator v1.0

This is a simple program that takes in a csv file with a list of the test pulses for which you would like to calculate a membrance capacitance, and creates a second csv file with the capacitances and tau indices (so you can plot and check the time constants if you want) alongside the rest of the csv file data. To get started, just call the membraneCapacitance.py program. It involves a few command-line inputs calling for:

1. The file to the path of your csv file, which needs to be in the same path as your abf files
2. The name of the csv file, but do not include the extension! The name will be used for the output as well
3. The column number in the csv file in which the first numbered abf file exists and
4. The column number in the csv file in which the last numbered abf file exists
5. The frequency at which you were collecting the data (I didn't feel like dealing with the file headers right now, but am hoping to address this in a future version)

The columns of your csv file can have any order you want, just make sure you know the number of said column (indexed starting at 0), for the command line input. Also, your csv must have a header of some sort as the reader is set to skip headers. An example of what the csv file might look like is included here as test.csv and the command line inputs for the test csv file will look like this:

```console
$ python3 membranceCapacitance.py
Enter the path to your csv file: ./
Enter the name of your csv file (DO NOT INCLUDE THE EXTENSION!): test
Path exists... now I need column info about where your abf files are written
In which column is your starting file number?: 1
In which column is your ending file number?: 2
And finally, what was the frequency at which you were collecting?: 20000
```

Right now the program only works for numbered abf files (i.e. the automatic output for abf files, YYMDD###). Also, the program takes the average trace from the trace list and finds the Cm of that averaged trace. The next version is likely to aim for Cm values for all traces, plus an average. If you want to see the Cm for all individual traces, list the traces individually in your `start` column and put the trace number +1 in the corresponding `end` column.

Required packages: numpy, pandas, pyabf

TODO:
 - Find the sampling frequency automatically using the abf headers
 - Add more comments; especially in the functional scripts
 - Return Cm for all traces plus the average
 - Return Rm into the output file
 - Return taum into the output file
 - Give an optional matplotlib output for easy viewing
 - Provide options for different input/output types (e.g. json, excel files, etc.)
 - Simplify initial csv loading and reading; currently I use a csv reader as I wanted to avoid leaning on pandas too much if I didn't need to, but ended up utilizing it anyway, so I might as well make it consistent and simplify the initial csv load