with open("input.txt", "r") as input_file:
    passports = input_file.readlines()

req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid = 0
passport = set()

for line in passports:
    # case where multiple fields are in a line
    if " " in line:
        field_vals = line.split(" ")
        fields = set([x.split(":")[0] for x in field_vals])
        passport.update(fields)
    # case where there's just one field
    elif line != "\n":
        passport.add(line.split(":")[0])
    # case where we've seen one whole passport
    else:
        if passport == req_fields:
            num_valid += 1
        elif len(passport) > len(req_fields) and \
                "cid" in passport:
            num_valid += 1
        passport.clear()

print(f'Number of valid passports is {num_valid}')
