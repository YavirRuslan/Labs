a = input().split(" ")
res = ""
for i in a:
    res += i[::-1] + " "
print(res)