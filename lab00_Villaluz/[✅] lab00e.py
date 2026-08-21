def friend_groups(relations: list[tuple[str, str]]) -> list[list[str]]:
    edges: dict[str, set[str]] = {}

    for p1, p2 in relations:
        if p1 not in edges:
            edges[p1] = set()

        if p2 not in edges:
            edges[p2] = set()

        edges[p1].add(p2)
        edges[p2].add(p1)

    visited: set[str] = set()
    groups: list[list[str]] = []

    for p in edges:
        if p not in visited:
            group: list[str] = []
            to_search_list = [p]
            visited.add(p)

            while to_search_list:
                to_search = to_search_list.pop()
                group.append(to_search)
                for neighbor in edges[to_search]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        to_search_list.append(neighbor)

            groups.append(sorted(group))

    return groups

# relations2 = [("Virgilia", "Beatrice")]
# print(friend_groups(relations2))

# relations3 = [("Virgilia", "Beatrice"), ("Ronove", "Beatrice")]
# print(friend_groups(relations3))

relations4 = [("Will", "Lion"), ("Zepar", "Furfur"), ("Lion", "Erika")]
print((friend_groups(relations4)))