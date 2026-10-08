# 单条件控制
n=15
if n>15:
    print("可以进来参观")
#print("执行完毕")
# 双条件控制
if n>15:
    print("号码是15号以后可以进来参观")
else:
    print("号码是15号以后才可以进来参观")

print("等级查询")
cource=int(input("请输入你的分数:"))
if(cource>=90):
    print("你的成绩等级是：优秀")
elif cource<90 and cource>=80:
    print("你的成绩等级是：良好")
elif cource<80 and cource>=70:
    print("你的成绩等级是：中等")
else:
    print("你的成绩等级是：不合格")

