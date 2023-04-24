import os
from PyPDF2 import PdfMerger

def merge(invoiceDir, doMerge):
    os.chdir(invoiceDir)
    if(doMerge == 'Y' or doMerge == 'y'):
        x = [a for a in os.listdir() if a.endswith(".pdf")]

        merger = PdfMerger()

        for pdf in x:
            merger.append(open(pdf, 'rb'))

        with open(invoiceDir+"/_merged.pdf", "wb") as fout:
            merger.write(fout)