
def total_distance(l1:list[int], l2:list[int]) -> int:
    """
    Calculate the total distance between `l1` and `l2`.

    The total distance is the sum of the distances between
    each pair gotten from `l1` and `l2`, arranged in ascending
    order.

    The distance between a pair is the absolute value of their
    arithmetic difference.
    """
    pairs = zip(sorted(l1), sorted(l2))
    distances = [abs(pair[0] - pair[1]) for pair in pairs]
    return sum(distances)

def similarity_score(l1:list[int], l2:list[int]) -> int:
    """
    Calculate the similarity score of `l1` and `l2`.

    This score is the sum of the multiplication of each ID
    in `l1` and its respective frequency in `l2`.
    """
    l2_frequency = {}
    for id_ in l2:
        l2_frequency[id_] = l2_frequency.get(id_, 0) + 1

    similarity_score = sum(id_*l2_frequency.get(id_, 0) for id_ in l1)
    return similarity_score

def render_input() -> tuple[list]:
    """
    Return two lists representing the location IDs found by each of the
    group of Historians.
    """
    l1 = []
    l2 = []
    with open("input.txt") as f:
        for line in f.readlines():
            ids = line.split(" ")
            l1.append(int(ids[0].strip()))
            l2.append(int(ids[-1].strip()))

    return (l1, l2)


if __name__ == "__main__":
    location_ids = render_input()
    td = total_distance(*location_ids)
    ss = similarity_score(*location_ids)
    
    print("Total Distance:", td)
    print("Similarity Score:", ss)
