# 간단한 Brute Force
# 카드 뭉치 최대 조합
def max_product(left_cards, right_cards):
    max_product = -1
    for i in left_cards:
        for j in right_cards:
            max_product = max(max_product, i * j)
    return max_product
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

''' 시간 복잡도
len(left_cards) = m , len(right_cards) = n이라고 할 때,
O(mn)'''