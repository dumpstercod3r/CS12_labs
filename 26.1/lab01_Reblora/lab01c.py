# pyright: strict

def most_xp(s: int, c: int, t: int, l: int, m: int) -> int:
    max_xp: int = 0

    for torch in range(min(s, c) + 1):
        xp_gained: int = t*torch + l*((s-torch)//7) + m*((c-torch)//3)

        if max_xp < xp_gained:
            max_xp = xp_gained

    return max_xp

# TLE problems