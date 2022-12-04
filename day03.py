from typing import NamedTuple
import string

PRIORITIES = {
    letter: priority for priority, letter in enumerate(string.ascii_letters, start=1)
}


class Rucksack(NamedTuple):
    compartment1: str
    compartment2: str

    @classmethod
    def from_str(cls, text: str):
        text = text.strip()
        split = int(len(text) / 2)
        return cls(text[:split], text[split:])

    @property
    def common_items(self) -> set[str]:
        return set(self.compartment1) & set(self.compartment2)

    @property
    def unique_items(self) -> set[str]:
        return set(self.compartment1 + self.compartment2)


with open("input/day03.txt") as f:
    rucksacks = [Rucksack.from_str(s) for s in f.readlines()]

sum(PRIORITIES[r.common_items.pop()] for r in rucksacks)

groups = [
    a.unique_items & b.unique_items & c.unique_items
    for a, b, c in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
]

sum(PRIORITIES[g.pop()] for g in groups)
