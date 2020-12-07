with open("input.txt", "r") as input_file:
    tree_map = [line.rstrip() for line in input_file]

index = 0
count = 0
for line in tree_map:
    line = [c for c in line]
    if line[index] == "#":
        line[index] = 'X'
        count += 1
    else:
        line[index] = 'O'
    index += 3
    print(''.join(line))
    # we've gone over, so we need to reset the index
    # this simulates the forest "repeating"
    if index > len(line) - 1:
        index = index - len(line)

print(f"{count}")
