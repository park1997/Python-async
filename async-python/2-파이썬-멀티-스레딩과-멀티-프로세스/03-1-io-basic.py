import time
import requests
import os
import threading


def fetcher(session,url):
    # os.getpid() : 현재 프로세스 id를 return 함
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    # urls = ["https://www.apple.com","https://www.google.com","https://www.github.com"]*50
    urls = ["https://www.google.com","https://www.apple.com"]*50

    with requests.Session() as session:
        result = [fetcher(session,url) for url in urls]
        # print(result)    

# 출력 결과를 보면 싱글스레드에서 실행되는 것을 알 수 있음. 
if __name__ =="__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
