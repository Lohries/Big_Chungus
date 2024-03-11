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


def find(frame_f, cursor):
    SQL_statement = "SELECT Photo FROM Images"
    cursor.execute(SQL_statement)
    results = cursor.fetchall()

    for result in results:
        img_data = result[0]
        with open("temp.jpg", "wb") as file:
            file.write(img_data)
        frame = cv.imread("temp.jpg")
        if DeepFace.verify(frame_f, frame)["verified"]:
            return True
    return False


def upload_file(frame_UF, cursor, Data_Base):
    cv.imwrite(f"img/img{i}.jpg", frame_UF)
    with open(frame_UF, "rb") as file:
        binary_data = file.read()
    SQL_statement = "INSERT INTO Images (Photo) VALUES (%s)"
    cursor.execute(SQL_statement, (binary_data,))
    Data_Base.commit()






data_base = mysql.connector.connect(
    host="localhost",
    user="Lohries",
    password="",
    database="Brain_Project"
)

cursor = data_base.cursor()


cursor.execute("CREATE TABLE people ()")
print("DataBase created !!!")

i = 0
while True:
    control_flow = input("Select what to do (1)-Store (2)-Find (3)-Analyze): ")
    if int(control_flow) == 1:
        frame_CF = extraction(i)
        upload_file(frame_CF, cursor, data_base)
        i += 1

    elif int(control_flow) == 2:
        frame_CF = extraction(i)
        if find(frame_CF, cursor):
            print("Found matching image")
        else:
            print("No matching image found")

    elif int(control_flow) == 3:
        analyze()

    else:
        break
