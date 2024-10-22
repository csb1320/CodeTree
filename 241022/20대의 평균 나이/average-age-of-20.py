cnt = 0
sum_age = 0

while True:
    n = int(input())

    if n > 29 or n < 20:
        break
    
    sum_age += n
    cnt += 1
        
print(f"{(sum_age / cnt):.2f}")