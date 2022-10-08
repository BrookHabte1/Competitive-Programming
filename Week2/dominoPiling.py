
M, N = map(int, input().split())
count = 0
for i in range(0, M):
    for j in range(0, N):
        count += 1
print(count / 2)
