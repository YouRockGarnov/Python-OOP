class ListTransaction:
    def __init__(self, the_list):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, type, value, traceback):
        raise NotImplementedError
