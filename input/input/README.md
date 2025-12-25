OCR DEMO

this project shows the basic functioning and a structured pipeline for extrcating text information from an sample invoice.

document type:
sample invoice taken from google.
tools used:
python
tesseract OCR
openCV

approch:
step 1. sample invoice image is used as input.
step 2. image is converted to grayscale to improve OCR readability.
step 3. text  is extracted using Tesseract OCR.
step 4. key fields such as invoice number, date, and total amount are identified using     simple pattern matching.
step 5. extracted information is structured into JSON format.

assumptions:
1.the document is in english.
2. invoice image iss clear.
3. due to time constraints and limited understanding of the topic the submission demonstrates the core .