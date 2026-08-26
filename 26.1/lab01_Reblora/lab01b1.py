# pyright: strict

def outcome(a: int, b: int, c: int) -> str:
    if c == 0:
        return "Draw"
    else:
        scores: dict[str, int] = {"Daryll": pow(a, c), "Jem": pow(b, c)}
        sorted_scores: dict[str, int] = dict(sorted(scores.items(), key= lambda i: i[1], reverse=True))

        if len(set(sorted_scores.values())) == 1:
            return "Draw"
        else:
            return list(sorted_scores.keys())[0]