from deepface import DeepFace
import os

def data_base_analyze(data):
    directory = "img"
    lista2 = []
    for i, file in enumerate(os.listdir(directory)):
        results = DeepFace.analyze(f"img/img{i+1}.jpg")
        if results:
            print("Age: ", results[0]["age"])
            print("Gender: ", results[0]["gender"])
            print("Emotion: ", results[0]["dominant_emotion"])
            print("Race: ", results[0]["dominant_race"])
            points = 0
            if results[0]["dominant_emotion"] == data[0]:
                points = 1 + points
            if results[0]["age"] == data[1]:
                points = 1 + points 
            if results[0]["gender"] == data[2]:
                points = points + 5
            if results[0]["dominant_race"] == data[3]:
                points = points + 1
            
            lista2.append(points)
            print(lista2)
    big_matching = max(lista2)
    index = lista2.index(big_matching)
    return index
