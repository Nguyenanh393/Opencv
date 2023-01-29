import cv2

vid_capture = cv2.VideoCapture('D:/projects/Learn-OpenCV/RW-video/RW-imgSeq/input/frame%04d.jpg')

if (vid_capture.isOpened() == False):
    print("Error")
else:
    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))

    size = (frame_width, frame_height)

    # name = name + '.mp4'
    # cap = VideoCapture(0)
    # fourcc = VideoWriter_fourcc(*'MP4V')
    # out = VideoWriter(name, fourcc, 20.0, (640,480))
    video = cv2.VideoWriter("D:\projects\Learn-OpenCV\RW-video\RW-imgSeq\output\output.mp4", 
                            cv2.VideoWriter_fourcc(*'mp4v'), 50, size)
    
    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        
        if ret == True:
            #thêm frame vào file
            video.write(frame)
        else:
            break

vid_capture.release()
video.release()

cv2.destroyAllWindows()

