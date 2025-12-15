import sys


def _find_fib_recursive(x: int):
    if x == 1:
        return 0
    if x == 2:
        return 1

    return _find_fib_recursive(x - 1) + _find_fib_recursive(x - 2)


def _find_fib_iterative(x: int) -> int:
    # 0, 1, 1, 2, 3, 5, 8, 13...

    base = 1
    prev = 0

    if x == 1:
        return 0
    if x == 2:
        return 1

    for i in range(2, x):
        next_num = base + prev
        prev = base
        base = next_num
    return next_num


if __name__ == '__main__':
  fib_index = int(sys.argv[1])
  print(_find_fib_iterative(fib_index))
