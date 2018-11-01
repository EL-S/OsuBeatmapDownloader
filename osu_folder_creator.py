import os
import shutil
import re
import hashlib
from osu_parser import parse

path = 'osu_files_testing/'

for entry in os.scandir(path):
    file_path = entry.path
    file_name = file_path[len(path):]
    if ".osu" in file_path:
        try:
            information,sections,hit_objects = parse(file_path)
            try:
                folder_name = str(information['BeatmapSetID'])+" "+str(information['Artist'])+" - "+str(information['Title'])
                folder_name = re.sub('[\\\\/:*?"<>|]', '', folder_name).rstrip(".") #removes invalid folder characters and all trailing periods
                folder_name = re.sub(r"\t", "", folder_name) #remove tabs
                directory = (path+folder_name).strip()
                try:
                    os.stat(directory)
                except:
                    os.mkdir(directory)
                try:
                    new_location = (directory+"/"+file_name).strip()
                    shutil.move(file_path, new_location)
                except Exception as e:
                    print("Error Officially Parsing:",file_path,e)
            except: #it doesn't have a beatmapset id
                try:
                    unique_string = ""
                    try:
                        unique_string += information['Title']
                    except:
                        pass
                    try:
                        unique_string += information['TitleUnicode']
                    except:
                        pass
                    try:
                        unique_string += information['Artist']
                    except:
                        pass
                    try:
                        unique_string += information['ArtistUnicode']
                    except:
                        pass
                    try:
                        unique_string += information['AudioFilename']
                    except:
                        pass
                    unique_string = str(unique_string).encode("utf-8")
                    hasher = hashlib.sha1(unique_string)
                    unique_hash = hasher.hexdigest()[0:5]
                    artist = str(information['Artist']).lstrip(" ")
                    title = str(information['Title']).lstrip(" ")
                    folder_name = artist+" - "+title
                    folder_name = re.sub('[\\\\/:*?"<>|]', '', folder_name).rstrip(".")+" ("+str(unique_hash)+")" #removes invalid folder characters and all trailing periods
                    folder_name = re.sub(r"\t", "", folder_name) #remove tabs
                    directory = (path+folder_name).strip()
                    try:
                        os.stat(directory)
                    except:
                        try:
                            os.mkdir(directory)
                        except Exception as e:
                            print("Error Creating Directory:",file_path,e)
                    try:
                        new_location = (directory+"/"+file_name).strip()
                        shutil.move(file_path, new_location)
                    except Exception as e:
                        print("Error Unofficially Parsing:",file_path,e,unique_string)
                except Exception as e:
                    print("Error Unofficially Parsing:",file_path,e,unique_string)
        except Exception as e:
            print("Error Parsing:",file_path,e)
