class Document:
    def print_document(self, printer):
        raise NotImplementedError


class InkjetPrinter:
    def print_page(self):
        raise NotImplementedError


class LaserPrinter:
    def print_page(self):
        raise NotImplementedError
