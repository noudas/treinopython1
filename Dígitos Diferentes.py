n,m = input().split()
count = 0

for i in range(int(n), int(m)+1):
    if len(set(list(str(i)))) == len(str(i)):
        count += 1
print(count)
