# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from PIL import Image, ImageFilter

show = True

# #######################################
# Load image
im = Image.open("python_logo.png")
if show:
    im.show("Original image")

# #######################################
# Get image size
print(im.size)

# #######################################
# Crop image (left, upper, right, lower)
box = (100, 100, 150, 150)
region = im.crop(box)
if show:
    region.show()

# #######################################
# Rotate
region = region.transpose(Image.ROTATE_90)
# Paste to original image
im.paste(region, box)
if show:
    im.show()

# #######################################
# Convert to RGB
im = im.convert("RGB")
# Split channels
r, g, b = im.split()  # -> (r, g, b)
# Manipulate R value
r = r.point(lambda i: i*5)
# Merge channels
im = Image.merge("RGB", (r, g, b))
if show:
    im.show()

# #######################################
# Select regions where red is less than 10
mask = r.point(lambda i: i < 10 and 255)
if show:
    mask.show()

# #######################################
# Filter
out = im.filter(ImageFilter.FIND_EDGES)
if show:
    im.show()
    out.save("test.jpg")
