# 간단한 Brute Force
# 가까운 매장 찾기

# 제곱근 사용을 위한 sqrt 함수 import
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    length = len(coordinates)
    store1 = coordinates[0]
    store2 = coordinates[1]
    min_distance = distance(store1, store2) # 일단 초기값으로 가까운 매장을 0번, 1번인덱스로 설정 
    
    for i in range(length):
        for j in range(length):
            if i < j:
                if min_distance > distance(coordinates[i], coordinates[j]):
                    min_distance = distance(coordinates[i], coordinates[j])
                    store1 = coordinates[i]
                    store2 = coordinates[j]
                    
    return [store1, store2]    
# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

'''시간복잡도
중첩반복문의 반복 횟수가 둘다 n에 비례하기에 O(n^2)'''