from document import Document, InkjetPrinter, LaserPrinter


def test_document_printing(capsys):
    document = Document()
    inkjet_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    document.print_document(inkjet_printer)
    captured = capsys.readouterr()
    assert captured.out == "Printing page on an inkjet printer\n"

    document.print_document(laser_printer)
    captured = capsys.readouterr()
    assert captured.out == "Printing page on a laser printer\n"
