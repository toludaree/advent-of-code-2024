from math import floor

def sum_middle_correctly_ordered_updates(rules:set[tuple[int, int]], updates:list[list[int]]) -> int:
    """
    Return the sum of the middle page in the updates that are
    correctly ordered.

    A correctly ordered update is one in which the order respects the
    page ordering rule.
    """
    return sum(
        update[floor(len(update)/2)]
        for update in find_correctly_ordered_updates(rules, updates)
    )

def find_correctly_ordered_updates(rules:set[tuple[int, int]], updates:list[list[int]]) -> list[list[int]]:
    """
    Find the page updates in `updates` that are correctly ordered.
    """
    correctly_ordered_updates = []

    for update in updates:
        if is_correctly_ordered(update, rules):
            correctly_ordered_updates.append(update)

    return correctly_ordered_updates

def is_correctly_ordered(update:list[int], rules:set[tuple[int, int]]):
    """
    Return True if update is correctly ordered.
    """
    for page_i in range(len(update)-1):
        for page in update[page_i+1:]:
            if (update[page_i], page) not in rules:
                return False
    return True

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
    page_ordering_rules, page_updates = render_input()
    print(sum_middle_correctly_ordered_updates(page_ordering_rules, page_updates))
