def parse_section(text: str) -> set[int]:
    start, stop = text.split("-")
    start, stop = int(start), int(stop) + 1  # Compensate for exclusive stop
    return set(range(start, stop))


with open("input/day04.txt") as f:
    assignment_pairs = [
        [parse_section(section) for section in pair.split(",")] for pair in f.readlines()
    ]

full_overlap = 0
any_overlap = 0

for section1, section2 in assignment_pairs:
    overlapping = section1 & section2

    if section1 == overlapping or section2 == overlapping:
        full_overlap += 1

    if overlapping:
        any_overlap += 1

assert full_overlap == 538
assert any_overlap == 792
