#!/usr/bin/env python3

import csv

raw_list = []

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        raw_list.append(row[0].split(': '))

def problem_1():
    good_passwords = 0
    for row in raw_list: 
        password_chars = {}
        # get the min and max range for the values
        char_range = row[0].split()[0]
        char_min = int(char_range.split('-')[0])
        char_max = int(char_range.split('-')[1]) 
        # get the policy-defined letter
        rule = row[0].split()[1]
        # iterate through password
        for c in row[1]:
            if c in password_chars:
                password_chars[c] += 1
            else:
                password_chars[c] = 1
        if rule in password_chars and \
           password_chars[rule] >= char_min and \
           password_chars[rule] <= char_max:
            good_passwords += 1

    print(f"Number of good passwords in first problem is {good_passwords}")


def problem_2():
    good_passwords = 0
    for row in raw_list:
        # get the min and max range for the values
        char_range = row[0].split()[0]
        first_pos = int(char_range.split('-')[0]) - 1
        second_pos = int(char_range.split('-')[1]) - 1
        # get the policy-defined letter
        rule = row[0].split()[1]
        pwd = row[1]
        if pwd[first_pos] == rule and pwd[second_pos] != rule:
            good_passwords += 1
        elif pwd[first_pos] != rule and pwd[second_pos] == rule:
            good_passwords += 1

    print(f"Number of good passwords in second problem is {good_passwords}")


problem_1()
problem_2()
