# pyright: strict

def pearl_smoke_count(n: int, k: int) -> int:
    smoke_count: int = 0

    while n > 0:
        n -= 1
        smoke_count += 1

        if smoke_count % k == 0:
            smoke_count += 1

    return smoke_count