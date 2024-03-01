import cv2 as cv



def extraction():
    capture = cv.VideoCapture(0)
    while True:

        success, frame = capture.read()

        if not success:
            print("Erro ao ler o frame")
            print("Tente novamente")
            break
        
    
        cv.imshow("Photo", frame)
        

        key = cv.waitKey(1)
        if key == ord('q'):
            cv.imwrite('banco_de_dados', frame) #Now we need to integrate with a database later on
            break
    cv.destroyAllWindows()
    capture.release()
    return frame
