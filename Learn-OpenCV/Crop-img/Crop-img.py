import cv2
from PIL import Image

img = cv2.imread('D:/Github/Opencv/Learn-OpenCV/Crop-img/test.png')

print(img.shape)

cv2.imshow("origin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped = img[150:330, 150:300]
cv2.imshow("crop", cropped)
cv2.waitKey(0)

img_copy = img.copy()
img_height = img.shape[0]
img_width = img.shape[1]

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return (width,height)

print(get_num_pixels("D:/Github/Opencv/Learn-OpenCV/Crop-img/test.png"))