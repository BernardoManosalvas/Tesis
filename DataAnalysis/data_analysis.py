import numpy as np
from utils import open_and_read_file, calculate_ci_std

create_results_mendix = open_and_read_file('./results_mendix/create_results.txt')
read_results_mendix = open_and_read_file('./results_mendix/read_results.txt')
update_results_mendix = open_and_read_file('./results_mendix/update_results.txt')
delete_results_mendix = open_and_read_file('./results_mendix/delete_results.txt')

create_results_outsystems = open_and_read_file('results_outsystems/create_results.txt')
read_results_outsystems = open_and_read_file('./results_outsystems/read_results.txt')
update_results_outsystems = open_and_read_file('./results_outsystems/update_results.txt')
delete_results_outsystems = open_and_read_file('./results_outsystems/delete_results.txt')

calculate_ci_std(create_results_outsystems, "CREATE_OUTSYSTEMS")
calculate_ci_std(read_results_outsystems, "READ_OUTSYSTEMS")
calculate_ci_std(update_results_outsystems, "UPDATE_OUTSYSTEMS")
calculate_ci_std(delete_results_outsystems, "DELETE_OUTSYSTEMS")
