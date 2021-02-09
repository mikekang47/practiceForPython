def std_weight(height, gender):
    if gender == "남자":
        print("키 {0}cm 남자의 표준 체중은 {1} 입니다."
        .format(height, round(height * height * pow(0.01, 2) * 22,2)))
    elif gender == "여자":
        print("키 {0}cm 남자의 표준 체중은 {1} 입니다."
        .format(height, round(height * height * pow(0.01, 2) * 21,2)))
    
std_weight(175, "남자")

