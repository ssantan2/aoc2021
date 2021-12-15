



brack_map = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

brack_score_map = {
    "}": 3,
    ")": 1,
    "]": 2,
    ">": 4,
}


def process_line(line):
    seen = []
    for char in line:
        if char in brack_map.keys():
            seen.append(char)
        elif char in brack_map.values():
            last_seen =  seen.pop(-1)

            if brack_map[last_seen] != char:
                return 0

    score = 0
    for brack in seen[::-1]:
        score *= 5
        score += brack_score_map[brack_map[brack]]

    return score



with open("input.txt") as f:
    lines = f.readlines()


    scores = [process_line(line) for line in lines]
    sorted_scores = sorted([score for score in scores if score != 0])
    print(sorted_scores[int(len(sorted_scores)/2)])
