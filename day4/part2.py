import re
with open("input.txt", "r") as input_file:
    passports = input_file.readlines()

req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid = 0
passport = {}

def is_valid(psport):
    valid = False
    for key in psport.keys():
        if key == "byr":
            valid = 1920 <= int(psport[key]) <= 2002
        elif key == "iyr":
            valid = 2010 <= int(psport[key]) <= 2020
        elif key == "eyr":
            valid = 2020 <= int(psport[key]) <= 2030
        elif key == "hgt":
            if psport[key][-2:] not in ['cm', 'in']:
                valid = False
            if psport[key][-2:] == "cm":
                valid = 150 <= int(psport[key][:-2]) <= 193
            elif psport[key][-2:] == "in":
                valid = 59 <= int(psport[key][:-2]) <= 76
        elif key == "hcl":
            match = re.search(r'\#[0-9a-f]{6}', psport[key])
            valid = match is not None
        elif key == "ecl":
            valid = psport[key] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == "pid":
            match = re.search(r'^[0-9]{9}$', psport[key])
            valid = match is not None
        elif key == "cid":
            valid = True
        if not valid:
            return False
    return True

for line in passports:
    # case where multiple fields are in a line
    if " " in line:
        field_vals = line.split(" ")
        fields = {x.split(":")[0]: x.split(":")[1].rstrip() for x in field_vals}
        passport.update(fields)
    # case where there's just one field
    elif line != "\n":
        passport[line.split(":")[0]] = line.split(":")[1].rstrip()
    # case where we've seen one whole passport
    else:
        if set(passport.keys()) == req_fields:
            num_valid = num_valid + 1 if is_valid(passport) else num_valid
        elif len(passport.keys()) > len(req_fields) and \
                "cid" in passport.keys():
            num_valid = num_valid + 1 if is_valid(passport) else num_valid
        passport.clear()

print(f'Number of valid passports is {num_valid}')
