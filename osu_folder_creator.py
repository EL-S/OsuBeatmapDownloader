import os

path = 'test/'

for entry in os.scandir(path):
    no_folder = entry.path.split("/")[1] #no slashes allowed in file name
    first = no_folder.split("(")[0] #potential way
    second = no_folder.split("-")[0]+"-"+no_folder.split("-")[1].split("(")[0] #different potential way
    third = no_folder.split("(")[:-1][0] #another potential way
    if len(first) > len(second):
        if len(first) > len(third):
            print(first)
        elif len(first) == len(third):
            print(first)
        else:
            print(third)
    elif len(first) == len(second):
        print(first)
    elif len(second) > len(third):
        print(second)
    else:
        print(third)    
