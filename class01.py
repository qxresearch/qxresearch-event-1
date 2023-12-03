# reading image (storing image in 'img' variable) and writeing image (saving the image in detination folder)
# image location (relative path) -> "res/lena.jpg"
# destination to save images -> "result/*.jpg"

# importing OpenCV, Numpy, Matplotlib.Pyplot
import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.imread -> image read
img = cv2.imread("res/lena.jpg", -1)
# cv2.IMREAD_COLOR -> 1 --> color
# cv2.IMREAD_GRAYSCALE -> 0 --> black and white
# cv2.IMREAD_UNCHANGED -> -1 --> color + alpha scale

cv2.imshow("Image", img)

cv2.imwrite("result/lena_Unchanged.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# using plt method to display image

# cv2.imread -> B,G,R
# plt.imshow -> R,G,B 
# so we convert from B,G,R to R,G,B

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()