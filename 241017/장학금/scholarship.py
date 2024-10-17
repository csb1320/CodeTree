mid_te, fin_te = map(int, input().split())

if mid_te >= 90:
    if fin_te >= 95:
        print(100000)
    elif fin_te >= 90:
        print(50000)
    else:
        print(0)
else:
    print