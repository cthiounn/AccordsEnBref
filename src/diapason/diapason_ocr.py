import pdf2image
import pytesseract

# https://stackoverflow.com/questions/64048828/pytesseract-gives-an-error-permissionerror-winerror-5-access-is-denied
def read_and_print_pdf_with_ocr(pdf_file_path: str, lang: str = None) -> None:
    def pdf_to_img(pdf_file):
        return pdf2image.convert_from_path(pdf_file)

    def ocr_core(file):
        if lang:
            text = pytesseract.image_to_string(file, lang=lang)
        else:
            text = pytesseract.image_to_string(file)
        return text

    def print_pages(pdf_file):
        text = ""
        images = pdf_to_img(pdf_file)
        for pg, img in enumerate(images):
            text += ocr_core(img)
        return text

    return print_pages(pdf_file_path)