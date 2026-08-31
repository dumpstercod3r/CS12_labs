# pyright: strict

def outcome(a: int, b: int, c: int) -> str:
    if c == 0:
        return "Draw"
    elif c%2 == 0:                          # exp is even
        a, b = abs(a), abs(b)
    else:                                   # exp is odd
        pass

    if a-b == 0:
        return "Draw"
    else:
        return "Daryll" if a > b else "Jem"

# Note: ** takes longer than just comparing bases
