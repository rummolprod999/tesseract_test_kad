import PIL.Image
import PIL.ImageEnhance
import PIL.ImageFilter
import PIL.ImageOps
import cv2
import pytesseract

filename = "305ec914-6556-411e-8200-e9ddd8af502d.png"
file_name_test = '1.png'

def tesser():
    im = PIL.Image.open(filename)
    nx, ny = im.size
    im2 = im.resize((int(nx * 5), int(ny * 5)), PIL.Image.BICUBIC)
    im2.save("temp2.png")
    imgx = PIL.Image.open('temp2.png')
    imgx = imgx.convert("RGBA")
    text = pytesseract.image_to_string(imgx, lang='rus')
    print(text)


if __name__ == '__main__':
    tesser()
