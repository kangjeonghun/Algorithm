# Dynamic Programming
# Memoization 이용하여 피보나치 수열 함수 구현

def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1
    # recursive case
    # 만약 key n의 value가 저장되어있으면 return해줌
    if n in cache:
        return cache[n]
    # n의 value가 없으면, 재귀적으로 불러와서 n에 value를 저장해줌
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
    
def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))