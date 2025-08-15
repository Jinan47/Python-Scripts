import shutil as sh
import os
import time

def copy_and_delete(path1, path2):
    path1 = input("where should I search").strip()
    path2 = input("where should I copy files to?").strip()
    path1 = ""

    for char in "FGHIJKLMNOPQRSTUVWXYZ":
        if os.path.exists(char+":"):
            break
    else:
        print("No external device is found")
        quit()
    path1 = char+":/Python"
    path2 = "D:/backup_photos"

    print("path 1 is: ", path1)

    list_of_files = os.listdir(path1)
    print(len(list_of_files))

    for file_name in list_of_files:
        print("checking file: ", file_name)
        if ".mp4" in file_name or "." in file_name:
            sh.copyfile(path1+"/"+file_name , path2+"/jinan_program_"+file_name)
            os.remove(path1+"/"+file_name)
            print("file: ", file_name, "is moved to backup_photos")

# def search_and_collect():
#     #path1 = input("where should I search").strip()
#     #path2 = input("where should I copy files to?").strip()
#     path1 = ""
#     list_of_file_paths = []

    
    for char in "FGHIJKLMNOPQRSTUVWXYZ":
        if os.path.exists(char+":"):
            break
    else:
        print("No external device is found")
        quit()
    path1 = char+""
    path2 = "D:/backup_photos"

    print("path 1 is: ", path1)
    print("path 2 is: ", path2)

