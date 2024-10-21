a, b = map(int, input().split())
sum_value = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum_value += i

print(sum_value)