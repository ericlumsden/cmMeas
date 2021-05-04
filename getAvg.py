import numpy as np
import pandas as pd
import pyabf

def get_avg(path, start, end):
    if start[3] == 0:
        date = start[:4]
        s = int(start[4:])
        e = int(end[4:])
    else:
        date = start[:3]
        s = int(start[3:])
        e = int(end[3:])


    traces = np.arange(s, e+1)
    avg = []

    if len(traces) == 1:
        avg.extend(pyabf.ABF(f'{path}/{date}{traces}.abf').sweepY)
    else:
        temp_dict = pd.DataFrame()
        for trace in traces:
            abf = pyabf.ABF(f'{path}/{date}{str(trace)}.abf')
            temp_dict[trace] = abf.sweepY
        
        #Now, average all of the traces into one trace on which the analysis will be performed
        avg = temp_dict.mean(axis=1).tolist()

    return avg