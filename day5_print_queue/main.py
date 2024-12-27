from math import floor

def sum_middle_correctly_ordered_updates(rules:set[tuple[int, int]], updates:list[list[int]], incorrect=False) -> int:
    """
    Return the sum of the middle page in the updates that are
    correctly ordered if `incorrect` is False.
    
    If `incorrect` is True, order the incorrectly ordered
    updates according to `rules` and return the sum of their
    middle pages.

    A correctly ordered update is one in which the order respects the
    page ordering rule.
    """
    return sum(
        update[floor(len(update)/2)]
        for update in find_correctly_ordered_updates(rules, updates, incorrect)
    )

def find_correctly_ordered_updates(rules:set[tuple[int, int]], updates:list[list[int]], incorrect=False) -> list[list[int]]:
    """
    Find the page updates in `updates` that are correctly ordered if
    `incorrect` is False.

    If `incorrect` is True,
        - find the updates that are incorrectly ordered,
        - correctly order them, and
        - return the correctly ordered version.
    """
    correctly_ordered_updates = []
    incorrectly_ordered_updates = []

    for update in updates:
        if is_correctly_ordered(update, rules):
            correctly_ordered_updates.append(update)
        else:
            incorrectly_ordered_updates.append(update)

    if not incorrect:
        return correctly_ordered_updates
    else:
        return [
            correctly_order(update, rules)
            for update in incorrectly_ordered_updates
        ]

def is_correctly_ordered(update:list[int], rules:set[tuple[int, int]]) -> bool:
    """
    Return True if update is correctly ordered.
    """
    for page_i in range(len(update)-1):
        for page in update[page_i+1:]:
            if (update[page_i], page) not in rules:
                return False
    return True

def correctly_order(update:list[int], rules:set[tuple[int, int]]) -> list[int]:
    """
    Correctly order `update` according to `rules`.
    """
    for i in range(len(update)-2, -1, -1):
        while (i+1 < len(update)) and (not (comes_before(update[i], update[i+1], rules))):
            update[i], update[i+1] = update[i+1], update[i]
            i += 1
    return update

def comes_before(page1:int, page2:int, rules:set[tuple[int, int]]) -> bool:
    """
    Return True if `page1` comes before `page2` according to `rules`. 
    """
    if (page1, page2) in rules:
        return True
    return False

def render_input() -> tuple[set[tuple[int, int]], list[list[int]]]:
    """
    Return:
        - a set of 2-tuple of ints. Each 2-tuple represent a page
        ordering rule, and
        - a list of list of strings. Each  inner list represent the pages
        to produce in each update. 
    """
    page_ordering_rules = set()
    pages_to_produce = []

    with open("input.txt") as f:
        for line in f.readlines():
            if '|' in line:
                rule = tuple(int(i) for i in line.rstrip().split('|'))
                page_ordering_rules.add(rule)
            elif ',' in line:
                page_updates = [int(i) for i in line.rstrip().split(',')]
                pages_to_produce.append(page_updates)
    
    return (page_ordering_rules, pages_to_produce)


if __name__ == "__main__":
    # page_ordering_rules, page_updates = render_input()
    PAGE_ORDERING_RULES = {
        (47, 53), (97, 13), (97, 61), (97, 47), (75, 29),
        (61, 13), (75, 53), (29, 13), (97, 29), (53, 29),
        (61, 53), (97, 53), (61, 29), (47, 13), (75, 47),
        (97, 75), (47, 61), (75, 61), (47, 29), (75, 13),
        (53, 13)
    }
    PAGES_TO_PRODUCE = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47]
    ]
    # print(sum_middle_correctly_ordered_updates(page_ordering_rules, page_updates, incorrect=True))
