n = int(input())
satisfied = True

for i in range(2, 1001):
    if n % i != 0:
        satisfied = False


if satisfied == False: 
    print("P")
else:
    print("C")