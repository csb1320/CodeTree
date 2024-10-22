a, b, c = map(int, input().split())
satisfied = False

for i in range(a, b + 1):
    if c % i == 0:
        satisfied = True

if satisfied == True:
    print("YES")
else:
    print("NO")