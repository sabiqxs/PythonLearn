from PIL import Image

kubo = Image.open("kubo.png")
area = (100, 100, 500, 400)
croppedImages = kubo.crop(area)
kubo.show()
croppedImages.show()
