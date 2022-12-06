def get_values_from_raw(path_raw_results):
    with open('results_mendix/raw/raw_create_results.txt', 'r+') as f:
        raw_results_create = f.readlines()
    # print(raw_results_create)
    results_create = []
    for i in range(1, 200, 2):
        results_create.append(raw_results_create[i].split(' in ')[1].split(' milliseconds. ')[0])
    return results_create


def write_results(results_path, raw_list):
    results = open(results_path, 'w+')
    for i in range(100):
        results.write(f'{i + 1}, {raw_list[i]}\n')


def write_file(method):
    result_values = get_values_from_raw(method[0])
    write_results(method[1], result_values)


if __name__ == '__main__':
    create = ['results_mendix/raw/raw_create_results.txt', 'results_mendix/create_results.txt']
    read = ['results_mendix/raw/raw_read_results.txt', 'results_mendix/read_results.txt']
    update = ['results_mendix/raw/raw_update_results.txt', 'results_mendix/update_results.txt']
    delete = ['results_mendix/raw/raw_delete_results.txt', 'results_mendix/delete_results.txt']

    write_file(delete)
