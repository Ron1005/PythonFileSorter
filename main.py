import os,shutil

path = r"C:\Users\mhady\PycharmProjects\FileSorter\TestFolder"

file_names = os.listdir(path)

folder_names = ['excel_files','txt_files','image_files']

#print(os.getcwd())
os.chdir(path)
#print(os.getcwd())
for folder_name in folder_names:
    if os.path.exists(folder_name):
        pass
    else:
        os.mkdir(folder_name)

for file in file_names:
    if ".xlsx" in file and file not in os.listdir(path+"\excel_files"):
        shutil.move(file,path+"\excel_files")
    elif ".txt" in file and file not in os.listdir(path+"\\"+"txt_files"):
        shutil.move(file,path+"\\txt_files")
    elif ".jpg" in file and file not in os.listdir(path+"\image_files"):
        shutil.move(file,path+"\image_files")

