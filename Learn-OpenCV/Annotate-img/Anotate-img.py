import cv2

img = cv2.imread('D:/Github/Opencv/Learn-OpenCV/Annotate-img/input/test.jpg')

if img is None: 
     print('No img')   

# Vẽ đường trên ảnh
imageLine = img.copy()
pointA = (100, 200)
pointB = (800, 70)

# line(image, start_point, end_point, color, thickness)
cv2.line(imageLine, pointA, pointB, (255,255,0), thickness=5)
cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/line_img.jpg', imageLine)

# Vẽ đường tròn
imgCircle = img.copy()

circle_cen = (400, 400)
radius = 100

# circle(image, center_coordinates, radius, color, thickness)
cv2.circle(imgCircle, circle_cen, radius, (0, 0, 225), thickness= 5, lineType=cv2.LINE_AA)
cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/cir_img.jpg',imgCircle)

# tròn full
imgFillCir = img.copy()

# thickness = -1 là fill hình
cv2.circle(imgFillCir, circle_cen, radius, (255, 0, 0), thickness= -1, lineType=cv2.LINE_AA)
cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/cirFill_img.jpg',imgFillCir)

# chữ nhật
imgRec = img.copy()

start_point = (300, 300)
end_point = (500, 500)

# rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(imgRec, start_point, end_point, (0, 0, 225), thickness= 3, lineType=cv2.LINE_8)
cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/rec_img.jpg',imgRec)

# elip
imgEllip = img.copy()

ellip_center = (500, 500)
axis1 = (300, 200)
axis2 = (600, 450)

# ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color, thickness)
cv2.ellipse(imgEllip, ellip_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/ell_img.jpg',imgEllip)

# Thêm văn bản 
# putText(image, text, org, font, fontScale, color)
#   FONT_HERSHEY_SIMPLEX        = 0,
#   FONT_HERSHEY_PLAIN          = 1,
#   FONT_HERSHEY_DUPLEX         = 2,
#   FONT_HERSHEY_COMPLEX        = 3,
#   FONT_HERSHEY_TRIPLEX        = 4,
#   FONT_HERSHEY_COMPLEX_SMALL  = 5,
#   FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
#   FONT_HERSHEY_SCRIPT_COMPLEX = 7,
#   FONT_ITALIC                 = 16

img_text = img.copy()
text = 'JustADuck'
org = (400, 400)
cv2.putText(img_text, text, org, cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (0,0,0))

cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Annotate-img/output/text_img.jpg',img_text)