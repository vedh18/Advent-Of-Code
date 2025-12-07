import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0
for line in input.split("\n"):
    n = len(line)
    m = 13
    dp = np.zeros((n, m))
    dp[0][1] = int(line[0])
    for i in range(1, n):
        dp[i][1] = max(dp[i-1][1], int(line[i]))
    for i in range(1, n):
        for j in range(2, m):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]*10 + int(line[i]))
    ans += dp[n-1][m-1]
    print(dp[n-1][m-1])
output_file.write(str(ans))