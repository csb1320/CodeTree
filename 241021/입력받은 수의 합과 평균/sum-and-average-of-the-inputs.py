n = int(input())
sum_value = 0
cnt = 0

for i in range(n):
    i = int(input())
    sum_value += i
    cnt += 1

avg = sum_value / cnt

print(sum_value, f"{avg:.1f}" )