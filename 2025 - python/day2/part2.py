input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

def f(n):
    ans = 0
    num = "1"
    while int(num + num) <= int(n):
        flag = 0
        for i in range(1, len(num)):
            if len(num) % i != 0:
                continue
            if num == str(num[:i]) * (len(num) // i):
                flag = 1
                break
        if len(num) == 1:
            flag = 0
        if flag:
            num = str(int(num) + 1)
            continue
        reps = 2
        cand = int(str(num) * reps)
        while cand <= int(n):
            ans += cand
            reps += 1
            cand = int(str(num) * reps)
        num = str(int(num) + 1)
    return ans

input = input_file.read()
ans = 0
for line in input.split(","):
    l, r = line.split("-")[0], line.split("-")[1]
    ans += f(r) - f(str(int(l) - 1))
output_file.write(str(ans)) 