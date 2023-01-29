import cv2

img_colour = cv2.imread("D:/projects/Learn-OpenCV/RW-img/frame0108.jpg", 1)
img_grayscale = cv2.imread("D:/projects/Learn-OpenCV/RW-img/frame0108.jpg", 0)
img_unchanged = cv2.imread("D:/projects/Learn-OpenCV/RW-img/frame0108.jpg", -1)

cv2.imshow("colour", img_colour)
cv2.imshow("gray", img_grayscale)
cv2.imshow("unchanged", img_unchanged)

cv2.waitKey(0) #cố định cửa sổ win 

cv2.imwrite("grayscale.jpg", img_grayscale)
#https://pixabay.com/vi/videos/ch%C3%B3-s%C3%B3i-th%C3%BA-v%E1%BA%ADt-%C4%91%E1%BB%99ng-v%E1%BA%ADt-c%C3%B3-v%C3%BA-27400/