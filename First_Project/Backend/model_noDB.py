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
    for i in range (1, 5):
        cv.waitKey(1)
    
    return frame

i = 0
while True:
    print("Select what to do (1)-Store (2)-Find (3)-Analyze: ")
    control_flow = input()

    if int(control_flow) == 1:
        frame_CF = extraction(i)
        
        cv.imwrite(f"img/img{i}.jpg", frame_CF)
        i+=1


    elif int(control_flow) == 2:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img_find/img{i}.jpg", frame_CF)
        results = DeepFace.find(img_path=f"img_find/img{i}.jpg", db_path="img/")
        print(results)
        os.remove(f'img_find/img{i}.jpg')


            
    elif int(control_flow) == 3:
        frame_CF = extraction(i)
        i += 1
        cv.imwrite(f"img_analyze/img{i}.jpg", frame_CF)
        analyze = DeepFace.analyze(img_path=f"img_analyze/img{i}.jpg")
        print("Age: ", analyze[0]["age"])
        print("Gender: ", analyze[0]["gender"])
        print("Emotion: ", analyze[0]["dominant_emotion"])
        print("Race: ", analyze[0]["dominant_race"])
        os.remove(f'img_analyze/img{i}.jpg')


    else:
        #os.remove()
        break
