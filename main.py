import os
from urllib.request import Request, urlopen
import time

directory = "osu_files/"
#466973
#815711
start = 0
end = 1100000+30000

def check_file():
    global directory
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

def make_request(i):
    global directory
    time.sleep(0.25)
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
check_file()

for i in range(start,end+1):
    try:
        make_request(i)
    except Exception as e:
        print(e)
        make_request(i)
