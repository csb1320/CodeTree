cnt = 0
sum_age = 0

while True:
    n = int(input())

    if n <= 29:
        sum_age += n
        cnt += 1
        continue
    else:
        break
        
    
print(f"{(sum_age / cnt):.2f}")