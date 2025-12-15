import pytest
import main


@pytest.mark.parametrize(
    "index, expected",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (7, 8),
        (8, 13),
        (9, 21),
        (10, 34),
    ],
)
def test_find_fib_iterative_valid_inputs(index, expected):
    assert main._find_fib_iterative(index) == expected


def test_find_fib_iterative_large_input():
    # Spot-check a larger Fibonacci index
    assert main._find_fib_iterative(20) == 4181
