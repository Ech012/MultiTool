import qrcode
from PIL import Image


def make(url):
    pic = qrcode.make(url)
    pic.save("qr.png", "PNG")
    Image.open("qr.png").show()
