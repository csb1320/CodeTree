a, b, c = map(int, input().split())
arr = [a, b, c]

if a != max(arr) and a != min(arr):
    print(a)
elif b != max(arr) and b != min(arr):
    print(b)
else:
    print(c)