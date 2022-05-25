#from pdf2docx import Converter,parse
# pdf_file='demo.pdf'
# word_file='demo.docx'
# #parsemethod
# parse(pdf_file,word_file,start=0,end=None)

#cv=Converter(pdf_file)
#cv.Convert(word_file,start=0,end=None)
#cv.close()

from docx2pdf import convert
pdf_file='result.pdf'
word_file='demo.docx'
convert(word_file)