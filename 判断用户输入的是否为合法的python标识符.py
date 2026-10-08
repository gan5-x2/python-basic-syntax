import string
import sys

# 定义首字符：大小写字母、下划线
first_letter = string.ascii_letters + "_"
#定义其余字符为大小写字母、下划线、数字的组合
other_letters=first_letter+string.digits
#定义一个标记，0为不合法，1为合法
flag=1
#接收输入的字符,strip表示把空格去掉
data=input("请输入合法的标识符").strip()
first_char=data[0]
if first_char not in first_letter:
    flag = 0
    print("不合法，首字符不能是数字")
    # sys.exit()退出系统
    sys.exit()

for i in range(1,len(data)):
    if data[i] not in other_letters:
        flag = 0
        print("不合法，首字符不能是数字")
        break
else:
    flag = 1

if flag == 1:
    print("你输入的用户名合法")
else:
    print("你输入的用户名不合法")
