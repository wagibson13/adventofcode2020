with open("input.txt", "r") as input_file:
    tree_map = [line.rstrip() for line in input_file]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] 
product = 0
counts = []
for slope in slopes:
    print("### Running with slope {slope} ###") 
    index = 0
    count = 0
    line_count = 0
    for line in tree_map:
        if line_count % slope[1] != 0:
            line_count += 1
            print(line)
            continue
        line = [c for c in line]
        if line[index] == "#":
            line[index] = 'X'
            count += 1
        else:
            line[index] = 'O'
        index += slope[0]
        # print(''.join(line))
        # we've gone over, so we need to reset the index
        # this simulates the forest "repeating"
        if index > len(line) - 1:
            index = index - len(line)
        line_count += 1

    counts.append(count)
    product = product * count if product else count
    print(f"Count for slope {slope} is {count}")
    print(f"Product is currently {product}")

print(f"Counts for all slopes are {counts}")
print(f"Final product is {product}")
