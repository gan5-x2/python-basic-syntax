import random
import string

# ascii_letters包含所有大小写字母
# string.digits包含所有的数字
# string.punctuation包含所有的特殊字符
all_str=string.ascii_letters+string.digits+string.punctuation
data=""

# random.choice(all_str)表示从all_str随机取出一个字符
for i in range(10):
    data=random.choice(all_str)+data
print(f"生成的10个随机字符是:{data}")
