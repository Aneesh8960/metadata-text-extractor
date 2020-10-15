import PyPDF2
a = PyPDF2.PdfFileReader('DPA-of-2012.pdf')
str = ""
for i in range(1, 31):
    str += a.getPage(i).extractText()

    with open("text.txt", "w", encoding='utf-8') as f:
        f.write(str)