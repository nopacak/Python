import cv2


path = "Vjezbe\Photos\Algebra_greyp.jpg"
photo = cv2.imread(path)

bw_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = cascade.detectMultiScale(bw_photo, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))

print(f"We have identified {len(faces)} faces.")

for (x, y, w, h) in faces:
    cv2.rectangle(photo, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Faces found', photo)

cv2.waitKey()