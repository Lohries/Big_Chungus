from deepface import DeepFace
from Cam import extraction

def storing():
    store = extraction()
    return store

def analysing():
    capturing = extraction()
    results = DeepFace.stream(capturing)
    return results

def finding():
    flag = 1
    searching = DeepFace.find(img_path='xxxxx', db_path='xxxxx')
    if searching["verified"] == 'True':
        return flag
    else:
        flag = -1
        return flag
    
    