import os
def rename_files():
    file_list = os.listdir("/Users/autumnlaniel/Documents/Programming/PythonPractice/filerename/idk files")
    saved_path = os.getcwd()
    #print(file_list)
    os.chdir("/Users/autumnlaniel/Documents/Programming/PythonPractice/filerename/idk files")

    for file_name in file_list:
        os.rename(file_name, file_name.translate("0123456789") )
    os.chdir(saved_path)
rename_files()