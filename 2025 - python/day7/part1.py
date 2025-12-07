import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

input = input.split("\n")
vis = np.zeros((len(input), len(input[0])))
def dfs(i, j):
    # print(i, j)
    global ans, input, vis
    if j < 0 or j >= len(input[0]) or i < 0 or i >= len(input) or vis[i][j]:
        return
    vis[i][j] = 1
    while i < len(input):
        if input[i][j] == "^":
            # print(i, j)
            # ans += 1
            if not vis[i][j]:
                ans += 1
            vis[i][j] = 1
            dfs(i, j-1)
            dfs(i, j+1)
            break
        i += 1

for i in range(len(input)):
    for j in range(len(input[0])):
        # print(i, j)
        if input[i][j] == "S":
            dfs(i, j)
            break
    else:
        continue
    break
output_file.write(str(ans))