import numpy as np
from scipy.stats import t


def open_and_read_file(path):
    with open(path, 'r') as f:
        method_list = f.readlines()
    aux = []
    for value in method_list:
        aux.append(float(value.split(', ')[1].replace('\n', '')))
    return np.array(aux)


def calculate_confidence_interval(method_array, confidence):
    m = method_array.mean()
    s = method_array.std()
    dof = len(method_array) - 1

    t_crit = np.abs(t.ppf((1-confidence)/2, dof))
    lower_interval, upper_interval = (m-s*t_crit/np.sqrt(len(method_array)), m+s*t_crit/np.sqrt(len(method_array)))

    return lower_interval, upper_interval


def calculate_ci_std(method_array, method_str):
    print(method_str)
    print(f'Confidence interval: {calculate_confidence_interval(method_array, 0.95)}'   )
    print(f'std: {np.std(method_array)} \n')

