import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('frame', frame)
    c=cv2.waitKey(1)
    if c==27:
        cv2.imwrite('photo.jpg',frame)
        break
cap.release()
cv2.destroyAllWindows()

# press esc to take a capture on webcam