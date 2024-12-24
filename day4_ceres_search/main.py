from typing import Optional

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
