from deepface import DeepFace
import cv2 as cv
import mysql.connector

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
    
    i = i + 1
    return frame


def analyze():
    pass


def find(frame_f):
    results = DeepFace.find(frame_f)
    return results


def Upload_File(frame_UF, cursor, Data_Base):
    cv.imwrite(f"img/img{i}.jpg", frame_UF)
    with open(frame_UF, "rb") as file:
        Binary_data = file.read()
    SQL_insert = "INSERT INTO Images (Photo) VALUES (%s)"
    cursor.execute(SQL_insert, (Binary_data,))
    Data_Base.commit()




Data_Base = mysql.connector.connect(
    host="localhost",
    user="Lohries",
    password="xxx",
    database="Brain-Project"
)

cursor = Data_Base.cursor()

query = """
    CREATE TABLE IF NOT EXISTS Images (
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Photo MEDIUMBLOB NOT NULL
    )
"""
cursor.execute(query)
print("DataBase created !!!")

i = 0
while True:
    control_flow = input("Select what to do (1)-Store (2)-Find (3)-Analyze): ")
    if int(control_flow) == 1:
        frame_CF = extraction(i)
        Upload_File(frame_CF, cursor, Data_Base)
        i += 1
    elif int(control_flow) == 2:
        frame_CF = extraction(i)
        cv.imwrite(f"img/img{i}.jpg", frame_CF)
        find(frame_CF)
    elif int(control_flow) == 3:
        analyze()
    else:
        break
