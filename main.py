







n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
prev = [[''] * m for _ in range(n)]

dp[0][0] = a[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + a[i][0]
    prev[i][0] = 'U' 

for j in range(1, m):
    dp[0][j] = dp[0][j-1] + a[0][j]
    prev[0][j] = 'L'

for i in range(1, n):
    for j in range(1, m):
        if dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + a[i][j]
            prev[i][j] = 'U'
        else:
            dp[i][j] = dp[i][j-1] + a[i][j]
            prev[i][j] = 'L'

print(dp[n-1][m-1])

path = []
i, j = n-1, m-1
while i > 0 or j > 0:
    if prev[i][j] == 'U':
        path.append('D')  
        i -= 1
    else: 
        path.append('R')  
        j -= 1


print(''.join(reversed(path)))







