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
    
    searching = DeepFace.find(img_path='xxxxx', db_path='xxxxx')
 
    if searching["verified"] == True:
        return 1
    else:
        return -1

if __name__ == "__main__":

    print("Selecione a modalidade")
    flag = int(input())
    if flag == 1:
        print("Armazenando dados...")
        stored_data = storing()

    elif flag == 2:
        print("Analisando dados...")
        analysis_results = analysing()
        
    else:
        print("Buscando imagem...")
        search_result = finding()

