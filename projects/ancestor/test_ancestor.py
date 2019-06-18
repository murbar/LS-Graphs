import unittest
from ancestor import earliest_ancestor


class Test(unittest.TestCase):

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

    def test_earliest_ancestor(self):
        graph = {
            1: {3},
            2: {3},
            3: {6},
            5: {6, 7},
            4: {5, 8},
            8: {9},
            11: {8},
            10: {1}
        }
        self.assertEqual(earliest_ancestor(graph, 1), 10)
        self.assertEqual(earliest_ancestor(graph, 2), -1)
        self.assertEqual(earliest_ancestor(graph, 3), 10)
        self.assertEqual(earliest_ancestor(graph, 4), -1)
        self.assertEqual(earliest_ancestor(graph, 5), 4)
        self.assertEqual(earliest_ancestor(graph, 6), 10)
        self.assertEqual(earliest_ancestor(graph, 7), 4)
        self.assertEqual(earliest_ancestor(graph, 8), 4)
        self.assertEqual(earliest_ancestor(graph, 9), 4)
        self.assertEqual(earliest_ancestor(graph, 10), -1)
        self.assertEqual(earliest_ancestor(graph, 11), -1)


if __name__ == '__main__':
    unittest.main()
