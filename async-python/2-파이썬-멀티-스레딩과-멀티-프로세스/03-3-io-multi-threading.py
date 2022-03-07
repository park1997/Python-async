from concurrent.futures import ThreadPoolExecutor
import time
import requests
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session,url = params
    # os.getpid() : 현재 프로세스 id를 return 함
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    # urls = ["https://www.apple.com","https://www.google.com","https://www.github.com"]*50
    urls = ["https://www.google.com","https://www.apple.com"]*50
    
    # max_workers : 최대 스레드를 실행할 개수
    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = [fetcher(session,url) for url in urls]
        # print(result)    

        params = [(session,url) for url in urls]
        # map 이라는 함수가 있는데 인자로 fetcher 와 parameter(리스트 형태)가 들어간다. 
        results = list(executor.map(fetcher,params))
        # print(results)

# 출력 결과를 보면 싱글스레드에서 실행되는 것을 알 수 있음. 
if __name__ =="__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start) 
    '''
    스레드 1개  => 13초 소요
    스레드 10개 => 1초 소요

    왠만하면 코루틴을 사용하는게 남 멀티스레드는 메모리 점유율이 많이 들기 때문
    '''
