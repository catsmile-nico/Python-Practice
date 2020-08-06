import PyPDF2, os

pdfFile = open("meetingminutes1.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdfFile)

#page count
print(reader.numPages)

#page print
page0 = reader.getPage(0)
print(page0.extractText())

# for pageNum in range(reader.numPages):
  #  print(reader.getPage(pageNum).extractText())


#combine pdf
pdfFile2 = open("meetingminutes2.pdf", "rb")
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter() # create blank pdf

for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open("combinedminutes.pdf","wb")
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFile2.close()
