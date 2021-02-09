address = "http://naver.com"

my_url = address.replace("http://", "")
my_url = my_url[:my_url.index(".")]
password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print("{0}의 password는 {1}입니다".format(address, password))

