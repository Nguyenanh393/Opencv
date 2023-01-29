import cv2

vid_capture = cv2.VideoCapture(0)

if (vid_capture.isOpened() == False):
    print("Error")
else:
    fps = int(vid_capture.get(5))
    print("Rate: ", fps)

    frame_count = vid_capture.get(7)
    print("Count: ", frame_count)
    currentFrame = 0
    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        
        if ret == True:
            cv2.imshow('Frame',frame)
            name = 'D:/projects/Learn-OpenCV/RW-video/RW-cam/R-cam/output/frame' + str("{:04d}".format(currentFrame)) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
            if cv2.waitKey(1) & 0xFF == ord('s') or currentFrame == 200:
                break
            
        else:
            break
vid_capture.release()
cv2.destroyAllWindows()