import cv2
from helperFunctions import *
from definitions import *

#for name in cover_names:
#    sizes = getSize(save_path_cut+name)
#    if sizes[0] != sizes[1]:
#        print(name+": different")
#    else:
#        print(name+": same")


img = cv2.imread(save_path_cut+"001.jpg")
img2 = img
img2[:,:] = [0, 0, 0]
cv2.imwrite(save_path_cut+"000.jpg", img2)

img3 = 100*[100*[[0,0,0]]]
print(img3)
