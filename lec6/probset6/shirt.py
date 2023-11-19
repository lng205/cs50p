import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) != 3:
    sys.exit("Expect 2 command-line arguments")

_, ext = os.path.splitext(sys.argv[1])
_, ext2 = os.path.splitext(sys.argv[2])
ext, ext2 = ext.lower(), ext2.lower()
if ext != ext2:
    sys.exit("Input and Output not in the same type")

if not ext in [".jpg", ".jpeg", ".png"]:
    sys.exit(f"Unsupported type: {ext}")

shirt = Image.open("shirt.png")

photo = Image.open(sys.argv[1])
photo = ImageOps.fit(photo, shirt.size)

photo.paste(shirt, shirt)
photo.save(sys.argv[2])
