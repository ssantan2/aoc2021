
def calc_fuel(steps):
    i = 1
    total_fuel = 0
    for j in range(0, steps):
        total_fuel += i
        i += 1

    return total_fuel

with open("input.txt") as f:
    lines = f.readlines()

    sorted_crabs = sorted([int(num) for num in lines[0].split(",")])

    middle = int(len(sorted_crabs)/2)
    # Find the middle which is the closet value to the average
    value_to_converge_unr = sum(sorted_crabs)/len(sorted_crabs)
    value_to_converge = round(value_to_converge_unr)
    import pdb;pdb.set_trace()

    total_fuel = 0
    for val in sorted_crabs:
        steps = abs(value_to_converge - val)
        total_fuel += calc_fuel(steps)


    print(total_fuel)

