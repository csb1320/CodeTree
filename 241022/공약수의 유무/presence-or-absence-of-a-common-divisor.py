a, b = map(int, input().split())
satisfied = False

for i in range(1, 1001):
    if 1920 % i == 0 and 2880 % i == 0:
        satisfied = True

if satisfied == True:
    print("1")
else:
    print("0")