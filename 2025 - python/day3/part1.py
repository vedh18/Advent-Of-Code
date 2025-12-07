input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0
for line in input.split("\n"):
    mp = dict()
    for x in line[::-1]:
        mp[int(x)] = mp.get(int(x), 0) + 1
    num = 0
    for x in line:
        mp[int(x)] -= 1
        for i in range(10, 1, -1):
            if mp.get(i, 0) > 0:
                num = max(num, int(x) * 10 + i)
                break
    print(num)
    ans += num
output_file.write(str(ans)) 