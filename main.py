import os
from urllib.request import Request, urlopen

directory = "osu_files/"
start = 0
end = 869742+1000

def check_file():
    global directory
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

check_file()

for i in range(start,end+1):
    try:
        url = "https://osu.ppy.sh/osu/" + str(i)

        request = Request(url)

        page = urlopen(request)
        try:
            file_name = page.headers['Content-Disposition'].split('"')[1]
            full_path = directory + file_name
            data = page.read().decode()
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(data)
            print("alive",url)
        except Exception as e:
            print("dead",url,e)
    except Exception as e:
        print(e)
