import cv2 as cv


capture = cv.VideoCapture(0)

while capture is open:
    sucess, frame = cv.imread(capture)
    cv.imshow("Photo", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite('img/img1.jpeg', frame)
        break
    
cv.destroyAllWindows()
capture.release()