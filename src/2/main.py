import re
import sys
from pathlib import Path
from pprint import pp

################################################################################


def part1(data):
    sum = 0
    for line in data:
        match = re.search(r'Game\s([\d]{1,3})', line)
        id = int(match.group(1))
        bad = False

        game = line.split(': ')
        for info in game[1].split('; '):
            set = info.split(', ')
            for value, color in (pair.split(' ') for pair in set):
                value = int(value)
                if value>12 and color=="red" or value>13 and color=="green" or value>14 and color=="blue":
                    bad = True
                    break;
            if bad:
                break;
        if not bad:
            sum+=id
    return sum


################################################################################



def part2(data):
    product = 0
    for line in data:
        match = re.search(r'Game\s([\d]{1,3})', line)
        id = int(match.group(1))

        minimum_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        game = line.split(': ')
        for info in game[1].split('; '):
            set = info.split(', ')
            for value, color in (pair.split(' ') for pair in set):
                value = int(value)

                if color == "red" and value > minimum_colors["red"]:
                    minimum_colors["red"] = value
                elif color == "green" and value > minimum_colors["green"]:
                    minimum_colors["green"] = value
                elif color == "blue" and value > minimum_colors["blue"]:
                    minimum_colors["blue"] = value

        product+=minimum_colors["red"] * minimum_colors["green"] * minimum_colors["blue"] 
    return product



################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()

    # data = [(x, int(y)) for x, y in data]
    # data = [[[int(x) for x in y] for y in line] for line in data]
    # data = [[int(x) for x in line] for line in data]
    # data = [[x for x in line] for line in data]
    # data = [[x.split(",") for x in line] for line in data]
    # data = [line.split(" ") for line in data]
    # data = [line.split(",") for line in data]
    data = [line.strip("\n") for line in data]
    # data = [x.split(" -> ") for x in data]
    # data = [x[0] for x in data]

    return data


data = "input.txt"
# data = "example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
