import os
import shutil
import time

def main():
    deleted_folder_count = 0
    deleted_file_count = 0
    path = "C:\Users\Hemant\Desktop\Computer\Backupfiles"
    days = 30
    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count = deleted_folder_count+1
                break
            else :
                for folder in folders:
                    folder_path = os.path.join(root_folder,folders)
                    if seconds>= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_count = deleted_folder_count+1
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds>= get_file_or_folder_age(file_path):
                        remove_folder(file_path)
                        deleted_file_count = deleted_file_count+1       
    else:
        if seconds>=get_file_or_folder_age(path):
            remove_file(path)
            deleted_file_count+=1
                                
                

 