import unittest
from main import (
    move_left_to_right, move_up_to_down,
    move_left_diagonal, move_right_diagonal,
    move_x,
    generate_valid_movements,
    generate_valid_tuples_of_indices,
    is_xmas, number_of_xmas
)


class TestCeresSearch(unittest.TestCase):
    M = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
         ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
         ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
         ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
         ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
         ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
         ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
         ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
         ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
         ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]

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
        self.assertIsNone(
            move_left_to_right(index=(3, 4), columns=7)
        )

    def test_move_left_to_right_4(self):
        self.assertIsNone(
            move_left_to_right(index=(4, 6), columns=7)
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
        self.assertIsNone(
            move_up_to_down(index=(3, 4), rows=5)
        )

    def test_up_to_down_4(self):
        self.assertIsNone(
            move_up_to_down(index=(7, 6), rows=8)
        )

    def test_move_left_diagonal_1(self):
        self.assertEqual(
            move_left_diagonal(index=(3, 4), rows=7, columns=7),
            ((3,4), (4,3), (5,2), (6,1))
        )

    def test_move_left_diagonal_2(self):
        self.assertIsNone(
            move_left_diagonal(index=(9, 2), rows=10, columns=10)
        )

    def test_move_left_diagonal_3(self):
        self.assertIsNone(
            move_left_diagonal(index=(4, 2), rows=10, columns=7)
        )

    def test_move_right_diagonal_1(self):
        self.assertEqual(
            move_right_diagonal(index=(3, 4), rows=10, columns=10),
            ((3,4), (4,5), (5,6), (6,7))
        )

    def test_move_right_diagonal_2(self):
        self.assertIsNone(
            move_right_diagonal(index=(9, 2), rows=10, columns=10)
        )

    def test_move_right_diagonal_3(self):
        self.assertIsNone(
            move_right_diagonal(index=(2, 7), rows=10, columns=10)
        )

    def test_move_x_1(self):
        self.assertEqual(
            move_x(index=(7,1), rows=10, columns=10),
            ((6,0), (7,1), (8,2), (6,2), (7,1), (8,0))
        )

    def test_move_x_2(self):
        self.assertIsNone(
            move_x(index=(0,4), rows=10, columns=10)
        )

    def test_generate_valid_movements_1(self):
        self.assertEqual(
            generate_valid_movements(index=(0,0), rows=7, columns=7, x_shape=False),
            {((0,0), (0,1), (0,2), (0,3)),
             ((0,0), (1,0), (2,0), (3,0)),
             ((0,0), (1,1), (2,2), (3,3))}
        )

    def test_generate_valid_movements_2(self):
        self.assertEqual(
            generate_valid_movements(index=(6,4), rows=10, columns=10),
            {((6,4), (6,5), (6,6), (6,7)),
             ((6,4), (7,4), (8,4), (9,4)),
             ((6,4), (7,3), (8,2), (9,1)),
             ((6,4), (7,5), (8,6), (9,7))}
        )

    def test_generate_valid_movements_3(self):
        self.assertEqual(
            generate_valid_movements(index=(4,9), rows=10, columns=10, x_shape=False),
            {((4,9), (5,9), (6,9), (7,9)),
             ((4,9), (5,8), (6,7), (7,6))}
        )

    def test_generate_valid_movements_4(self):
        self.assertEqual(
            generate_valid_movements(index=(8,5), rows=10, columns=10, x_shape=False),
            {((8,5), (8,6), (8,7), (8,8))}
        )

    def test_generate_valid_movements_5(self):
        self.assertEqual(
            generate_valid_movements(index=(7,7), rows=10, columns=10),
            set()
        )

    def test_generate_valid_movements_6(self):
        self.assertEqual(
            generate_valid_movements(index=(8,5), rows=10, columns=10, x_shape=True),
            {((7,4), (8,5), (9,6), (7,6), (8,5), (9,4))}
        )
    
    def test_generate_valid_movements_6(self):
        self.assertEqual(
            generate_valid_movements(index=(0,2), rows=10, columns=10, x_shape=True),
            set()
        )

    def test_generate_valid_movements_7(self):
        self.assertEqual(
            generate_valid_movements(index=(4,9), rows=10, columns=10, x_shape=True),
            set()
        )

    def test_generate_valid_movements_8(self):
        self.assertEqual(
            generate_valid_movements(index=(9,5), rows=10, columns=10, x_shape=True),
            set()
        )

    def test_generate_valid_tuples_of_indices_1(self):
        self.assertEqual(
            generate_valid_tuples_of_indices(rows=0, columns=0),
            set()
        )
    
    def test_generate_valid_tuples_of_indices_2(self):
        self.assertEqual(
            generate_valid_tuples_of_indices(rows=4, columns=4, x_shape=False),
            {((0,0), (0,1), (0,2), (0,3)),
             ((0,0), (1,0), (2,0), (3,0)),
             ((0,0), (1,1), (2,2), (3,3)),
             ((0,1), (1,1), (2,1), (3,1)),
             ((0,2), (1,2), (2,2), (3,2)),
             ((0,3), (1,3), (2,3), (3,3)),
             ((0,3), (1,2), (2,1), (3,0)),
             ((1,0), (1,1), (1,2), (1,3)),
             ((2,0), (2,1), (2,2), (2,3)),
             ((3,0), (3,1), (3,2), (3,3))}
        )

    def test_generate_valid_tuples_of_indices_3(self):
        self.assertEqual(
            generate_valid_tuples_of_indices(rows=4, columns=4, x_shape=True),
            {((0,0), (1,1), (2,2), (0,2), (1,1), (2,0)),
             ((0,1), (1,2), (2,3), (0,3), (1,2), (2,1)),
             ((1,0), (2,1), (3,2), (1,2), (2,1), (3,0)),
             ((1,1), (2,2), (3,3), (1,3), (2,2), (3,1))}
        )

    def test_is_xmas_1(self):
        self.assertTrue(
            is_xmas(self.M, ((0,5), (0,6), (0,7), (0,8)))
        )
    
    def test_is_xmas_2(self):
        self.assertFalse(
            is_xmas(self.M, ((3,1), (3,2), (3,3), (3,4)), x_shape=False)
        )

    def test_is_xmas_3(self):
        self.assertTrue(
            is_xmas(self.M, ((1,6), (2,6), (3,6), (4,6)), x_shape=False)
        )

    def test_is_xmas_4(self):
        self.assertFalse(
            is_xmas(self.M, ((4,4), (5,4), (6,4), (7,4)))
        )

    def test_is_xmas_5(self):
        self.assertTrue(
            is_xmas(self.M, ((6,4), (7,3), (8,2), (9,1)), x_shape=False)
        )

    def test_is_xmas_6(self):
        self.assertFalse(
            is_xmas(self.M, ((2,8), (3,7), (4,6), (5,5)))
        )

    def test_is_xmas_7(self):
        self.assertTrue(
            is_xmas(self.M, ((6,6), (7,7), (8,8), (9,9)))
        )

    def test_is_xmas_8(self):
        self.assertFalse(
            is_xmas(self.M, ((0,0), (1,1), (2,2), (3,3)))
        )

    def test_is_xmas_9(self):
        self.assertTrue(
            is_xmas(self.M, ((2,1), (3,2), (4,3), (2,3), (3,2), (4,1)), x_shape=True)
        )

    def test_is_xmas_10(self):
        self.assertFalse(
            is_xmas(self.M, ((5,6), (6,7), (7,8), (5,8), (6,7), (7,6)), x_shape=True)
        )

    def test_number_of_xmas_1(self):
        self.assertEqual(
            number_of_xmas([[]]),
            0
        )

    def test_number_of_xmas_2(self):
        self.assertEqual(
            number_of_xmas([['S', 'A', 'M', 'X'],
                            ['S', 'A', 'M', 'S'],
                            ['X', 'A', 'M', 'S'],
                            ['S', 'M', 'A', 'X']], x_shape=False),
            3
        )

    def test_number_of_xmas_3(self):
        self.assertEqual(
            number_of_xmas([['S', 'A', 'M', 'X'],
                            ['S', 'A', 'M', 'S'],
                            ['S', 'A', 'M', 'S'],
                            ['S', 'M', 'M', 'X']], x_shape=True),
            2
        )

    def test_number_of_xmas_4(self):
        self.assertEqual(
            number_of_xmas(self.M, x_shape=False),
            18
        )

    def test_number_of_xmas_5(self):
        self.assertEqual(
            number_of_xmas(self.M, x_shape=True),
            9
        )


if __name__ == "__main__":
    unittest.main()
