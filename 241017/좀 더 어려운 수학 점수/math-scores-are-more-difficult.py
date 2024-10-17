A_math, A_english = map(int, input().split())
B_math, B_english = map(int, input().split())

A = [A_math, A_english]
B = [B_math, B_english]

if A[0] > B[0] or (A_math == B_math and A_english > B_english):
    print('A')
else:
    print('B')