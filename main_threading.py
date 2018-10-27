import os
from urllib.request import Request, urlopen
from tornado import ioloop, httpclient

directory = "osu_files/"
start = 1
end = 1000
i = 0
threads = 5
total = 0

def check_file():
    global directory
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)

def download_osu_files():
    global cookies,start,end,i,threads,total

    http_client = httpclient.AsyncHTTPClient(force_instance=True,defaults=dict(user_agent="Mozilla/5.0"),max_clients=threads)
    for id_num in range(start,end+1):
        url = "https://osu.ppy.sh/osu/"+str(id_num)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        request = httpclient.HTTPRequest(url.strip(),headers=headers,method='GET',connect_timeout=10000,request_timeout=10000)
        http_client.fetch(request,handle_page_response)
        i += 1
    total = i
    ioloop.IOLoop.instance().start()

def handle_page_response(response):
    if response.code == 599:
        print(response.effective_url,"error")
        http_client.fetch(response.effective_url.strip(), handle_page_response, method='GET',connect_timeout=10000,request_timeout=10000)
    else:
        global i,total
        try:
            file_name = str(response.effective_url.split("/")[-1:])
            full_path = directory + file_name
            data = response.body.decode('utf-8')
            with open(full_path, "w") as file:
                file.write(data)
            print("alive",response.effective_url)
        except Exception as e:
            print("dead",response.effective_url,e)
        i -= 1
        if i == 0: #all pages loaded
            ioloop.IOLoop.instance().stop()
            print("complete")

check_file()
download_osu_files()
