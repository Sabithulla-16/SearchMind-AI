import fitz


class PDFLoader:

    def load(
        self,
        path: str,
    ):

        return fitz.open(path)


pdf_loader = PDFLoader()