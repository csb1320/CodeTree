a, b = map(int, input().split())

if a < b:
    a = a
    b = b + 1
else:
    temp = a + 1
    a = b
    b = temp

sum_value = 0

for i in range(a, b):
    if i % 5 == 0:
        sum_value += i

print(sum_value)