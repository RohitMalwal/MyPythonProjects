import os
from PyPDF2 import PdfWriter

os.chdir('D:/pdf merger')

x = os.listdir()
merger = PdfWriter()

for pdf in x:
    merger.append(pdf)

merger.write("merged PDF.pdf")
merger.close()

# input_1 = open('pypdf mergerr.pdf', 'rb')
# input_2 = open('pypdf2 mergerr.pdf', 'rb')

# merger.append(fileobj=input_1, pages=(0,2))
# merger.merge(position=2, fileobj=input_2, pages=(0,2))
# merger.merge(position=3, fileobj=input_1, pages=(2,4))
# merger.merge(position=4, fileobj=input_2, pages=(2,3))

# output = open('merger_done.pdf', 'wb')
# merger.write(output)

# merger.close()
# output.close()