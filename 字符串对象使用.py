#判断字符串的开头与结尾
#startswith以什么开始
print("python".startswith("py"))
#endswith以什么结尾
print("python".endswith("a"))

#filename=input("请输入上传的文件名，包括扩展名")
#if filename.endswith(".doc") or filename.endswith(".ppt"):
#    print("符合上传文件类型，上传成功")
#else:
#    print("只能上传word文件，上传不成功")

#去除指定的字符
#去除左右两边指定的字符
print("ApythAonAA".strip("A"))
#去除左边指定的字符
print("ApythAonAA".lstrip("A"))
#去除右边指定的字符
print("ApythAonAA".rstrip("A"))
#去除空格
print("    Apyth  AonAA    ".strip(" "))

#分割字符串
data="python-linux-java-shell"
#split()分割字符串，括号里面写的什么符号就以什么符合分割，默认是空格，结果是一个列表
new_data=data.split("-")
j=0
for i in new_data:
    j+=1
    print(f"分割之后的第{j}个数据是：{i}")

#替换字符
#replace("old","new"),表示用后面的字符替代前面的字符
print("ApythAonAA".replace("A", ""))
#去除所有的A之后
old_str = "ApythAonAA"
new_str = old_str.replace("A", "")
print(f"ApythAonAA去除所有的A之后是：{new_str}")

#统计相同字的个数
duanluo = """你总说前路难行，可你不曾停下脚步。
你见过暮色沉落，你听过晚风低语，你在迷茫里寻找方向，你在疲惫中守住初心。
不必畏惧眼前坎坷，你拥有独属于自己的力量。你要相信，你付出的每一分努力，时光都会铭记。
愿你保持热爱，奔赴山海，你走过的路，终会化作照亮你的光。"""
print(duanluo.count("你"))

english="""Life is full of small warm moments. The soft morning sunlight, gentle wind and quiet smiles can cheer us up. Don’t rush for results. Slow down and feel the world around you. Keep hope in your heart, bravely face troubles, and keep moving forward step by step. Every effort you make will bring you closer to your dreams."""
#duanluo是段落
#len是计算长度的方法，它会包括逗号句号这些
print(f"这个段落中一共有{len(english.splitlines())}行")
print(f"这个段落中一共有{len(english.splitlines())}行")
print(f"段落包含标点符号的字符个数：{len(duanluo)}")
#\u4e00 到 \u9fff 是 Unicode 里汉字的编码区间。表示从一到最后一个汉字
j=0
for i in duanluo:
    if '\u4e00' <= i <= '\u9fff':
        j=j+1
print(f"段落中包含中文字符：{j}")



