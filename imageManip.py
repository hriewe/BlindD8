# Hayden Riewe
# Image Manipulation program for hackGSU hackathon

from PIL import Image
import sys


# Open image for manipulation

images = map(Image.open, [sys.argv[1], sys.argv[2], sys.argv[3]])
width, height = zip(*(i.size for i in images))

imageWidth = sum(width)
imageHeight = sum(height)

outputImage = Image.new('RGB', (imageWidth, imageHeight))

x_offset = 0
for im in images:
	outputImage.paste(im, (x_offset, 0))
	x_offset += im.size[0]

outputImage.save('final.png')