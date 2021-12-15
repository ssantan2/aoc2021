



brack_map = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

brack_score_map = {
    "}": 1197,
    ")": 3,
    "]": 57,
    ">": 25137,
}


def process_line(line):
    seen = []
    score = 0
    for char in line:
        if char in brack_map.keys():
            seen.append(char)
        elif char in brack_map.values():
            last_seen =  seen.pop(-1)

            if brack_map[last_seen] != char:
                score = brack_score_map[char]
                break

    return score



with open("input.txt") as f:
    lines = f.readlines()


    score = sum(process_line(line) for line in lines)
    print(score)
