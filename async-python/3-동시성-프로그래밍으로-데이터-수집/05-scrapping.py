import aiohttp
import asyncio
from config import get_secret

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""


async def fetch(session, url, i):
    print(i + 1)
    # http프로토콜에 해당하는 header를 넣어주어야 함
    # 헤더를 지정해주지 않으면 권한 오류가 생김
    # secret key들은 외부에 유출이 되면 안댐
    headers = {
        "X-Naver-Client-Id" : get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret" : get_secret("NAVER_API_SECRET")
    }
    async with session.get(url,headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        # print(result)
        
        # cat 이미지들이 담기게 됨
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    # 여기서 page는 각 사진의 index 이므로 페이지당 20개의 사진이있어서 20개씩 건너뛰어서 json을 받아줘야함
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={i}" for i in range(1, 200, 20)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())