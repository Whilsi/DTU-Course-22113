def load_experiments(filename:str,data_dict:dict):
    with open(filename) as infile:
        for line in infile:
            split_line = line.split()
            if split_line[0] in data_dict:
                data_dict[split_line[0]] += split_line[1:]
            else:
                data_dict[split_line[0]] = split_line[1:]

data_dict = dict()
load_experiments('test1.dat',data_dict)
load_experiments('test2.dat',data_dict)
load_experiments('test3.dat',data_dict)

avg_dict = dict()
for key in data_dict:
    n = len(data_dict[key])
    experiment_sum = 0
    for value in data_dict[key]:
        experiment_sum += float(value)
    avg_dict[key] = experiment_sum/n