import cv2

img = cv2.imread('D:/Github/Opencv/Learn-OpenCV/Annotate-img/input/test.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)

if img is None: 
     print('No img')   

# Vẽ đường trên ảnh
imageLine = img.copy()
pointA = (100, 200)
pointB = (800, 70)

cv2.line(imageLine, pointA, pointB, (255,255,0), thickness=5)
cv2.imshow('line', imageLine)
cv2.waitKey(0)

# Vex đường tròn
imgCircle = img.copy()

circle_cen = (400, 400)

radius = 100

cv2.circle(imgCircle, circle_cen, radius, (0, 0, 225), thickness= 5, lineType=cv2.LINE_AA)

cv2.imshow("cir", imgCircle)
cv2.waitKey(0)

# tròn full
imgFillCir = img.copy()

cv2.circle(imgFillCir, circle_cen, radius, (255, 0, 0), thickness= 5, lineType=cv2.LINE_AA)
cv2.waitKey(0)

# chữ nhật
imgRec = img.copy()

start_point = (300, 300)
end_point = (500, 500)

cv2.rectangle(imgRec, start_point, end_point, (0, 0, 225), thickness= 3, lineType=cv2.LINE_8)
cv2.imshow('rec', imgRec)
cv2.waitKey(0)

# elip
imgEllip = img.copy()

ellip_center = (500, 500)
axis1 = (300, 200)
axis2 = (600, 450)

cv2.ellipse(imgEllip, ellip_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)

cv2.imshow('ellipse', imgEllip)
cv2.waitKey(0)
