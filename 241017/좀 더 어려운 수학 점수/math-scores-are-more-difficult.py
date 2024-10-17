A_math, A_english = map(int, input().split())
B_math, B_english = map(int, input().split())

A = [A_math, A_english]
B = [B_math, B_english]

if A[0] > B[0]:
    print('A')
elif B[0] > A[0]:
    print('B')
else:
    if A[1] > B[1]:
        print('A')
    elif B[1] > A[1]:
        print('B')