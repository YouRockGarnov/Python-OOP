from .cache import slow_function


def test_cache():
    results = [slow_function(i) for i in range(4)]
    assert results == [0, 1, 2, 3]

    # Проверяем, что первые два результата были удалены из кэша
    assert slow_function.cache_data == {2: 2, 3: 3}
