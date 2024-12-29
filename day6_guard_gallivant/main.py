
def count_distinct_positions(map_:list[list[str]]) -> int:
    """
    Return the number of distinct positions the guard crosses
    before leaving the map.
    """
    rows, columns = len(map_), len(map_[0]) 
    distinct_positions = set()

    current_pos, current_dir = find_current_pos_and_dir(map_)

    while (0 <= current_pos[0] < rows) and (0 <= current_pos[1] < columns):
        distinct_positions.add(current_pos)
        next_pos = determine_next_possible_position(current_pos, current_dir)
        if (0 <= next_pos[0] < rows) and (0 <= next_pos[1] < columns):
            map_value = map_[next_pos[0]][next_pos[1]]
            if map_value == "#":
                current_dir = turn_right_90_deg(current_dir)
            else:
                current_pos = next_pos
        else:
            break
    
    return len(distinct_positions)

def find_current_pos_and_dir(map_:list[list[str]]) -> tuple[tuple[int, int], str]:
    """
    Return the current position of the guard and the direction
    he is facing.

    The directions is one of ['^', '<', 'v', '>'].
    """
    for i, row in enumerate(map_):
        for j, column in enumerate(row):
            if (column != '.') and (column != '#'):
                return ((i, j), column)

def determine_next_possible_position(current_pos:tuple[int, int], current_dir:str) -> tuple[int, int]:
    """
    Return a new position from `current_pos`, depending on `current_dir`. 
    """
    if current_dir == '^':
        return (current_pos[0]-1, current_pos[1])
    elif current_dir == '>':
        return (current_pos[0], current_pos[1]+1)
    elif current_dir == 'v':
        return (current_pos[0]+1, current_pos[1])
    elif current_dir == '<':
        return (current_pos[0], current_pos[1]-1)

def turn_right_90_deg(current_dir:str) -> str:
    """
    Return a new direction that represents a guard
    turning right by 90 degrees.

    Directions turned right by 90 degrees:
        - '^' -> '>'
        - '>' -> 'v'
        - 'v' -> '<'
        - '<' -> '^'
    """
    if current_dir == '^':
        return '>'
    elif current_dir == '>':
        return 'v'
    elif current_dir == 'v':
        return '<'
    elif current_dir == '<':
        return '^'

def render_input() -> list[list[str]]:
    """
    Represent the map as a list of list of
    strings.
    """
    map = []
    with open("input.txt") as f:
        for line in f.readlines():
            road = list(line.rstrip())
            map.append(road)
    return map


if __name__ == "__main__":
    map_ = render_input()
    print(count_distinct_positions(map_))
