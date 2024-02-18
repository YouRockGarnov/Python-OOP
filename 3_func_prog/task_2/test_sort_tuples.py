from sort_tuples import sort_tuples


def test_sort_tuples():
    tuples = [(1, 3), (3, 2), (2, 1)]
    assert sort_tuples(tuples) == [(2, 1), (3, 2), (1, 3)]
