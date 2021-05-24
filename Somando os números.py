a = input()
a = [char for char in a]
print(a)
c = 0
for i in range(len(a)):
    c += int(a[i])

print(c)
