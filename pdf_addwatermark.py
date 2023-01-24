# Add watermark to a pdf file

from PyPDF2 import PdfReader, PdfWriter

input_file = PdfReader(open('super.pdf', 'rb'))
watermark_file = PdfReader(open('wtr.pdf', 'rb'))
output_file = PdfWriter()

for i in range(len(input_file.pages)):
    page = input_file.pages[i]
    page.merge_page(watermark_file.pages[0])
    output_file.add_page(page)

with open('watermarked_output.pdf', "wb") as merged_file:
    output_file.write(merged_file)
