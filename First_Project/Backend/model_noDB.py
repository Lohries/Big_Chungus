from deepface import DeepFace
import cv2 as cv
import os 


def extraction(i):
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

    capture.release()
    cv.destroyAllWindows()
    
    return frame

i = 0
while True:
    print("Select what to do (1)-Store (2)-Find (3)-Analyze): ")
    control_flow = input()

    if int(control_flow) == 1:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img/img{i}.jpg", frame_CF)
      
     
    elif int(control_flow) == 3:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img_analyze/img{i}.jpg", frame_CF)
        analyze = DeepFace.analyze(img_path=f"img_analyze/img{i}.jpg")
        print("Age: ", analyze[0]["age"])
        print("Gender: ", analyze[0]["gender"])
        print("Emotion: ", analyze[0]["dominant_emotion"])
        print("Race: ", analyze[0]["dominant_race"])

    else:
        break


