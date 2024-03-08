import os
import sys
import argparse

import pytesseract
from PIL import Image
from docx import Document


def main(input_folder, output_file):
    document = Document()

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image = Image.open(os.path.join(input_folder, filename))
            text = pytesseract.image_to_string(image)
            document.add_paragraph(text)

    document.save(os.path.join(input_folder, output_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description
                                     ='OCR images (png or jpg) of the input folder, and write the text to a '
                                      'Word document.')
    parser.add_argument('input_folder', help='the input directory for images')
    parser.add_argument('output_file', help='the Word output file with docx extension.')
    args = parser.parse_args()
    sys.exit(main(args.input_folder, args.output_file))
