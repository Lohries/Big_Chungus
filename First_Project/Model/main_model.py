from deepface import DeepFace
from Cam import extraction

def storing():
    store = extraction()
    return store

def analysing():
    capturing = extraction()
    results = DeepFace.analyze(capturing)
    return results

def finding():
    searching = DeepFace.find(img_path='xxxxx', db_path='xxxxx')