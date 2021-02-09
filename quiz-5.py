from random import *


cnt = 0
for i in range(1,51):
    time = randrange(5, 51)
    if 5<= time <= 15:
        print("[o] [%d] 번째 손님 (소요시간 : %d)" %(i, time))
        cnt += 1
    else :
        print("[ ] [%d] 번째 손님 (소요시간 : %d)" %(i, time))


print("총 탑승 승객 : " + str(cnt) + " 분")

