a, b, c = map(int, input().split())
arr = [a, b, c]

print(1, end = " ") if a == min(arr) else print(0, end = " ")
if a == b and b == c:
    print(1)
else:
    print(0)