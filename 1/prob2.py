with open("input2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        thing = line.split(" ")
        value = int(thing[1])
        if thing[0] == "forward":
            horizontal += value
            depth += (aim * value)
        elif thing[0] == "down":
            aim += value
        elif thing[0] == "up":
            aim -= value


    print(horizontal * depth)



