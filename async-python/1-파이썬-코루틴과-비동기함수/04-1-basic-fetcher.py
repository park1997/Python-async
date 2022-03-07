import requests
import time

def fetcher(session,url):
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://www.naver.com","https://www.google.com","https://www.instagram.com"]*10
    
    # session = requests.Session()
    # session.get(url)
    # session.close()

    # 열고 닫기 한번에 
    with requests.Session() as session:
        result = [fetcher(session,url) for url in urls]
        print(result) # web에 대한 data


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start) # 코루틴을 사용하지 않은 결과 12초가 걸림