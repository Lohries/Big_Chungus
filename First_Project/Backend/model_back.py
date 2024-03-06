from deepface import DeepFace
import cv2 as cv

def main():
    print("Selecione o que fazer: ")
    control_flow = input()
    i = 0

    if control_flow == '1':
        frame = extraction()
        
        storing(frame, i)
        print("Finalizado")
        i = i + 1
       

    elif (control_flow == '2' and i >= 1):
        verification = find()
        print(verification)
        
        

    #else:
     #   analyze()



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
            print("Camera fechada")
            break
    
    cv.destroyAllWindows()
    capture.release()
    return frame

def storing(frame, i):
    cv.imwrite('img/frame{i}.jpg', frame)
    print("Frame armazenado com sucesso!")


def find():
    frame_f = extraction()
    df = DeepFace.find(frame_f, db_path='img')
    return df


#def analyze():
 #   pass


if __name__ == "__main__":
    main()
