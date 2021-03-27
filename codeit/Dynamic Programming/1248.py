# Dynamic Programming
# Tabulation 이용

def fib_tab(n):
    # base case
    if n < 2:
        return 1
    # Tabulation    
    table = [0, 1, 1]
    i = 3
    while i <= n:
        table.append(table[i - 2] + table[i - 1])
        i += 1
    return table[n]
        
# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))