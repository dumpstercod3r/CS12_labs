# pyright: strict

from collections.abc import Sequence

def min_to_pass(n_tests: Sequence[int]) -> int:
    last_test: int = max([(len(n_tests)+1)*60 - sum(n_tests), 0])

    if 0 <= last_test <= 100:       # Ibuki can pass
        return last_test
    else:                           # Ibuki can't pass
        return -1