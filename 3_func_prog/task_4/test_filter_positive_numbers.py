from filter_positive_numbers import filter_positive_numbers


def test_filter_positive_numbers():
    assert filter_positive_numbers([-2, -1, 0, 1, 2]) == [1, 2]
