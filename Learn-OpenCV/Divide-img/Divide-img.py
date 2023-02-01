import cv2
from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return (width,height)

img = cv2.imread("D:/Github/Opencv/Learn-OpenCV/Divide-img/test.png")

image_copy = img.copy() 
img_height=img.shape[0] #333
img_width=img.shape[1]  #500

#img_width, img_height = get_num_pixels("D:/Github/Opencv/Learn-OpenCV/Divide-img/test.png")

patch_height = 111
patch_width = 100
x1 = 0 # ngang
y1 = 0 # cao
 
for y in range(0, img_height, patch_height):
    for x in range(0, img_width, patch_width):
        if (img_height - y) < patch_height or (img_width - x) < patch_width:
            break
             
        y1 = y + patch_height
        x1 = x + patch_width
 
        # x1 > ngang, y1 > cao => x1 = ngang - 1, y1 = cao - 1
        if x1 >= img_width and y1 >= img_height:
            x1 = img_width - 1
            y1 = img_height - 1
            tiles = image_copy[y:y+patch_height, x:x+patch_width]
            cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Divide-img/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

        # y1 >= cao => gán y1 = cao - 1 (x không hề hấn gì)
        elif y1 >= img_height: 
            y1 = img_height - 1
            tiles = image_copy[y:y+patch_height, x:x+patch_width]
            cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Divide-img/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

        # x1 >= ngang => gán x1 = ngang - 1 (y không hề hấn gì)
        elif x1 >= img_width: 
            x1 = img_width - 1
            tiles = image_copy[y:y+patch_height, x:x+patch_width]
            cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Divide-img/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

        # x1 < ngang, y1 < cao => làm như bình thường
        else:
            tiles = image_copy[y:y+patch_height, x:x+patch_width]
            cv2.imwrite('D:/Github/Opencv/Learn-OpenCV/Divide-img/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

# lưu ảnh full hd không che :)))
cv2.imshow("Patched Image",img)
cv2.imwrite("D:/Github/Opencv/Learn-OpenCV/Divide-img/patched.jpg",img)
  
cv2.waitKey()
cv2.destroyAllWindows()