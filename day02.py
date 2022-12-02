import itertools
from enum import Enum
from typing import NamedTuple


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


OpponentShape = Shape
PlayerShape = Shape

PLAYS: dict[tuple[OpponentShape, PlayerShape], Outcome] = {
    (Shape.ROCK, Shape.ROCK): Outcome.DRAW,
    (Shape.ROCK, Shape.PAPER): Outcome.WIN,
    (Shape.ROCK, Shape.SCISSORS): Outcome.LOSS,
    (Shape.PAPER, Shape.PAPER): Outcome.DRAW,
    (Shape.PAPER, Shape.ROCK): Outcome.LOSS,
    (Shape.PAPER, Shape.SCISSORS): Outcome.WIN,
    (Shape.SCISSORS, Shape.SCISSORS): Outcome.DRAW,
    (Shape.SCISSORS, Shape.ROCK): Outcome.WIN,
    (Shape.SCISSORS, Shape.PAPER): Outcome.LOSS,
}


class Round(NamedTuple):
    opponent: Shape
    player: Shape

    @property
    def outcome(self):
        return PLAYS[self]

    @property
    def score(self):
        return self.player.value + self.outcome.value


# -------- Part 1 -------------------------------------------------------------


def parse_round(text: str) -> Round:
    opponent, player = text.strip().split(" ")
    mapping = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": Shape.ROCK,
        "Y": Shape.PAPER,
        "Z": Shape.SCISSORS,
    }
    return Round(mapping[opponent], mapping[player])


with open("input/day02.txt") as f:
    plays = [parse_round(i) for i in f.readlines()]

assert sum(p.score for p in plays) == 11873


# -------- Part 2 -------------------------------------------------------------

_fixed_plays = {
    (opponent, outcome): player for (opponent, player), outcome in PLAYS.items()
}


def parse_round(text: str) -> Round:
    opponent, outcome = text.strip().split(" ")
    mapping = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": Outcome.LOSS,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }
    opponent, outcome = mapping[opponent], mapping[outcome]
    return Round(opponent, _fixed_plays[opponent, outcome])


with open("input/day02.txt") as f:
    plays = [parse_round(i) for i in f.readlines()]

assert sum(p.score for p in plays) == 12014
