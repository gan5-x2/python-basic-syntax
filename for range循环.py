# range(5)它返回一个 range 对象，表示从 0 开始到 5 结束（不包含 5）的整数序列。
# print(range(5))
j=0
for i in range(5,10):
    j+=1 #表示把j上一次循环的值加1之后再赋值给变量j
    print(f"这是第{i+1}个数{i}")
