

class Cave:

    def __init__(self, value):
        self.connected_caves = {}
        self.value = value
        self.is_start = value == "start"
        self.is_end = value == "end"
        self.is_big = value.lower() != value
        self.visit_pass = False

    def connect(self, cave):
        self.connected_caves[cave.value] = cave
        cave.connected_caves[self.value] = self

    def can_visit(self, path):
        visited = False
        times_visited = len(path.split(self.value)) - 1

        if times_visited == 2 or (times_visited == 1 and not self.visit_pass):
            visited = True

        return not visited or self.is_big or self.is_end


class CaveSystem:

    def __init__(self, start_cave):
        self.start = start_cave
        self.paths = set()

    def _find_paths(self, cave, path):
        if not cave.can_visit(path):
            return

        if path == "":
            new_path = cave.value
        else:
            new_path = path + "," + cave.value
        if cave.is_end:
            self.paths.add(new_path)
            return

        for new_cave in cave.connected_caves.values():
            self._find_paths(new_cave, new_path)

    def find_paths(self):
        self._find_paths(self.start, "")



with open("input.txt") as f:
    lines =f.readlines()

    caves = {}
    for line in lines:
        _to, _from = line.replace("\n", "").split("-")
        if _to not in caves:
            caves[_to] = Cave(_to)
        if _from not in caves:
            caves[_from] = Cave(_from)

        caves[_to].connect(caves[_from])

    start_cave = caves["start"]
    cs = CaveSystem(start_cave)

    for cave in caves.values():
        if not cave.is_big and not cave.is_start and not cave.is_end:
            cave.visit_pass = True
            cs.find_paths()
            cave.visit_pass = False
    print(len(cs.paths))
