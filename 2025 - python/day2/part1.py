input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0
for line in input.split(","):
    l, r = line.split("-")[0], line.split("-")[1]
    if len(str(l)) % 2 != 0:
        l = "1" + "0" * (len(str(l)))
    curr_num = int(l[:(len(l) + 1)//2])
    while int(str(curr_num) + str(curr_num)) <= int(r):
        # print(int(str(curr_num) + str(curr_num)))
        if (int(str(curr_num) + str(curr_num)) >= int(l)):
            ans += int(str(curr_num) + str(curr_num))
        curr_num += 1
output_file.write(str(ans)) 