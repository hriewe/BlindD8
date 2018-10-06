# Hayden Riewe
# Image Manipulation program for hackGSU hackathon
# Credit to multiple stack overflow users for code snipits used throughout

from PIL import Image, ImageDraw, ImageFont, ImageChops
import sys

# This function handels the wrapping of text on the image
# Currently not useful, but keeping it just in case

def insert_newlines(string, every=42):
    return '\n'.join(string[i:i+every] for i in xrange(0, len(string), every))

# This function trims unnecesary whitespace from the image

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

# Open image for manipulation

images = map(Image.open, [sys.argv[1], sys.argv[2], sys.argv[3]])
width, height = zip(*(i.size for i in images))

imageWidth = sum(width)
imageHeight = sum(height)

# Set the image dimensions

outputImage = Image.new('RGB', (imageWidth, imageHeight))

# Default PNG is transparent, this sets background to white
pixels = outputImage.load()

for y in xrange(outputImage.size[1]): 
    for x in xrange(outputImage.size[0]): 
        if pixels[x,y][2] < 255:
            pixels[x,y] = (255, 255, 255, 255)

# Merge the three input pictures into one horizonatal picture
x_offset = 0
for im in images:
	outputImage.paste(im, (x_offset, 0))
	x_offset += im.size[0]

# Merge the bio picture underneath the horizontal pic
bio = Image.open(sys.argv[4])
outputImage.paste(bio, (10, 810))

# Trim image
outputImage = trim(outputImage)

# Save the completed image to the computer
outputImage.save('final.png')