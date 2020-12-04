import csv

num_list = []

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        num_list.append(int(row[0]))

    for i in range(0, len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                if num_list[i] + num_list[j] + num_list[k] == 2020:
                    print(num_list[i] * num_list[j] * num_list[k])
