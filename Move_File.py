import os
import shutil

from_dir="C:/Users/Lenovo/Downloads"
to_dir="D:/Document_Files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_Name in list_of_files:
    path,ext=os.path.splitext(file_Name)
    #print(path)
    if ext in ['.png','.jpg']:
        path1=from_dir+'/'+file_Name
        path2=to_dir+'/'+file_Name
        shutil.move(path1,path2)
        
