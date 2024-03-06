class ListTransaction:
    def __init__(self, the_list):
        self.the_list = the_list

    def __enter__(self):
        self.working_copy = list(self.the_list)
        return self.working_copy

    def __exit__(self, type, value, traceback):
        if type is not None:  # Exception occurred
            self.the_list[:] = self.working_copy  # Revert changes
