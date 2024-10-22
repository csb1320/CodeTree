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
        
    
if cnt > 0:
    print(f"{(sum_age / cnt):.2f}")
else:
    print("No valid input received")