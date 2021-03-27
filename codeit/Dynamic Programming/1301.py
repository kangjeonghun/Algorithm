# Dynamic Programming
# 새꼼달꼼 장사 Tabulation

def max_profit(price_list, count):
    # base case를 포함한 table 생성
    table = [0, 100]
    if count < 2:
        return table[count]
    # table에 인덱스 2부터 count까지 채워나가는 과정
    for i in range(2, count + 1):
        # max_profit 설정
        '''일단 리스트에 인덱스 i에대해 한번에 파는 가격이 존재하면, 한번에 파는 가격을 max값으로 저장
        인덱스 i에 대해 한번에 파는 가격이 존재하지 않으면, 0으로 저장함
        예를 들어 count = 10이고 , price_list = [0, 200, 600, 900, 1200, 2000]면
        i가 5가될때까지는 max값을 인덱스 i에 대한 값으로 설정해야만 함. 한번에 파는게 최대일 수 있기 때문임.
        그러나 i가 6이 되면서부터 i를 한번에 팔 수 있는 방법은 없음. 가격이 없기때문임'''
        if i <= len(price_list) - 1: 
            max_profit = price_list[i]
        else:
            max_profit = 0 
        # table 채우는 과정
        for j in range(1, i // 2 + 1):
            tmp = table[j] + table[i - j]
            max_profit = max(max_profit, tmp)
        table.append(max_profit)
    return table[count]    
# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
