N = int(input())


for i in range(11):
    if N // (2 ** i) == 1:
        break
    
print(i)