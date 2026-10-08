import random

ran = random.randint(0, 100)

for i in range(1000):
    print(f"这是第{i + 1}次猜测")

    a = int(input("请输入你猜的数："))

    if a > ran:
        print("猜大了")
    elif a < ran:
        print("猜小了")
    else:
        print("你猜对了")
        break


