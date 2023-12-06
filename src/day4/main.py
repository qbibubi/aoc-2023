import re
import sys
from pathlib import Path
from pprint import pp

################################################################################


def part1(data):
    result = 0
    for line in data:
        card = line.split(': ')
        cards = card[1].split('| ')
        winning = cards[0].split()
        choices = cards[1].split()
        matching = 0
        for choice in choices:
            if choice in winning:
                if matching < 1:
                    matching += 1
                else:
                    matching *= 2
        result+=matching
    return result


################################################################################


def part2(data):
    result = 0
    for line in data:
        card = line.split(': ')
        cards = card[1].split('| ')
        winning = cards[0].split()
        choices = cards[1].split()
        matching = 0
        for choice in choices:
            if choice in winning:
                if matching < 1:
                    matching += 1
    return result


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
