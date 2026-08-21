def pearl_smoke_count(n: int, k: int) -> int:
    smoked = 0
    butts = 0

    while n > 0:
        smoked += n
        butts += n
        
        n = butts//k
        butts -= k*n

    return smoked

assert pearl_smoke_count(10, 2) == 19
assert pearl_smoke_count(4, 3) == 5
assert pearl_smoke_count(10, 3) == 14
assert pearl_smoke_count(100, 2) == 101