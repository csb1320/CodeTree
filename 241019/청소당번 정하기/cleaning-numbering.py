n = int(input())

class_cnt = 0
pass_cnt = 0
toilet_cnt = 0

for i in range(1, n + 1):
    # 주기가 가장 긴 12일부터 확인합니다.
    if i % 12 == 0:
        toilet_cnt += 1
    # 12일 주기에 들어오지 않는다면, 3일 주기에 들어오는지 확인합니다.
    elif i % 3 == 0:
        pass_cnt += 1
    # 3일 주기에도 들어오지 않는다면, 2일 주기에 들어오는지 확인합니다.
    elif i % 2 == 0:
        class_cnt += 1

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         if i % 3 == 0:
#             if i % 12 == 0:
#                 toilet_cnt += 1
#             else:
#                 pass_cnt += 1
#         else:
#             class_cnt += 1
#     elif i % 3 == 0:
#         if i % 12 == 0:
#             toilet_cnt += 1
#         else:
#             pass_cnt += 1

print(class_cnt, pass_cnt, toilet_cnt)