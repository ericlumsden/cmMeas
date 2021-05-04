import numpy as np

def find_rm_tau(av, dV, time_points, voltages, freq):
    avg = np.array(av)
    bl1 = np.average(avg[0:time_points[0]])
    bl2 = np.average(avg[time_points[-1]:])
    tp_diff = time_points[1] - time_points[0]

    rm_bl = int(0.5*tp_diff)
    rm_bl_s = time_points[0] + rm_bl

    rm_avg = np.average(avg[rm_bl_s:time_points[1]])
    
    Rs = dV / ( (bl1 - np.min(avg)) / 1000) # Needs to be in nA for the capacitance to be in pF
    if Rs < 0:
        Rs *= -1

    # Next find tau
    max_pt = np.argmax(avg)
    min_pt = np.argmin(avg)

    if voltages[0] < voltages[1]:
        tau_max_val = (avg[max_pt] - rm_avg) - ( (avg[max_pt] - rm_avg) / np.exp(1) )
        tau_max_arg = np.where(avg[max_pt:] <= (tau_max_val + rm_avg))[0][0]
        tau_max_t = tau_max_arg / freq
        tau_min_val = (avg[min_pt] - bl2) - ( (avg[min_pt] - bl2) / np.exp(1) )
        tau_min_arg = np.where(avg[min_pt:] >= (tau_min_val + bl2))[0][0]
        tau_min_t = tau_min_arg / freq
    else:
        tau_min_val = (avg[min_pt] - rm_avg) - ( (avg[min_pt] - rm_avg) / np.exp(1) )
        tau_min_arg = np.where(avg[min_pt:] >= (avg[min_pt] - tau_min_val))[0][0]
        tau_min_t = tau_min_arg / freq
        tau_max_val = (avg[max_pt] - bl2) - ( (avg[max_pt] - bl2) / np.exp(1))
        tau_max_arg = np.where(avg[max_pt:] <= (avg[max_pt] - tau_max_val))[0][0]
        tau_max_t = tau_max_arg / freq
    
    return Rs, tau_max_t, tau_min_t, tau_min_arg+min_pt, tau_max_arg+max_pt