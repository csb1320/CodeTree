h, w = map(int, input().split())

# b = int((10000 * w) / (h ** 2))
b = (10000 * w) // (h ** 2)


print(b)
if(b >= 25):
    print("Obesity")