import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import topological_sort


def create_pairs(s):
    return [x.split('-') for x in s.split()]


class TestReadPairs(unittest.TestCase):

    Input = 'A B C\nD E   F G\n\n H I'

    def test_read_words(self):
        actual = list(topological_sort.get_words(StringIO(self.Input)))
        expected = 'A B C D E F G H I'.split()
        self.assertListEqual(expected, actual)

    def test_read_pairs(self):
        actual = list(topological_sort.read_pairs(StringIO(self.Input)))
        expected = [ ('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H') ]
        self.assertListEqual(expected, actual)


class TestTopoligicalSort(unittest.TestCase):

    Pairs = 'A-A B-C C-D C-E D-G F-E E-D B-G H-H'

    def test_make_table(self):
        actual = topological_sort.make_table(create_pairs(self.Pairs))
        expected = {'A': [0, []], 'C': [1, ['D', 'E']], 'B': [0, ['C', 'G']], 'E': [2, ['D']], 'D': [2, ['G']], 'G': [2, []], 'F': [0, ['E']], 'H': [0, []]}
        self.assertDictEqual(expected, actual)

    def test_topological_sort(self):
        actual = list(topological_sort.topological_sort(create_pairs(self.Pairs)))
        for x, y in [ ('B', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'G'),
                      ('F', 'D'), ('A', 'E'), ('H', 'G'), ('B', 'E') ]:
            self.assertLess(actual.index(x), actual.index(y), 'Order error')

    def test_cycle_graph(self):
        with self.assertRaises(topological_sort.CycleError):
            list(topological_sort.topological_sort(create_pairs('X-X A-B Y-Y B-C D-E C-A')))


if __name__ == '__main__':
    unittest.main()
