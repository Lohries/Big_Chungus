from deepface import DeepFace
from Cam import taking_photo


def register():
    result_register = taking_photo()
    return result_register

def analyse():
    pass

def compare():
    result_compare = DeepFace.find(img_path='xxxxx', db_path='xxxxxx')
    return result_compare


