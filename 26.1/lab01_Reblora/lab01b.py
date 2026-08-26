# pyright: strict

def outcome(a: int, b: int, c: int) -> str:
    if c == 0:
        return "Draw"
    else:
        daryll: int = a**c
        jem: int = b**c

        if daryll == jem:
            return "Draw"
        elif daryll > jem:
            return "Daryll"
        else:
            return "Jem"