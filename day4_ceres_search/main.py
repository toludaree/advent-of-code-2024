from typing import Optional


def number_of_xmas(M:list[list[str]], x_shape=False) -> int:
    """
    Given a matrix of characters:
    
    If `x_shape` is False, return the number of times a valid search in `M`
    represents the string "XMAS".

    If `x_shape` is True, return the number of times a valid search in `M`
    represents two strings, each "MAS", in the shape of an `X`.

    Informally, a search in `M` is valid when the sequence of characters
    is horizontal, vertical, diagonal, or backwards.

    If the search space of `M` is given as a set of all tuples of indices of 'M` called S,
    then s in S is valid if:

    ## x_shape is False
    - the length of s is 4
    - s = `((m1,n1), (m2,n2), (m3,n3), (m4,n4))` implies that either
        - (m1 = m2 = m3 = m4) and (n2-n1 = n3-n2 = n4-n3 = 1)
        - (m2-m1 = m3-m2 = m4-m3 = 1) and (n1 = n2 = n3 = n4)
        - (m2-m1 = m3-m2 = m4-m3 = 1) and (|n2-n1| = |n3-n2| = |n4-n3| = 1)
    ## x_shape is True
    - the length of s is 6
    - s = `((m1,n1), (m2,n2), (m3,n3), (m4,n4), (m5,n5), (m6,n6))` implies that
        - (m2,n2) = (m5,n5) = (m,n)
        - (m1,n1) = (m-1,n-1)
        - (m3,n3) = (m+1,n+1)
        - (m4,n4) = (m-1,n+1)
        - (m6,n6) = (m+1,n-1)
    """
    rows, columns = len(M), len(M[0])
    if columns == 0:
        return 0
    else:
        count = 0
        valid_tuples = generate_valid_tuples_of_indices(rows=rows, columns=columns, x_shape=x_shape)
        for tuples in valid_tuples:
            if is_xmas(M, indices=tuples, x_shape=x_shape):
                count += 1
        return count

def generate_valid_tuples_of_indices(rows:int, columns:int, x_shape=False) -> set[tuple[tuple[int, int]]]:
    """
    Return a set S whose members are valid 4|6-tuple of indices of a matrix M
    depending on `x_shape`. M has `rows` rows and `columns` columns.

    The set of all indices of the matrix M is
    ```python
    {(0,0), (0,1), ..., (0,columns-1),
     (1,0), (1,1), ..., (1,columns-1),
     ....., ....., ..., .............,
     (rows-1, 1), (rows-1, 2), ..., (rows-1, columns-1)}
     ```

    The definition of validity for any member of set S is given in the
    docstring for `number_of_xmas`.
    """
    valid_tuples = set()

    for m in range(rows):
        for n in range(columns):
            valid_movements = generate_valid_movements(index=(m,n), rows=rows, columns=columns, x_shape=x_shape)
            valid_tuples = valid_tuples.union(valid_movements)

    return valid_tuples

def generate_valid_movements(index:tuple[int, int], rows:int, columns:int, x_shape=False) -> set[tuple[tuple[int, int]]]:
    """
    Return a valid movement from a reference point `index` depending on `x_shape`.

    If `x_shape` is False, return a set containing 4-tuple of indices, each element representing
    a valid search of a matrix M.

    If `x_shape` is True, return a singleton set containing a 6-tuple of indices, representing
    a valid search of a matrix M.

    M has `rows` rows and `columns` columns. The definition of a valid search
    is given in the docstring of `number_of_xmas`.
    """
    valid_movements = set()

    if not x_shape:
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
    else:
        mx = move_x(index=index, rows=rows, columns=columns)
        if mx is not None:
            valid_movements.add(mx)
    
    return valid_movements

def move_left_to_right(index:tuple[int, int], columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index (m, n) of a matrix M, return
        ((m,n), (m,n+1), (m,n+2), (m,n+3))

    or None if
        n+3 >= `columns`
    
    `columns` represents the number of columns of M.
    """
    m, n = index
    if n+3 >= columns:
        return None
    else:
        return ((m,n), (m,n+1), (m,n+2), (m, n+3))
    
def move_up_to_down(index:tuple[int, int], rows:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index (m, n) of a matrix M, return
        ((m,n), (m+1,n), (m+2,n), (m+3,n))

    or None if
        m+3 >= `rows`

    `rows` represents the number of rows of M.
    """
    m, n = index
    if m+3 >= rows:
        return None
    else:
        return ((m,n), (m+1,n), (m+2,n), (m+3, n))
    
def move_left_diagonal(index:tuple[int, int], rows:int, columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index (m, n) of a matrix M, return
        ((m,n), (m+1,n-1), (m+2,n-2), (m+3,n-3))

    or None if
        (m+3 >= `rows`) or (n-3 < 0)

    `rows` and `columns` represents the number of rows and columns of M.
    """
    m, n = index
    if (m+3 >= rows) or (n-3 < 0):
        return None
    else:
        return ((m,n), (m+1,n-1), (m+2,n-2), (m+3, n-3))
    
def move_right_diagonal(index:tuple[int, int], rows:int, columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index (m, n) of a matrix M, return
        ((m,n), (m+1,n+1), (m+2,n+2), (m+3,n+3))

    or None if
        (m+3 >= `rows`) or (n+3 >= `columns`)

    `rows` and `columns` represents the number of rows and columns of M.
    """
    m, n = index
    if (m+3 >= rows) or (n+3 >= columns):
        return None
    else:
        return ((m,n), (m+1,n+1), (m+2,n+2), (m+3, n+3))

def move_x(index:tuple[int, int], rows:int, columns:int) -> Optional[tuple[tuple[int, int]]]:
    """
    Given an index (m, n) of a matrix M, return
        ((m-1,n-1), (m,n), (m+1,n+1), (m-1,n+1), (m,n), (m+1,n-1))

    or None if
        (m-1 < 0) or (n-1 < 0) or (m+1 >= `rows`) or (n+1 >= `columns`)

    `rows` and `columns` represents the number of rows and columns of M.
    """
    m, n = index
    if (m-1 < 0) or (n-1 < 0) or (m+1 >= rows) or (n+1 >= columns):
        return None
    else:
        return ((m-1,n-1), (m,n), (m+1,n+1), (m-1,n+1), (m,n), (m+1,n-1))

def is_xmas(M:list[list[str]], indices:tuple[tuple[int, int]], x_shape=False) -> bool:
    """
    Given a matrix `M` with each row represented as a list of characters
    and `indices` a 4|6-tuple of valid indexes of matrix `M`,

    If `x_shape` is False, return True if the location of `indices`
    in M represents the string "XMAS" or "SAMX".

    If `x_shape` is True, return True if the location of indices in M represents
    either one of the following strings:
        ("MASMAS", "MASSAM", "SAMMAS", "SAMSAM")
    """
    if not x_shape:
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
    else:
        character_seq = [
            M[indices[0][0]][indices[0][1]],
            M[indices[1][0]][indices[1][1]],
            M[indices[2][0]][indices[2][1]],
            M[indices[3][0]][indices[3][1]],
            M[indices[4][0]][indices[4][1]],
            M[indices[5][0]][indices[5][1]]
        ]
        string = "".join(character_seq)
        if string in ("MASMAS", "MASSAM", "SAMMAS", "SAMSAM"):
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
    count_xmas = number_of_xmas(M, x_shape=False)
    count_mas_x = number_of_xmas(M, x_shape=True)
    print("Number of XMAS:", count_xmas)
    print("Number of X-MAS:", count_mas_x)
