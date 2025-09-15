# unittest 是 Python 内置的单元测试框架

# 运行

# 1.发现并运行（默认：start_dir=当前目录, pattern="test*.py"）
# unittest discover 会递归，但只会深入“包目录”（有 __init__.py 的目录）
# python -m unittest (== python -m unittest discover -s . -p "test*.py")

# 2.发现并运行（指定测试目录和文件模式）
# 在根目录运行此命令：
# python -m unittest discover -s tests -p "test_*.py"
# discover：启用“测试发现”。它会去找测试文件并导入运行
# -s tests（start dir）：从 tests/ 目录开始找测试
# 不要求 tests/ 包含 __init__.py
# 内部的子文件还是要求包含 __init__.py 才会被递归深入
# -p "test_*.py"：只匹配文件名形如 test_*.py 的测试文件

# 其他参数
# -v：verbose，显示更详细的测试结果
# -f：failfast，遇到第一个失败的测试用例就停止运行

def main():
    ...

if __name__ == "__main__":
    main()