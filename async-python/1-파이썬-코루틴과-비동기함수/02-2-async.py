import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():

    result = await asyncio.gather(
        delivery("A", 5),
        delivery("B", 3),
        delivery("C", 4),
    )

    print(result)

    # 아래처럼 예약하고 할 수 있음
    task1 = asyncio.create_task(delivery("A",5))
    task2 = asyncio.create_task(delivery("B",3))
    task3 = asyncio.create_task(delivery("C",4))

    await task1
    await task2
    await task3



if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)