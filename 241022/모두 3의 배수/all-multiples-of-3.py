satisfied = True

for i in range(5):
    i = int(input())

    if i % 3 != 0:
        satisfied == False

if satisfied == False:
    print("0")
else:
    print("1")