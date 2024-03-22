from pymongo import MongoClient
import gridfs

def storing(i):
    """
    This function is responsible to try  connection to the database and manages if this connection doesn't sucessed
    If the connection happens, theres another kind of try, except method 



    """
    print(i)
    try:
        connection_string = "mongodb://localhost:27017"
        client = MongoClient(connection_string)
        db_connection = client["meuBanco"]
        fs = gridfs.GridFS(db_connection)

        print("Connected")
    except Exception as error:
        print(error)
        exit(1)

    #putting image
    try:
        filename = f'imgDB_help/img{i}.jpg'  # Correctly format the filename string
        with open(filename, 'rb') as file_data:
            fs.put(file_data, filename='img')
            print("File uploaded successfully.")
    except Exception as error:
        print("Error uploading file:", error)

# Example usage:
storing(1)  # Change the argument as needed
