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
    current_card = 0
    copies = { 1: 1 }

    for line in data:
        current_card+=1
        card = line.split(': ')
        card_info = card[0].split(' ')
        card_id = card_info[1]
        cards = card[1].split('| ')

        winning = cards[0].split()
        choices = cards[1].split()

        matching = 0
        for choice in choices:
            if choice in winning:
                matching+=1
                key = current_card+matching
                copies[key] = copies.get(key, 0) + 1
        print(f"Card id: {card_id}, Key: {key}, Copies: {copies}, Matching: {matching}")
    return copies

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


# data = "  input.txt"
data = "example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
