import cv2
import pytesseract
import re
import json
image = cv2.imread("input/sample_invoice.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
with open("output/extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
data = {
    "invoice_number": None,
    "invoice_date": None,
    "total_amount": None
}
invoice_no = re.search(r"Invoice\s*No[:\-]?\s*(\S+)", text)
date = re.search(r"Date[:\-]?\s*(\S+)", text)
amount = re.search(r"Total[:\-]?\s*₹?\s*(\d+\.?\d*)", text)
if invoice_no:
    data["invoice_number"] = invoice_no.group(1)
if date:
    data["invoice_date"] = date.group(1)
if amount:
    data["total_amount"] = amount.group(1)
with open("output/extracted_fields.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print("OCR and field extraction completed.")
