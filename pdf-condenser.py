import os, sys
from pathlib import Path
from wand.image import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

SIM_THRESHOLD = 0.05    # wand.image.BaseImage.similarity
RESOLUTION = 67         # in DPI

"""
Get the indices of pages in a PDF with a substantial (with respect to previous page, 
similarity should be > SIM_THRESHOLD) amount of new content. 
"""
def filter_pages(filename, resolution=RESOLUTION):
    pages = Image(filename=filename, resolution=resolution)
    n = len(pages.sequence)

    # list with indices
    return [i for i, page in enumerate(pages.sequence) 
        if i != n - 1 and page.similarity(pages.sequence[i+1])[1] > SIM_THRESHOLD] + [n-1]

"""
Extract specific pages from a PDF and save to a new file.
"""
def save_pages(filename, page_indices):
    with open(filename, "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        # populate writer with pages
        for i in page_indices:
            writer.addPage(reader.getPage(i))

        # retain input stream until write is complete
        with open(f"{os.path.splitext(filename)[0]}-condensed.pdf", "wb") as output_stream:
            writer.write(output_stream)

if __name__ == "__main__":
    path = os.path.expanduser(
        input("Enter path to pdf: ") if len(sys.argv) == 1 else sys.argv[1]
    )
    save_pages(path, filter_pages(path))