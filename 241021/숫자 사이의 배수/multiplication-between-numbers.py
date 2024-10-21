a, b = map(int, input().split())

sum_value = 0
count = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_value += i
        count += 1

avg_value = sum_value / count
print(sum_value, f"{avg_value:.1f}")