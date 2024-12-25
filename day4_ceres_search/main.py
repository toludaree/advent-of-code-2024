from typing import Optional


def number_of_xmas(M:list[list[str]]) -> int:
    """
    Given a matrix of characters, return the number of times
    a valid search in `M` represents the string "XMAS".

    Informally, a search in `M` is valid when the sequence of characters
    is horizontal, vertical, diagonal, or backwards.

    Formally, if the search space of `M` is given as S, then a member s of S is valid if:
        - the length of s is 4
        - the indices of s given as `((m1,n1), (m2,n2), (m3,n3), (m4,n4))` implies that either:
            - (m1 = m2 = m3 = m4) and (n2-n1 = n3-n2 = n4-n3 = 1) or
            - (m2-m1 = m3-m2 = m4-m3 = 1) and (n1 = n2 = n3 = n4) or
            - (m2-m1 = m3-m2 = m4-m3 = 1) and (|n2-n1| = |n3-n2| = |n4-n3| = 1)
    """
    rows, columns = len(M), len(M[0])
    if columns == 0:
        return 0
    else:
        count = 0
        valid_tuples = generate_valid_tuples_of_indices(rows=rows, columns=columns)
        for tuples in valid_tuples:
            if is_xmas(M, indices=tuples):
                count += 1
        return count

def generate_valid_tuples_of_indices(rows:int, columns:int) -> set[tuple[tuple[int, int]]]:
    """
    Return a set S whose members are valid 4-tuple of indices of a matrix M.
    M has `rows` rows and `columns` columns.

    The set of all indices of the matrix M is
    ```python
    {(0,0), (0,1), ..., (0,columns-1),
     (1,0), (1,1), ..., (1,columns-1),
     ....., ....., ..., .............,
     (rows-1, 1), (rows-1, 2), ..., (rows-1, columns-1)}
     ```

    A 4-tuple of indices, s = ((m1,n1), (m2,n2), (m3,n3), (m4,n4)) is valid
    when any of the following is true:
        - (m1 = m2 = m3 = m4) and (n2-n1 = n3-n2 = n4-n3 = 1)
        - (m2-m1 = m3-m2 = m4-m3 = 1) and (n1 = n2 = n3 = n4)
        - (m2-m1 = m3-m2 = m4-m3 = 1) and (|n2-n1| = |n3-n2| = |n4-n3| = 1)
    """
    valid_tuples = set()

    for m in range(rows):
        for n in range(columns):
            valid_movements = generate_valid_movements(index=(m,n), rows=rows, columns=columns)
            valid_tuples = valid_tuples.union(valid_movements)

    return valid_tuples

def generate_valid_movements(index:tuple[int, int], rows:int, columns:int) -> set[tuple[tuple[int, int]]]:
    """
    Return a set containing 4-tuple of indices, each element representing
    a valid movement from `index`.

    Valid movements are:
        - left to right
        - up to down
        - left diagonal
        - right diagonal
    """
    valid_movements = set()

    ltr = move_left_to_right(index=index, columns=columns)
    if ltr is not None:
        valid_movements.add(ltr)
    utd = move_up_to_down(index=index, rows=rows)
    if utd is not None:
        valid_movements.add(utd)
    ld = move_left_diagonal(index=index, rows=rows, columns=columns)
    if ld is not None:
        valid_movements.add(ld)
    rd = move_right_diagonal(index=index, rows=rows, columns=columns)
    if rd is not None:
        valid_movements.add(rd)
    
    return valid_movements

def move_left_to_right(index:tuple[int, int], columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index of a matrix (m, n), return
        ((m,n), (m,n+1), (m,n+2), (m,n+3))
    
    `columns` is the number of columns in the matrix from which (m,n)
    is drawn.

    If n+3 >= `columns`, return None.
    """
    m, n = index
    if n+3 >= columns:
        return None
    else:
        return ((m,n), (m,n+1), (m,n+2), (m, n+3))
    
def move_up_to_down(index:tuple[int, int], rows:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index of a matrix (m, n), return
        ((m,n), (m+1,n), (m+2,n), (m+3,n))

    `rows` is the number of rows in the matrix from which (m,n)
    is drawn.

    If m+3 >= `rows`, return None.
    """
    m, n = index
    if m+3 >= rows:
        return None
    else:
        return ((m,n), (m+1,n), (m+2,n), (m+3, n))
    
def move_left_diagonal(index:tuple[int, int], rows:int, columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index of a matrix (m, n), return
        ((m,n), (m+1,n-1), (m+2,n-2), (m+3,n-3))

    `rows` and `columns` represents the number of rows and columns
    in the matrix from which (m,n) is drawn.

    If m+3 >= `rows` or n-3 < 0, return None.
    """
    m, n = index
    if (m+3 >= rows) or (n-3 < 0):
        return None
    else:
        return ((m,n), (m+1,n-1), (m+2,n-2), (m+3, n-3))
    
def move_right_diagonal(index:tuple[int, int], rows:int, columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index of a matrix (m, n), return
        ((m,n), (m+1,n+1), (m+2,n+2), (m+3,n+3))

    `rows` and `columns` represents the number of rows and columns
    in the matrix from which (m,n) is drawn.

    If m+3 >= `rows` or n+3 >= `columns`, return None.
    """
    m, n = index
    if (m+3 >= rows) or (n+3 >= columns):
        return None
    else:
        return ((m,n), (m+1,n+1), (m+2,n+2), (m+3, n+3))

def is_xmas(M:list[list[str]], indices:tuple[tuple[int, int]]) -> bool:
    """
    Given a matrix `M` with each row represented as a list of characters
    and `indices` a 4-tuple of valid indexes of matrix `M`,

    Return True if the location of `indices` in M represents the string
    "XMAS" or "SAMX".
    """
    character_seq = [
        M[indices[0][0]][indices[0][1]],
        M[indices[1][0]][indices[1][1]],
        M[indices[2][0]][indices[2][1]],
        M[indices[3][0]][indices[3][1]]
    ]
    string = "".join(character_seq)
    if string in ("XMAS", "SAMX"):
        return True
    return False

def render_input() -> list[list[str]]:
    """
    Return the puzzle as a matrix M of characters. Each element
    is a single-character long.

    `M[m][n]` represents the element of the matrix at row m and column n.
    """
    M = []
    with open("input.txt") as f:
        for line in f.readlines():
            row = list(line.strip())
            M.append(row)
    return M

if __name__ == "__main__":
    M = render_input()
    count_xmas = number_of_xmas(M)
    print(count_xmas)
