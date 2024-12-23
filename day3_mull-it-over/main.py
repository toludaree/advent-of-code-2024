import re

def sum_instructions(memory:str, conditionals=False) -> int:
    """
    Return the sum of the multiplication of all the generated
    uncorrupted instructions.

    If `conditionals` is True, only consider memory sections where mul
    instructions are enabled.
    """
    return sum((ins[0]*ins[1])
               for ins in find_instructions(memory, conditionals))

def find_instructions(memory:str, conditionals=False) -> list[tuple[int, int]]:
    """
    Return all the uncorrupted instructions in `memory`.

    If `conditionals` is True, only consider memory sections where mul
    instructions are enabled.
    """
    return find_instructions_in_section(
        determine_valid_memory_sections(memory, conditionals)
    )

def find_instructions_in_section(section:str) -> list[tuple[int, int]]:
    """
    Return all the uncorrupted mul instructions within `section`.
    """
    pattern = r"mul\((\d+),(\d+)\)"
    instructions = []
    matches = re.finditer(pattern, section, re.DOTALL)
    
    for match in matches:
        instructions.append(
            (
                int(match.group(1)),
                int(match.group(2))
            )
        )
    
    return instructions

def determine_valid_memory_sections(memory:str, conditionals=False) -> str:
    """
    If `conditionals` is True, only consider sections where instructions
    are enabled. If False, return memory as-is.
    
    Instructions are enabled at the beginning and within "do()" blocks.
    """
    if not conditionals:
        return memory
    else:
        if not "EOF" in memory:
            memory_with_eof = memory + "EOF"
            beginning_section_pattern = r".*?don't\(\)"
            do_section_pattern = r"do\(\).*?don't\(\)|do\(\).*?EOF"
            
            beginning_section = [
                re.search(beginning_section_pattern,
                          memory_with_eof,
                          re.DOTALL).group()
            ]
            do_sections = re.findall(do_section_pattern, memory_with_eof, re.DOTALL)
            return "".join(beginning_section+do_sections)
        else:
            raise Exception("memory already contains EOF specifier; use another one.")

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
    sum_woc = sum_instructions(corrupted_memory, conditionals=False)
    sum_wc = sum_instructions(corrupted_memory, conditionals=True)
    print("Sum Without Conditionals:", sum_woc)
    print("Sum With Conditionals:", sum_wc)
