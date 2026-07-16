import cv2

# 加载人脸识别的模型文件
face_cascade = cv2.CascadeClassifier('4.OpenCV_FaceRec/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

# 加载图片
img = cv2.imread('4.OpenCV_FaceRec/image.png')

# 将图片转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 多尺度人脸检测, 1.3:每次缩放图像大小比例。越小越精细, 5:同一个区域检测到几次就算人脸
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 在图片上绘制矩形框
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()