# pyright: strict

def missing(nums: tuple[int, ...] | list[int]) -> int:
    n: int = 1
    _nums: set[int] = set(nums)

    while True:
        if n not in _nums:
            return n
        else:
            n += 1