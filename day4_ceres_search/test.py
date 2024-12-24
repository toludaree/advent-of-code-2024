import unittest
from main import (
    move_left_to_right, move_up_to_down,
    move_left_diagonal, move_right_diagonal
)


class TestCeresSearch(unittest.TestCase):

    def test_move_left_to_right_1(self):
        self.assertEqual(
            move_left_to_right(index=(0, 0), columns=7),
            ((0,0), (0,1), (0,2), (0,3))
        )

    def test_move_left_to_right_2(self):
        self.assertEqual(
            move_left_to_right(index=(3, 4), columns=10),
            ((3,4), (3,5), (3,6), (3,7))
        )

    def test_move_left_to_right_3(self):
        self.assertEqual(
            move_left_to_right(index=(3, 4), columns=7),
            None
        )

    def test_move_left_to_right_4(self):
        self.assertEqual(
            move_left_to_right(index=(4, 6), columns=7),
            None
        )

    def test_up_to_down_1(self):
        self.assertEqual(
            move_up_to_down(index=(0, 0), rows=8),
            ((0,0), (1,0), (2,0), (3,0))
        )
    
    def test_up_to_down_2(self):
        self.assertEqual(
            move_up_to_down(index=(3, 4), rows=10),
            ((3,4), (4,4), (5,4), (6,4))
        )

    def test_up_to_down_3(self):
        self.assertEqual(
            move_up_to_down(index=(3, 4), rows=5),
            None
        )

    def test_up_to_down_4(self):
        self.assertEqual(
            move_up_to_down(index=(7, 6), rows=8),
            None
        )

    def test_move_left_diagonal_1(self):
        self.assertEqual(
            move_left_diagonal(index=(3, 4), rows=7, columns=7),
            ((3,4), (4,3), (5,2), (6,1))
        )

    def test_move_left_diagonal_2(self):
        self.assertEqual(
            move_left_diagonal(index=(9, 2), rows=10, columns=10),
            None
        )

    def test_move_left_diagonal_3(self):
        self.assertEqual(
            move_left_diagonal(index=(4, 2), rows=10, columns=7),
            None
        )

    def test_move_right_diagonal_1(self):
        self.assertEqual(
            move_right_diagonal(index=(3, 4), rows=10, columns=10),
            ((3,4), (4,5), (5,6), (6,7))
        )

    def test_move_right_diagonal_2(self):
        self.assertEqual(
            move_right_diagonal(index=(9, 2), rows=10, columns=10),
            None
        )

    def test_move_right_diagonal_3(self):
        self.assertEqual(
            move_right_diagonal(index=(2, 7), rows=10, columns=10),
            None
        )


if __name__ == "__main__":
    unittest.main()
