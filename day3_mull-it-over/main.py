import re

def sum_uncorrupted_instructions(instructions:list[tuple[int, int]]) -> int:
    """
    Return the sum of the multiplication of all the generated
    uncorrupted instructions.
    """
    return sum((ins[0]*ins[1]) for ins in instructions)

def find_uncorrupted_instructions(memory:str) -> list[tuple[int, int]]:
    """
    Return all the uncorrupted instructions in `memory`.
    """
    pattern = r"mul\((\d+),(\d+)\)"
    instructions = []
    matches = re.finditer(pattern, memory)
    
    for match in matches:
        instructions.append(
            (
                int(match.group(1)),
                int(match.group(2))
            )
        )
    
    return instructions

def render_input() -> str:
    """
    Return a string representing the corrupted memory
    of the computer at the North Pole Toboggan Rental Shop.
    """
    with open("input.txt") as f:
        memory = f.read()
    return memory


if __name__ == "__main__":
    corrupted_memory = render_input()
    uncorrupted_instructions = find_uncorrupted_instructions(corrupted_memory)
    sum_ui = sum_uncorrupted_instructions(uncorrupted_instructions)
    print(sum_ui)
