import unittest
from main import (
    count_loop_obstructions,
    count_distinct_positions,
    get_distinct_positions,
    path_becomes_loop,
    find_current_pos_and_dir,
    determine_next_possible_position,
    turn_right_90_deg,
    next_pos_is_obstacle
)

class TestGuardGallivant(unittest.TestCase):
    def setUp(self):
        self.MAP1 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
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

        # self.map1_77 = self.MAP1.copy()
        # self.map1_77[7][7] = "#"

        # self.map1_23 = self.MAP1.copy()
        # self.map1_23[2][3] = "#"

        # (7, 7)
        self.MAP4 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
            list(".......##."),
            list("#........."),
            list("......#...")
        ]

        # (2, 3)
        self.MAP5 = [
            list("....#....."),
            list(".........#"),
            list("...#......"),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
            list("........#."),
            list("#........."),
            list("......#...")
        ]

        # (7, 6)
        self.MAP6 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#..^....."),
            list("......#.#."),
            list("#........."),
            list("......#...")
        ]

        # (4, 4)
        self.MAP7 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list("....#..#.."),
            list(".........."),
            list(".#..^....."),
            list("........#."),
            list("#........."),
            list("......#...")
        ]

        # (6, 3)
        self.MAP8 = [
            list("....#....."),
            list(".........#"),
            list(".........."),
            list("..#......."),
            list(".......#.."),
            list(".........."),
            list(".#.#^....."),
            list("........#."),
            list("#........."),
            list("......#...")
        ]

    # def test_count_loop_obstructions_1(self):
    #     self.assertEqual(
    #         count_loop_obstructions(self.MAP1),
    #         6
    #     )

    # def test_count_loop_obstructions_2(self):
    #     self.assertEqual(
    #         count_loop_obstructions(self.MAP2),
    #         0
    #     )

    # def test_count_loop_obstructions_3(self):
    #     self.assertEqual(
    #         count_loop_obstructions(self.MAP3),
    #         0
    #     )
    
    def test_count_distinct_positions_1(self):
        self.assertEqual(
            count_distinct_positions(self.MAP1),
            41
        )

    def test_count_distinct_positions_2(self):
        self.assertEqual(
            count_distinct_positions(self.MAP2),
            3
        )

    def test_count_distinct_positions_3(self):
        self.assertEqual(
            count_distinct_positions(self.MAP3),
            3
        )

    def test_get_distinct_positions_1(self):
        self.assertEqual(
            get_distinct_positions(self.MAP1),
            {(3, 4), (4, 3), (5, 4), (4, 6), (8, 3), (8, 6),
             (1, 6), (2, 8), (7, 4), (6, 2), (7, 1), (7, 7),
             (6, 5), (6, 8), (4, 2), (4, 5), (5, 6), (4, 8),
             (8, 2), (9, 7), (8, 5), (2, 4), (1, 5), (1, 8),
             (6, 4), (7, 3), (6, 7), (7, 6), (5, 2), (4, 4),
             (3, 8), (8, 4), (5, 8), (8, 1), (8, 7), (1, 4),
             (1, 7), (7, 2), (6, 6), (7, 5), (6, 3)}
        )

    def test_get_distinct_positions_2(self):
        self.assertEqual(
            get_distinct_positions(self.MAP2),
            {(9, 5), (9, 3), (9, 4)}
        )

    def test_get_distinct_positions_3(self):
        self.assertEqual(
            get_distinct_positions(self.MAP3),
            {(2, 0), (2, 1), (2, 2)}
        )

    def test_path_becomes_loop_1(self):
        self.assertTrue(
            path_becomes_loop(self.MAP1, (7, 7))
        )

    def test_path_becomes_loop_2(self):
        self.assertFalse(
            path_becomes_loop(self.MAP1, (2, 3))
        )

    def test_path_becomes_loop_3(self):
        self.assertTrue(
            path_becomes_loop(self.MAP1, (7, 6))
        )

    def test_path_becomes_loop_4(self):
        self.assertFalse(
            path_becomes_loop(self.MAP1, (4, 4))
        )

    def test_path_becomes_loop_5(self):
        self.assertTrue(
            path_becomes_loop(self.MAP1, (6, 3))
        )

    def test_find_current_pos_and_dir_1(self):
        self.assertEqual(
            find_current_pos_and_dir(self.MAP1),
            ((6, 4), "^")
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

    def test_next_pos_is_obstacle_1(self):
        self.assertTrue(
            next_pos_is_obstacle(self.MAP1, (3, 1), '>')
        )

    def test_next_pos_is_obstacle_2(self):
        self.assertFalse(
            next_pos_is_obstacle(self.MAP1, (5, 4), '^')
        )

    def test_next_pos_is_obstacle_3(self):
        self.assertTrue(
            next_pos_is_obstacle(self.MAP1, (4, 8), '<')
        )


if __name__ == "__main__":
    unittest.main()
