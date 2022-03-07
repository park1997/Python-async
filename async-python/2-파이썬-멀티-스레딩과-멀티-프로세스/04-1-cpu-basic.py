import time
import os
import threading

nums = [50,63,32]

# cpu 연산만 필요함 굳이 동시성프로그래밍이 사용될 이유가 없음
def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1,num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i*j*k
    return total


def main():
    results = [cpu_bound_func(num) for num in nums]
    print(results)

if __name__=="__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
