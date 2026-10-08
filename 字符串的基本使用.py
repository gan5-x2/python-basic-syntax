str_01="python"
str_02='Linux'
str_03=""""this is python cource"""

file_name1="d:\file\new.log"
file_name2=r"d:\file\new.log"
print(f"{file_name2}非正常输出: ")
print(f"{file_name2}正常输出: {file_name2}")

print(str_01+" "+str_02)
print((str_01+" ")*3)
print(f"{str_03}的长度是：{len(str_03)}")

print("py" not in str_02)
print("python" in str_03)

print(f"{str_01}的第一个字符是: {str_01[0]}")
print(str_03[0:9])

print(str_03[-6:])
print(str_03[5:10])

print(len("this is "))
new_data=str_03[0:8]+" p"+str_03[8:]
print(new_data)