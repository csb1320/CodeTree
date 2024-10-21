a, b = map(int, input().split())

# print(a**b)
prod = 1
for _ in range(b):
    prod *= a

print(prod)