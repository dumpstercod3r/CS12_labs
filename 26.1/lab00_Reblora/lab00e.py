# pyright: strict

def friend_groups(friends: list[tuple[str, str]]) -> list[list[str]]:
    groups: dict[str, set[str]] = {} # key is also in val

    def _friend_groups(_friends: list[tuple[str, str]]):
        if len(_friends) == 0:
            return
        else:
            a: str = ""
            b: str = ""
            a, b = _friends[0]

            group: set[str] = groups.get(a, {a}) | groups.get(b, {b})

            for f in group:
                groups.update({f: group})

        _friend_groups(_friends[1:])

    _friend_groups(friends)       

    return sorted_groups(groups)

def sorted_groups(groups: dict[str, set[str]]) -> list[list[str]]:
    keys: list[str] = list(groups.keys())
    done: set[str] = set()
    _sorted_groups: list[list[str]] = []

    for key in keys:
        if key not in done:
            grp: list[str] = sorted(groups[key])
            _sorted_groups.append(grp)
            done.update(grp)
        else:
            pass

    return _sorted_groups