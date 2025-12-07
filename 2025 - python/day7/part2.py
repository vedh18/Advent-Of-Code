import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

input = input.split("\n")
dp = np.zeros((len(input), len(input[0])), dtype=np.int64)

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "S":
            dp[i][j] = 1
            break
    else:
        continue
    break

for i in range(1, len(input)):
    for j in range(len(input[0])):
        if input[i][j] == ".":
            dp[i][j] += dp[i-1][j]
        elif input[i][j] == "^":
            if j-1>=0:
                dp[i][j-1] += dp[i-1][j] 
            if j+1<len(input[0]):
                dp[i][j+1] += dp[i-1][j]
    if i == len(input)-1:
        for j in range(len(input[0])):
            ans += dp[i][j]           
output_file.write(str(ans))