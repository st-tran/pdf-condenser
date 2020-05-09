import os
from wand.image import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

SIM_THRESHOLD = 0.05    # wand.image.BaseImage.similarity
RESOLUTION = 67        # in DPI

"""
Get the indices of pages in a PDF with a substantial (> SIM_THRESHOLD) amount of new content. 
"""
def filter_pages(filename, resolution=RESOLUTION):
    pages = Image(filename=filename, resolution=resolution)
    n = len(pages.sequence)
    print(n)
    print([page.similarity(pages.sequence[i+1])[1] for i, page in enumerate(pages.sequence) if i != n - 1])
    return [i for i, page in enumerate(pages.sequence) 
        if i != n - 1 and page.similarity(pages.sequence[i+1])[1] > SIM_THRESHOLD] + [n-1]

"""
Extract specific pages from a PDF and save to a new file.
"""
def save_pages(filename, page_indices):
    print(page_indices)
    with open(filename, "rb") as f:
        reader = PdfFileReader(f)
        out = PdfFileWriter()
        for i in page_indices:
            out.addPage(reader.getPage(i))

        # input stream needs to remain open
        with open(f"{os.path.splitext(filename)[0]}-condensed.pdf", "wb") as output_stream:
            out.write(output_stream)


if __name__ == "__main__":
    path = input("Enter path to pdf: ")
    save_pages(path, filter_pages(path))