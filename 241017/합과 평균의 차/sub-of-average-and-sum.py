a, b, c = map(int, input().split())

arr = [a, b, c]

if(sum(arr) % 3 == 0):
    print(sum(arr))
    print(sum(arr)//len(arr))
    print(sum(arr) - sum(arr)//len(arr))

else:
    print(sum(arr))
    print(sum(arr)/len(arr))
    print(sum(arr) - sum(arr)/len(arr))