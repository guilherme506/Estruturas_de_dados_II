from conway.game import (
    next_generation,
    next_generation_optimized,
    next_generation_integer,
    encode,
)



def test_blinker():
    initial = {
        (1, 0),
        (1, 1),
        (1, 2),
    }

    expected = {
        (0, 1),
        (1, 1),
        (2, 1),
    }

    result = next_generation(initial)

    assert result == expected


def test_block():
    initial = {
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
    }

    result = next_generation(initial)

    assert result == initial

def test_optimized_blinker():
    initial = {
        (1, 0),
        (1, 1),
        (1, 2),
    }

    expected = {
        (0, 1),
        (1, 1),
        (2, 1),
    }

    assert next_generation_optimized(initial) == expected


def test_optimized_block():
    initial = {
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
    }

    assert next_generation_optimized(initial) == initial


def test_implementations_are_equivalent():
    initial = {
        (1, 0),
        (2, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    }

    assert next_generation(initial) == next_generation_optimized(initial)

def test_integer_blinker():
    initial = {
        encode(1, 0),
        encode(1, 1),
        encode(1, 2),
    }

    expected = {
        encode(0, 1),
        encode(1, 1),
        encode(2, 1),
    }

    assert next_generation_integer(initial) == expected

def test_encode_coordinates():
    from conway.game import decode

    coordinates = [
        (0, 0),
        (10, 20),
        (-10, 30),
        (1000, -500),
    ]

    for x, y in coordinates:
        assert decode(encode(x, y)) == (x, y)
