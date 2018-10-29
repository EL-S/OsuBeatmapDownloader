import os
import shutil

path = 'test/'
value = 0

for entry in os.scandir(path):
    file_path = entry.path
    if ".osu" in file_path:
        no_folder = entry.path.split("/")[1] #no slashes allowed in file name
        print(file_path)
        try:
            first = no_folder.split("(")[0] #potential way
        except:
            first = ""
        try:
            second = no_folder.split("-")[0]+"-"+no_folder.split("-")[1].split("(")[0] #different potential way
        except:
            second = ""
        try:
            third = no_folder.split("(")[:-1][0] #another potential way
        except:
            third = ""
        potential_folder_name = (first,second,third)
        if len(first) > len(second): #yuckky
            if len(first) > len(third):
                value = 0
            elif len(first) == len(third):
                value = 0
            else:
                value = 2
        elif len(first) == len(second):
            if len(first) > len(third):
                value = 0
            else:
                value = 2
        elif len(second) > len(third):
            value = 1
        else:
            value = 2
        folder_name = potential_folder_name[value]
        directory = (path+folder_name).strip()
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)
        try:
            new_location = directory+"/"+no_folder
            shutil.move(file_path, new_location)
        except:
            print("trailing zeros or something preventing correct folder naming")
    
