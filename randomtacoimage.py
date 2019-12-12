from PIL import Image

image = Image.open('randomtaco.jpg')  # the random taco image

size = (500, 300)
out = image.resize(size)  # used the word out in lines 6-7 from the following site and this line is edit the size of
# the image:
# https://pythonexamples.org/python-pillow-resize-image/
out.save('resized-taco.jpg')  # this will save the image
