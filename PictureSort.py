import cv2		#Image processing library
import os,glob	#For os manipulation

im_fullres = 0	#Initializing counts for each category
im_facebook	= 0
im_instagram = 0
im_purpleport = 0
im_lowerres = 0

os.system("mkdir fullres")	#Creating directories for each type
os.system("mkdir facebook")
os.system("mkdir instagram")
os.system("mkdir purpleport")
os.system("mkdir lowerres")

for image in glob.glob('*.jpg'):	#Selecting images one by one
	print(image)
	img = cv2.imread(image)		#Reading image
	height, width, channel = img.shape	#getting image resolution
	if(width>=2049 and height>=100):	#Comparing image resolutions and moving them accordingly
		os.system("mv "+image+" fullres")
		im_fullres = im_fullres+1
		continue
	if(width>=2048 and height>=100):
		os.system("mv "+image+" facebook")
		im_facebook = im_facebook+1
		continue
	if(width>=1080 and height>=100):
		os.system("mv "+image+" instagram")
		im_instagram = im_instagram+1
		continue
	if(width>=900 and height>=100):
		os.system("mv "+image+" purpleport")
		im_purpleport = im_purpleport+1
		continue
	if(width>=0 and height>=100):
		os.system("mv "+image+" lowerres")
		im_lowerres = im_lowerres+1
		continue
print(im_fullres," FullRes images moved to FullRes folder")	#Printing counts for each type
print(im_facebook,"Facebook images moved to Facebook folder")
print(im_instagram," Instagram images moved to Instagram folder")
print(im_purpleport," PurplePort images moved to PurplePort folder")
print(im_lowerres," LowerRes images moved to LowerRes folder")
