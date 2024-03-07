import pytest
from my_module import compute_squares  # предполагается, что ваш код находится в my_module.py


def test_compute_squares():
    numbers = [0, 1, 2, 3, 4]
    results = compute_squares(numbers)
    assert sorted(results) == [0, 1, 4, 9, 16]
