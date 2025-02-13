''' Ejercicio del cursillo pragmatic python impartido en MediaLab
    Enunciado: Hacer un generador de códigos QR
'''
import qrcode


# presentacion
link = "https://www.canva.com/design/DAGcxcj4h_A/DAMVSe5OS5au98bIje6hUg/view?utm_content=DAGcxcj4h_A&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h35e4843ade"
filename = "pragmatic_qr_presentacion"
extension = ".png"

img = qrcode.make(link)
img.save(filename + extension)

# github
link = "https://github.com/JotaLou/Pragmatic-Python"
filename = "pragmatic_qr_github"
extension = ".png"

img = qrcode.make(link)
img.save(filename + extension)
