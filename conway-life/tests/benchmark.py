from time import perf_counter

from conway.game import (
    next_generation,
    next_generation_optimized,
    next_generation_integer,
    encode,
)


def create_dense_grid(size: int) -> set[tuple[int, int]]:
    return {
        (x, y)
        for x in range(size)
        for y in range(size)
    }


def create_glider(
    offset_x: int = 0,
    offset_y: int = 0,
) -> set[tuple[int, int]]:
    pattern = {
        (1, 0),
        (2, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    }

    return {
        (x + offset_x, y + offset_y)
        for x, y in pattern
    }


def create_many_gliders(
    count: int,
) -> set[tuple[int, int]]:
    alive = set()

    for i in range(count):
        x = (i % 100) * 10
        y = (i // 100) * 10

        alive.update(create_glider(x, y))

    return alive


def create_many_gliders_integer(
    count: int,
) -> set[int]:
    alive = set()

    pattern = {
        (1, 0),
        (2, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    }

    for i in range(count):
        x = (i % 100) * 10
        y = (i // 100) * 10

        for px, py in pattern:
            alive.add(encode(x + px, y + py))

    return alive


def benchmark(
    name: str,
    function,
    alive,
    generations: int,
) -> float:
    start = perf_counter()

    for _ in range(generations):
        alive = function(alive)

    elapsed = perf_counter() - start

    print(
        f"{name:<25} "
        f"gerações={generations:<5} "
        f"tempo={elapsed:.6f}s "
        f"células={len(alive)}"
    )

    return elapsed


if __name__ == "__main__":
    print("=== 100 gliders ===")

    initial = create_many_gliders(100)

    benchmark(
        "Original",
        next_generation,
        initial,
        100,
    )

    benchmark(
        "Otimizada",
        next_generation_optimized,
        initial,
        100,
    )

    print("\n=== 1000 gliders ===")

    initial = create_many_gliders(1000)

    benchmark(
        "Original",
        next_generation,
        initial,
        100,
    )

    benchmark(
        "Otimizada",
        next_generation_optimized,
        initial,
        100,
    )

    print("\n=== Integer ===")

    initial = create_many_gliders_integer(1000)

    benchmark(
        "Integer",
        next_generation_integer,
        initial,
        100,
    )
