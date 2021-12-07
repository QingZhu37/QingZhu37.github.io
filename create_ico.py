from PIL import Image
import numpy as np
import cv2

fin="qingzhu_logo.jpg"
icon_sizes = [(128,128),(256,256),(64,64)]
foutpfx="qingzhu_"

img = cv2.imread(fin)
img_resize = cv2.resize(img,(256,256))
print(img_resize.shape)

cv2.imwrite("resized_"+fin,img_resize)

img = Image.open("resized_"+fin)
icon_sizes = [(128,128),(256,256),(64,64)]
for (dx, dy) in icon_sizes:
	fnout = foutpfx+str(dx)+"x"+str(dy)+".ico"
	size_out = (dx,dy)
	print(fnout)
	img.save(fnout,sizes=[size_out])

