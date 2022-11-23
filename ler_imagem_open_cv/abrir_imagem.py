import pytesseract
import cv2

# opencv == tratamento de imagem
#tesseract == pedar dados

#passo 1: ler a imagem
imagem = cv2.imread('C:\\Curso02_github\\ler_imagem_open_cv\\rel_magalu.jpg')

caminho = r'C:\\Program Files\\Tesseract-OCR'
#passo2: pedir pro tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)
