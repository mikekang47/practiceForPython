
for i in range(1, 51) :
    with open(str(i) + " 주차.txt", "w", encoding="utf8") as profile_file:
        profile_file.write("- {0}주차 주간보고 -".format(i))
        profile_file.write("\n부서 : ")
        profile_file.write("\n이름 : ")
        profile_file.write("\n업무 요약 : ")
