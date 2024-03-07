from deepface import DeepFace
import cv2 as cv

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
    
    cv.destroyAllWindows()
    capture.release()
    return frame

i = 0
while True:
    control_flow = input("Select what to do (1)-Store (2)-Find (3)-Analyze): ")

    if int(control_flow) == 1:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img/img{i}.jpg", frame_CF)
      
    elif int(control_flow) == 2:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img_find/img{i}.jpg", frame_CF)
        results = DeepFace.find(img_path=f"img_find/img{i}.jpg", db_path="img/")
        print(results)
     
    elif int(control_flow) == 3:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img_analyze/img{i}.jpg", frame_CF)
        analyze = DeepFace.analyze(img_path=f"img_analyze/img{i}.jpg")
        print("Age: ", analyze["age"])
        print("Gender: ", analyze["gender"])
        print("Emotion: ", analyze["dominant_emotion"])
        print("Race: ", analyze["dominant_race"])

    else:
        break
