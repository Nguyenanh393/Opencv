import cv2
import numpy as np

img = cv2.imread("D:/Github/Opencv/Learn-OpenCV/Resize-Img/test.jpg")

# chiều rộng và chiều cao tùy chỉnh
# resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# src: hình ảnh
# dsize: kích thước mong muốn (đầu ra)
# fx: hệ số tỉ lệ trục hoành
# fy: hệ số tỉ lệ trục tung
# interpolation: phương pháp thay đổi kích thước
# Thay đổi kích thước với

new_width = 600
new_height = 800
new_points = (new_width, new_height)

new_resized = cv2.resize(img, new_points, interpolation= cv2.INTER_LINEAR)

cv2.imshow('resize', new_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

scale = 0.5 # có thể có 2 scale khác nhau cho fx, fy
scale_img = cv2.resize(img, None, fx= scale, fy= scale, interpolation= cv2.INTER_LINEAR)

cv2.imshow('scale', scale_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# các phương pháp thay đổi kích thước:
# INTER_AREA: (phù hợp dùng để thu nhỏ) 
# những pixel xung quanh để lấy mẫu lại

# INTER_CUBIC: sử dụng phép nội suy nhị phân
# để thay đổi kích thước hình ảnh (lấy px lân cận 4x4)
# của hình ảnh, lấy trọng số trung bình của 16px để tạo px
# được nội suy mới

# INTER_LINEAR: giống INTER_CUBIC, khác: dùng lân cận 2x2 
# để lấy giá trị trung bình

# INTER_NEAREST: lấy 1 px lân cận từ hình ảnh để nội suy
# (thường phù hợp cho phóng to)

inter_nearest_img = cv2.resize(img, None, fx= scale, fy= scale, interpolation= cv2.INTER_NEAREST)
inter_linear_img = cv2.resize(img, None, fx= scale, fy= scale, interpolation= cv2.INTER_LINEAR)
inter_area_img = cv2.resize(img, None, fx= scale, fy= scale, interpolation= cv2.INTER_AREA)

vertical = np.concatenate((inter_nearest_img, inter_linear_img, inter_area_img), axis= 1)
cv2.imshow('Nearest :: Linear :: Area', vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()