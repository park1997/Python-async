# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3

# import requests # 동기와 관련된 패키지
import time
import aiohttp
import asyncio

async def fetcher(session,url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.naver.com","https://www.google.com","https://www.instagram.com"]*10
    
    # session = requests.Session()
    # session.get(url)
    # session.close()

    # 열고 닫기 한번에 
    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session,url) for url in urls]
        # print(result) # web에 대한 data
        
        result = await asyncio.gather(*[fetcher(session,url) for url in urls])
        # result = await fetcher(session,urls[0]) # 하나의 결과 확인하기 
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main()) # 비동기 함수 실행할떄 이렇게 해야함
    end = time.time()
    print(end-start) # 코루틴을 사용한 결과 2초가 걸림