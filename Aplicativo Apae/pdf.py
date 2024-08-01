from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Cria um novo documento PDF
cnv = canvas.Canvas("teste.pdf", pagesize=A4)

# Define a fonte e o tamanho
cnv.setFont("Helvetica", 8)  # Substitua "Helvetica" pela fonte desejada e 12 pelo tamanho desejado

# Desenha uma imagem no PDF
cnv.drawImage("Imagerm.png", 12, 700, width=312, height=100)

# Adiciona texto ao PDF
cnv.drawString(80, 740, "Nome:")
cnv.drawString(110, 740, "Marcos André da Silva Malta")

cnv.drawString(80, 725, "Data:")
cnv.drawString(110, 725, "28/02/2003")

# Salva o documento PDF
cnv.save()
