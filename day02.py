import itertools
from enum import IntEnum
from typing import NamedTuple


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


OpponentShape = Shape
PlayerShape = Shape

RULES: dict[tuple[OpponentShape, PlayerShape], Outcome] = {
    (Shape.ROCK, Shape.ROCK): Outcome.DRAW,
    (Shape.ROCK, Shape.PAPER): Outcome.WIN,
    (Shape.ROCK, Shape.SCISSORS): Outcome.LOSS,
    (Shape.PAPER, Shape.PAPER): Outcome.DRAW,
    (Shape.PAPER, Shape.SCISSORS): Outcome.WIN,
    (Shape.PAPER, Shape.ROCK): Outcome.LOSS,
    (Shape.SCISSORS, Shape.SCISSORS): Outcome.DRAW,
    (Shape.SCISSORS, Shape.ROCK): Outcome.WIN,
    (Shape.SCISSORS, Shape.PAPER): Outcome.LOSS,
}


class Round(NamedTuple):
    opponent: Shape
    player: Shape

    @property
    def outcome(self):
        return RULES[self]

    @property
    def score(self):
        return self.player + self.outcome


# -------- Part 1 -------------------------------------------------------------


def parse_round(text: str) -> Round:
    opponent, player = text.strip().split()
    translate = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": Shape.ROCK,
        "Y": Shape.PAPER,
        "Z": Shape.SCISSORS,
    }
    return Round(translate[opponent], translate[player])


with open("input/day02.txt") as f:
    plays = [parse_round(s) for s in f.readlines()]

assert sum(p.score for p in plays) == 11_873


# -------- Part 2 -------------------------------------------------------------

_cheat_rules = {
    (opponent, outcome): player for (opponent, player), outcome in RULES.items()
}


def parse_round(text: str) -> Round:
    opponent, outcome = text.strip().split()
    translate = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": Outcome.LOSS,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }
    opponent, outcome = translate[opponent], translate[outcome]
    return Round(opponent, _cheat_rules[opponent, outcome])


with open("input/day02.txt") as f:
    plays = [parse_round(s) for s in f.readlines()]

assert sum(p.score for p in plays) == 12_014
