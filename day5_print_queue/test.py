import unittest
from main import (
    sum_middle_correctly_ordered_updates,
    find_correctly_ordered_updates,
    is_correctly_ordered
)


class TestPrintQueue(unittest.TestCase):
    PAGE_ORDERING_RULES_1 = {
        (29, 11), (15, 11), (15, 29),
        (75, 11), (75, 29), (15, 75)
    }
    PAGES_TO_PRODUCE_1 = [
        [15, 75, 29],
        [15, 29, 75],
        [75, 29, 11]
    ]
    PAGE_ORDERING_RULES_2 = {
        (47, 53), (97, 13), (97, 61), (97, 47), (75, 29),
        (61, 13), (75, 53), (29, 13), (97, 29), (53, 29),
        (61, 53), (97, 53), (61, 29), (47, 13), (75, 47),
        (97, 75), (47, 61), (75, 61), (47, 29), (75, 13),
        (53, 13)
    }
    PAGES_TO_PRODUCE_2 = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47]
    ]

    def test_sum_middle_correctly_ordered_updates_1(self):
        self.assertEqual(
            sum_middle_correctly_ordered_updates(
                self.PAGE_ORDERING_RULES_1,
                self.PAGES_TO_PRODUCE_1
            ),
            104
        )

    def test_sum_middle_correctly_ordered_updates_2(self):
        self.assertEqual(
            sum_middle_correctly_ordered_updates(
                self.PAGE_ORDERING_RULES_2,
                self.PAGES_TO_PRODUCE_2
            ),
            143
        )

    def test_find_correctly_ordered_updates_1(self):
        self.assertEqual(
            find_correctly_ordered_updates(
                self.PAGE_ORDERING_RULES_1,
                self.PAGES_TO_PRODUCE_1
            ),
            [[15, 75, 29], [75, 29, 11]]
        )

    def test_find_correctly_ordered_updates_2(self):
        self.assertEqual(
            find_correctly_ordered_updates(
                self.PAGE_ORDERING_RULES_2,
                self.PAGES_TO_PRODUCE_2
            ),
            [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]
        )

    def test_is_correctly_ordered_1(self):
        self.assertTrue(
            is_correctly_ordered(
                [15, 75, 29],
                self.PAGE_ORDERING_RULES_1
            )
        )

    def test_is_correctly_ordered_2(self):
        self.assertFalse(
            is_correctly_ordered(
                [15, 29, 75],
                self.PAGE_ORDERING_RULES_1
            )
        )

    def test_is_correctly_ordered_3(self):
        self.assertTrue(
            is_correctly_ordered(
                [97, 61, 53, 29, 13],
                self.PAGE_ORDERING_RULES_2
            )
        )

    def test_is_correctly_ordered_4(self):
        self.assertFalse(
            is_correctly_ordered(
                [61, 13, 29],
                self.PAGE_ORDERING_RULES_2
            )
        )


if __name__ == "__main__":
    unittest.main()
