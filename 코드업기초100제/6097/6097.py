#6097 [기초-리스트]설탕과자 뽑기
h, w = input().split()
n = input()

p = [[0 for i in range(int(w))] for j in range(int(h))]

for i in range(int(n)):
    l, d, x, y = input().split()
    for j in range(int(l)):
        if int(d) == 1:
            p[int(x)-1+j][int(y)-1] = 1
        else:
            p[int(x)-1][int(y)-1+j] = 1
print(p)