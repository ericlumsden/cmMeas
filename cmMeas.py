import numpy as np
import pandas as pd
from getAvg import get_avg
from findEpochs import find_epochs
from findRm import find_rm_tau 

def cm_meas(path, start, end, freq):
    # First, need to convert to string in case the file names are passed in as ints
    start = str(start)
    end = str(end)

    # Now, get the time points and voltages of the seal test and the average traces using the...
    # ...find_epochs and get_avg functions (imported above)
    time_points, voltages = find_epochs(path, start)
    avg = get_avg(path, start, end)

    dV = voltages[0] - voltages[1]
    if ( (voltages[0] <= 0) and (voltages[0] < voltages[1]) ) or ( (voltages[0] > 0) and (voltages[0] > voltages[1]) ):
        dV *= -1
    
    Rs, tau_max, tau_min, tau_min_arg, tau_max_arg = find_rm_tau(avg, dV, time_points, voltages, (freq/1000))

    return ( (tau_max / Rs) + (tau_min / Rs) ) / 2, tau_min_arg, tau_max_arg