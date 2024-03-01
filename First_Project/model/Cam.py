import cv2 as cv

def taking_photo():
    capture = cv.VideoCapture(0)

    while True:
        confirm, video = capture.read()
        if not confirm:
            print("Falha")
            break

        cv.imshow("Sorria", video)

        key = cv.waitKey(1)
        if key == ord('q'):
            cv.imwrite('img/Capture_Images/img1.jpeg', video) 
            break
    capture.release()
    cv.destroyAllWindows()
    return video
