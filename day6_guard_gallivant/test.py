import unittest
from main import (
    count_distinct_positions,
    find_current_pos_and_dir,
    determine_next_possible_position,
    turn_right_90_deg,
)

class TestGuardGallivant(unittest.TestCase):
    def setUp(self):
        self.MAP1 = [
            list("....#....."),
            list("....^....#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#........"),
            list("........#."),
            list("#........."),
            list("......#...")
        ]

        self.MAP2 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#........"),
            list("........#."),
            list("#........."),
            list("...>..#...")
        ]

        self.MAP3 = [
            list("..#."),
            list(".#.."),
            list(">..#")
        ]

    def test_distinct_positions_1(self):
        self.assertEqual(
            count_distinct_positions(self.MAP1),
            38
        )

    def test_distinct_positions_2(self):
        self.assertEqual(
            count_distinct_positions(self.MAP2),
            3
        )

    def test_distinct_positions_3(self):
        self.assertEqual(
            count_distinct_positions(self.MAP3),
            3
        )

    def test_find_current_pos_and_dir_1(self):
        self.assertEqual(
            find_current_pos_and_dir(self.MAP1),
            ((1, 4), "^")
        )

    def test_find_current_pos_and_dir_2(self):
        self.assertEqual(
            find_current_pos_and_dir(self.MAP2),
            ((9, 3), ">")
        )

    def test_determine_next_possible_position_1(self):
        self.assertEqual(
            determine_next_possible_position(
                (6, 4), '^'
            ),
            (5, 4)
        )

    def test_determine_next_possible_position_2(self):
        self.assertEqual(
            determine_next_possible_position(
                (3, 1), '>'
            ),
            (3, 2)
        )

    def test_determine_next_possible_position_3(self):
        self.assertEqual(
            determine_next_possible_position(
                (9, 5), 'v'
            ),
            (10, 5)
        )

    def test_determine_next_possible_position_4(self):
        self.assertEqual(
            determine_next_possible_position(
                (7, 0), '<'
            ),
            (7, -1)
        )

    def test_turn_right_90_deg_1(self):
        self.assertEqual(
            turn_right_90_deg('^'),
            '>'
        )

    def test_turn_right_90_deg_2(self):
        self.assertEqual(
            turn_right_90_deg('>'),
            'v'
        )

    def test_turn_right_90_deg_3(self):
        self.assertEqual(
            turn_right_90_deg('v'),
            '<'
        )

    def test_turn_right_90_deg_4(self):
        self.assertEqual(
            turn_right_90_deg('<'),
            '^'
        )


if __name__ == "__main__":
    unittest.main()
