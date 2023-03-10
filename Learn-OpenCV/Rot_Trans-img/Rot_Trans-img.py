import cv2

#rot-img
image = cv2.imread("D:/Github/Opencv/Learn-OpenCV/Rot_Trans-img/input/test.jpg")

height, width = image.shape[:2]
print(height, width)

center = (width/2, height/2)
print(center)

# lấy ma trận xoay bằng cv2.getRotationMatrix2D()
rotate_matrix = cv2.getRotationMatrix2D(center= center, angle= 60, scale= 1)
# hàm cv2.getRotationMatrix2D(center, angle, scale)
# với: 
# center: tâm quay của ảnh đầu vào
# angle: góc quay, angle > 0 => xoay theo chiều ngược chiều kim đồng hồ
# scale: hệ số tỉ lệ

# lấy hình ảnh xoay bằng cv2.warpAffine()
rotate_image = cv2.warpAffine(src= image, M= rotate_matrix, dsize=(width, height))

# warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
# src = ảnh nguồn
# M: ma trận biến đỏio
# dsize: kích thước ảnh đầu ra
# dts: hình ảnh đầu ra
# flags:kết hợp các phương thức nội suy như 
# INTER_LINEAR hoặc UNTER_NEAREST
# borderMode: phương pháp ngoại suy pixel
# borderValue giá trị ssuowcj sử dụng trong trường hợp đường 
# viền không đổi, có giá trị mặc định là 0
# ?????????????

cv2.imwrite("output/rot-image.jpg", rotate_image)

#trans-img
import numpy as np
# Tạo ma trận dịch
tx, ty = width / 4, height / 4

translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype= np.float32)

#sử dụng cv2.warpAffine() để dịch
translation_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))

cv2.imwrite("output/tran-image.jpg", translation_image)