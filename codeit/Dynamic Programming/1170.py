# Dynamic Programming
# 새꼼달꼼 장사 Memoization

def max_profit_memo(price_list, count, cache):
    # base case
    # 사려고 하는 개수가 2개 미만이면 개수에 해당하는 가격을 return
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]
    # recursive case
    # 사려고 하는 개수에 해당하는 value가 존재한다면 리턴해줌
    if count in cache:
        return cache[count]
    # count에 대한 캐시가 존재하지 않다면, 즉 cache[count]가 없다면    
    else:
        # max_ 결정하기
        # 사려고 하는 개수(count)를 한번에 파는 가격이 리스트에 없다면
        # 일단 max_에 리스트의 맨 마지막가격을 저장함.
        # count를 한번에 파는 가격이 리스트에 있으면(price_list[count])
        # 그 값을 max_에 저장
        if count > len(price_list) - 1:
            max_ = price_list[len(price_list) - 1]
        else:
            max_ = price_list[count]
        # 팔수있는 모든 경우의 가격을 반복문을 통해 구하고  가장 큰값을 구하는 과정     
        for i in range(1, count // 2 + 1):
            tmp = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache)
            max_ = max(max_, tmp)
        # 가장 큰 가격을 찾았으면 이제 그 값을 count의 value로 저장해줌            
        cache[count] = max_
        return max_
    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))