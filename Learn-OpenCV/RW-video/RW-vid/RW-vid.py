import cv2

vid_capture = cv2.VideoCapture('D:\projects\Learn-OpenCV\RW-video\RW-vid\image.mp4')

if (vid_capture.isOpened() == False):
    print("Error")
else:
    # Get frame rate information
    # ??????????????????????
    # Giá trị số 5 và 7,
    # tương ứng với tốc độ khung hình (CAP_PROP_FPS) 
    # và số khung hình ( CAP_PROP_FRAME_COUNT)
    fps = int(vid_capture.get(5))
    print("Rate: ", fps)

    frame_count = vid_capture.get(7)
    print("Count: ", frame_count)

    # Đã truy xuất siêu dữ liệu mong 
    # muốn được liên kết với tệp video
    # sẵn sàng để đọc từng khung hình ảnh từ tệp
    currentFrame = 0
    # tạo một vòng lặp và đọc từng khung hình từ 
    # luồng video bằng vid_capture.read()
    # vid_capture.read()thức trả về một tuple
    # (giá trị logic, khung hình vide thực tế)
    # giá trị logic = True => lường vid chứa khung để đọc
    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        # ret = True => có frame để đọc 
        # ret = False => không có frame => thoát khỏi vòng lặp
        if ret == True:
            # Saves image of the current frame in jpg file
            name = 'D:/projects/Learn-OpenCV/RW-video/RW-vid/output/frame' + str("{:04d}".format(currentFrame)) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
        else:
            break
vid_capture.release()
cv2.destroyAllWindows()
#https://pixabay.com/vi/videos/ch%C3%B3-s%C3%B3i-th%C3%BA-v%E1%BA%ADt-%C4%91%E1%BB%99ng-v%E1%BA%ADt-c%C3%B3-v%C3%BA-27400/