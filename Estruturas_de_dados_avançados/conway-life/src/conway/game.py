from collections import Counter


NEIGHBORS = (
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),
)
def next_generation(
    alive: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    neighbor_count = Counter()

    for x, y in alive:
        for dx, dy in NEIGHBORS:
            neighbor = (x + dx, y + dy)
            neighbor_count[neighbor] += 1

    next_alive = set()

    for cell, count in neighbor_count.items():
        if count == 3:
            next_alive.add(cell)
        elif count == 2 and cell in alive:
            next_alive.add(cell)

    return next_alive

def next_generation_optimized(
    alive: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    counts: dict[tuple[int, int], int] = {}

    for x, y in alive:
        for dx, dy in NEIGHBORS:
            cell = (x + dx, y + dy)
            counts[cell] = counts.get(cell, 0) + 1

    return {
        cell
        for cell, count in counts.items()
        if count == 3 or (count == 2 and cell in alive)
    }

