import os
from os.path import exists
import enum

class FVM(enum.Enum): # short for FaceVerificationModel
    vgg = "VGG-Face"
    facenet = "Facenet"
    facenet512 = "Facenet512"
    openface = "OpenFace"
    deepface = "DeepFace"
    deep_id = "DeepID"
    
class GBU(enum.Enum):
    good = "Good"
    bad = "Bad"
    ugly = "Ugly"

folder_path = "./GBU-Dataset"
query_path_suffix = "_Query_Normailized_128x128_gbuReduced/"
target_path_suffix = "_Target_Normailized_128x128_gbuReduced/"

def get_query_target_paths(gbu_type:GBU):
    gbu = str(gbu_type.value)
    query_path = f"{folder_path}/{gbu}{query_path_suffix}" 
    target_path = f"{folder_path}/{gbu}{target_path_suffix}" 
    return query_path, target_path

def get_images_from_path(path:str):
    try: return os.listdir(path)
    except: raise Exception("Path invalid!")