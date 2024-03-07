import gc


class MyObject:
    def __init__(self, name):
        self.name = name


def create_objects(n):
    return [MyObject(i) for i in range(n)]


def delete_objects(objects):
    del objects
    gc.collect()


def main(n):
    objects = create_objects(n)
    delete_objects(objects)
