from process_numbers import process_numbers


def test_process_numbers():
    assert process_numbers([1, 2, 3, 4, 5, -2, -4]) == 20
