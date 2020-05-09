# PDF Condenser
A tool to extract pages from a PDF that add a substantial amount of new content. 

## Requirements
- Python 3.4+ and modules defined in `requirements.txt`; can be installed with `pip -r install`
- Libraries for ImageMagick
- Linux (for now)

## Usage
- Clone this repository
- Run `pdf-condenser.py` with an optional parameter of the PDF to be used (if one is not supplied, the program requests one from stdin)
- Condensed PDF is saved to the same directory as the original file with `-condensed` appended to filename
- Tips:
  - For PDFs with many pages, you may need to decrease `RESOLUTION`
  - Depending on the general content of the PDF (e.g. changing background), you may need to increase/decrease `SIM_THRESHOLD`
  - You can add this to your PATH variable to run it from wherever 

## Notes
- You may need to change the ImageMagick policies as defined in `/etc/ImageMagick-*/policy.xml` (e.g. comment out `<policy domain="coder" rights="none" pattern="PDF" />`)