

class Cave:

    def __init__(self, value):
        self.connected_caves = {}
        self.value = value
        self.is_start = value == "start"
        self.is_end = value == "end"
        self.is_big = value.lower() != value
        self.visited = {}

    def connect(self, cave):
        self.connected_caves[cave.value] = cave
        cave.connected_caves[self.value] = self

    def can_visit(self, path):
        return (self.value not in path) or self.is_big or self.is_end


class CaveSystem:

    def __init__(self, start_cave):
        self.start = start_cave
        self.paths = set()

    def _find_paths(self, cave, path):
        if not cave.can_visit(path):
            return

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

    cs.find_paths()
    print(len(cs.paths))
