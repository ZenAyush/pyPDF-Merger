import os
from PyPDF2 import PdfMerger, PdfReader

input_dir = os.getcwd()
output_file = "output.pdf"

# create a PdfMerger object
merger = PdfMerger()

# loop through the files in the current working directory and append any PDF files to the merger object
for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'rb') as f:
            merger.append(PdfReader(f))

# write the merged PDF to a file
with open(output_file, "wb") as out_file:
    merger.write(out_file)

# close the merger object
merger.close()

# print a message indicating the output file location
print(f"Output file saved to {os.path.abspath(output_file)}")
