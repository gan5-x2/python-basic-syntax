import string
import sys

def check_identifier():
    # 1. 定义合法的字符集合
    # 首字符：大小写字母 + 下划线
    valid_first_chars = string.ascii_letters + "_"
    # 后续字符：大小写字母 + 下划线 + 数字
    valid_other_chars = valid_first_chars + string.digits

    # 2. 接收输入，并去除前后空格
    data = input("请输入合法的标识符: ").strip()

    # 3. 处理空输入的情况（最重要的漏洞修复）
    if not data:
        print("❌ 不合法：输入不能为空！")
        sys.exit()

    # 4. 检查首字符
    if data[0] not in valid_first_chars:
        print("❌ 不合法：首字符不能是数字，必须是字母或下划线！")
        sys.exit()

    # 5. 检查后续字符 (使用 for...else 更简洁)
    # 遍历从第二个字符到最后一个字符
    for char in data[1:]:
        if char not in valid_other_chars:
            print(f"❌ 不合法：包含了非法字符 '{char}'，只能包含字母、数字、下划线！")
            sys.exit()

    # 如果循环正常结束（没有 break 也没有 exit），说明全部通过
    print("✅ 你输入的用户名合法")

if __name__ == '__main__':
    check_identifier()