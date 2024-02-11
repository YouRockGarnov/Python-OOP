from .list_transaction import ListTransaction


def test_list_transaction():
    items = [1, 2, 3]
    with ListTransaction(items) as working:
        working.append(4)
        working.append(5)
    assert items == [1, 2, 3, 4, 5]

    with pytest.raises(ValueError):
        with ListTransaction(items) as working:
            working.append(6)
            working.append(7)
            raise ValueError()
    assert items == [1, 2, 3, 4, 5]  # Changes should be reverted
