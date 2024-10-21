sum_value = 0
cnt = 0

for _ in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        sum_value += a
        cnt += 1

print(f"{sum_value} {(sum_value / cnt):.1f}")