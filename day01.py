from collections.abc import Iterator
from pathlib import Path

BLANK_LINE = "\n\n"


class Inventory:
    def __init__(self, items: Iterator[int]):
        self._items = list(items)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self._items!r})"

    def __iter__(self):
        return iter(self._items)

    @classmethod
    def from_str(cls, text: str):
        return Inventory(int(item) for item in text.splitlines())


with open("input/day01.txt") as f:
    inventories = f.read().split(BLANK_LINE)

calories = [sum(Inventory.from_str(inventory)) for inventory in inventories]
calories.sort(reverse=True)

assert calories[0] == 68_442
assert sum(calories[:3]) == 204_837
