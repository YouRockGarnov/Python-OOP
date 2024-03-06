class Document:
    def print_document(self, printer):
        printer.print_page()


class InkjetPrinter:
    def print_page(self):
        print("Printing page on an inkjet printer")


class LaserPrinter:
    def print_page(self):
        print("Printing page on a laser printer")
