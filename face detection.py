import cv2


face_cascade=cv2.cascadeclassifier('haarcascade_frontalface_default.xml')

img=cv2.imread("C:/Users/BASIL THOMAS/Pictures/Camera Roll/2018-10-11-19-52-46-560.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiscale(gray,1.1,4)

print(type(faces))
print(faces)

for (x,y,w,h )in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Gray",img)

cv2.waitkey(0)

cv2.destroyAllWindows()
        
