import cv2

img_colour = cv2.imread("D:/Github/Opencv/Learn-OpenCV/RW-img/test.jpg", 1)
img_grayscale = cv2.imread("D:/Github/Opencv/Learn-OpenCV/RW-img/test.jpg", 0)
img_unchanged = cv2.imread("D:/Github/Opencv/Learn-OpenCV/RW-img/test.jpg", -1)

cv2.imshow("colour", img_colour)
cv2.imshow("gray", img_grayscale)
cv2.imshow("unchanged", img_unchanged)

cv2.waitKey(0) #cố định cửa sổ win 

cv2.imwrite("grayscale.jpg", img_grayscale)