import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

nums = [50,63,32]

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1,num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i*j*k
    return total

# 멀티프로세싱 병렬로 실행
def main():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func,nums))
    print(results)


if __name__=="__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start) # 멀티스레딩을하든 안하든은 결과가 같지만 멀티프로세싱을 하면 실행시간이 빠름
    # 어차피 해야하는일을 나눠서하든 순서대로 하든 실행 시간은 같음
    # 하지만 각각의 해야할 일을 멀티프로세싱으로 한다면 분업과 마찬가지 이기떄문에 실행시간이 줄어듬
    