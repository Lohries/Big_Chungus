import cv2 as cv



def extraction():
    capture = cv.VideoCapture(0)
    i = 0
    while True:

        success, frame = capture.read()
        

        if not success:
            print("Erro ao ler o frame")
            print("Tente novamente")
            break
        
    
        cv.imshow("Photo", frame)
        i = i +1

        key = cv.waitKey(1)
        if key == ord('q'):
            cv.imwrite('img/Capture_Images/img{i}.jpeg', frame) #Now we need to integrate with a database later on
            break

    cv.destroyAllWindows()
    capture.release()
    return frame
