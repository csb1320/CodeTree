n = int(input())

class_cnt = 0
pass_cnt = 0
toilet_cnt = 0

for i in range(1, n):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 12 == 0:
                toilet_cnt += 1
            else:
                pass_cnt += 1
        else:
            class_cnt += 1
    elif i % 3 == 0:
        if i % 12 == 0:
            toilet_cnt += 1
        else:
            pass_cnt += 1

print(class_cnt, pass_cnt, toilet_cnt)