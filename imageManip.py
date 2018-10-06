# Hayden Riewe
# Image Manipulation program for hackGSU hackathon

from PIL import Image, ImageDraw, ImageFont
import sys

def insert_newlines(string, every=42):
    return '\n'.join(string[i:i+every] for i in xrange(0, len(string), every))

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

bio = sys.argv[4]
bio = insert_newlines(bio, 42)

myFont = ImageFont.truetype('/Library/Fonts/Georgia.ttf', 100)
text = ImageDraw.Draw(outputImage)
text.text((10,650), bio , font = myFont, fill=(255,255,255))

outputImage.save('final.png')