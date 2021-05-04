import pyabf
import numpy as np

def find_epochs(path, start):
    time_points = []
    voltages = []

    abf = pyabf.ABF(f'{path}{start}.abf')
    for i, p1 in enumerate(abf.sweepEpochs.p1s):
        voltages.append(abf.sweepEpochs.levels[i])
        time_points.append(p1)
    tp_voltage_changes = []
    voltage_changes = []
    i = 0
    while i < len(voltages)-1:
        if voltages[i] != voltages[i+1]:
            voltage_changes.append(voltages[i])
            tp_voltage_changes.append(time_points[i])

        i += 1

    return tp_voltage_changes, voltage_changes