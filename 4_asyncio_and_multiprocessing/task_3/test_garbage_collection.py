import pytest
from my_module import create_objects, delete_objects  # предполагается, что ваш код находится в my_module.py


def test_objects():
    objects = create_objects(10)
    assert len(objects) == 10
    delete_objects(objects)
    assert 'objects' not in locals()
