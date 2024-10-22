N = int(input())
prod = 1
x = 0

while True:
	# prod가 n이 될 때까지 2를 곱합니다.
	if N == prod:
		break

	prod *= 2
	x += 1
# for i in range(11):
#     if N // (2 ** i) == 1:
#         break
    
print(x)