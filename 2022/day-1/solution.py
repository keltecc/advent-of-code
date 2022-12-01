#!/usr/bin/env python3

from typing import List


# https://adventofcode.com/2022/day/1


Input = List[List[int]]
Output = int


def parse(input: str) -> Input:
    lines = input.strip().splitlines()

    result = []
    current = []

    for line in lines:
        line = line.strip()

        if len(line) == 0:
            result.append(current)
            current = []
            continue

        value = int(line)
        current.append(value)

    result.append(current)

    return result


def solve(data: Input, count: int) -> Output:
    sums = [
        sum(group) for group in data
    ]
    sums.sort(reverse = True)

    result = sum(sums[:count])

    return result


def part1(test: Input, challenge: Input) -> Output:
    count = 1

    assert solve(test, count) == 24000

    return solve(challenge, count)


def part2(test: Input, challenge: Input) -> Output:
    count = 3

    assert solve(test, count) == 45000

    return solve(challenge, count)


def main():
    with open('test.txt', 'r') as file:
        test = parse(file.read())

    with open('challenge.txt', 'r') as file:
        challenge = parse(file.read())

    print('Part 1:', part1(test, challenge))
    print('Part 2:', part2(test, challenge))


if __name__ == '__main__':
    main()
