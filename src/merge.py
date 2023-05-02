import os
from PyPDF2 import PdfMerger

def merge(invoiceDir, doMerge):
    if(doMerge == 'Y' or doMerge == 'y'):
        try:
            os.chdir(invoiceDir)
            x = [a for a in os.listdir() if (a.endswith(".pdf") or a.endswith(".PDF"))]

            merger = PdfMerger()

            for pdf in x:
                merger.append(open(pdf, 'rb'))

            with open(invoiceDir+"/_merged.pdf", "wb") as fout:
                merger.write(fout)
        except Exception as e:
                    print("Nothing to Merge")