import cv2 as cv
from deepface import DeepFace
import os 

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
    for i in range(1,5):
        cv.waitKey(1)
        
    

    return frame



def data_base_analyze(i):
  
    lista2 = []
   
    results = DeepFace.analyze(f"img_analyze/img{i}.jpg")
    if results:
        print("Age: ", results[0]["age"])
        print("Gender: ", results[0]["gender"])
        print("Emotion: ", results[0]["dominant_emotion"])
        print("Race: ", results[0]["dominant_race"])
        lista2 = [results[0]["age"], results[0]["gender"], results[0]["dominant_emotion"], results[0]["dominant_race"]]
        print(lista2)
 

    return lista2


def verify():
    frame_CF = extraction()
    cv.imwrite("img_find/img.jpg", frame_CF)
    for i in enumerate(os.listdir("img")):
        i += 1
        results = DeepFace.verify("img_find/img.jpg", f"img/img{i}.jpg")
        print(results["verify"])
        if results["verify"] == True:
            os.remove("img_find/img.jpg")
            return i
