mid_te, fin_te = map(int, input().split())

if mid_te >= 90 and fin_te >= 95:
	print("100000")
elif mid_te >= 90 and fin_te >= 90:
	print("50000")
else:
	print("0")