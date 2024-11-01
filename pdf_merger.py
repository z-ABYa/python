from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["Exercises/clutteredFolder/a.pdf", "Exercises/clutteredFolder/b.pdf"]:
    merger.append(pdf)

merger.write("Exercises/clutteredFolder/merged-pdf.pdf")
merger.close()