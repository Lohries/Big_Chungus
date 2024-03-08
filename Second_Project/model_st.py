from deepface import DeepFace
import cv2 as cv


     
def analyze():
    
    i += 1
    cv.imwrite(f"img_analyze/img{i}.jpg", frame_CF)
    analyze = DeepFace.analyze(img_path=f"img_analyze/img{i}.jpg")
    print("Age: ", analyze[0]["age"])
    print("Gender: ", analyze[0]["gender"])
    print("Emotion: ", analyze[0]["dominant_emotion"])
    print("Race: ", analyze[0]["dominant_race"])


