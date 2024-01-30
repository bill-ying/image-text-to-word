OCR images from input folder and write the text to a Word document using Google's tesseract engine.  The output word document is generated in the same folder where input images are located.

Input parameters:
- input-folder (the folder containing all the image files)
- output-file (the output file with .docx extension)

The program depends on packages:
- pytesseract
- python-docx
- pillow

Following program must be installed on the computer:
- tesseract-ocr

Example:
- python image-text-to-word ~/images output.docx


The source code includes the necessary files to create a docker image.  The docker image of this program can be pulled from docker hub:
- https://hub.docker.com/r/billying/image-text-to-word

Example of running docker container:
- docker run -v ~/images:/images billying/image-text-to-word /images output.docx
