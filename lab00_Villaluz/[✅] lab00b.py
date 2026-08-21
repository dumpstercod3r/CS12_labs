from functools import cache

@cache
def cs12_string_count(n: int) -> int:
    if n <= 3:
        return 0

    elif n == 4:
        return 1

    else:
        n1 = cs12_string_count(n - 1)
        n2 = cs12_string_count(n - 2)
        n4 = cs12_string_count(n - 4)
        n5 = cs12_string_count(n - 5)
        n8 = cs12_string_count(n - 8)

        return 72*n1 - 1296*n2 - 3*n4 + 108*n5 - 2*n8


assert cs12_string_count(0) == 0
assert cs12_string_count(3) == 0
assert cs12_string_count(5) == 72
assert cs12_string_count(6) == 3888
assert cs12_string_count(7) == 186624
assert cs12_string_count(12) == 25389913584391