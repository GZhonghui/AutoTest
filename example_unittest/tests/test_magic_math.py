from src.magic_math import magic_add
from unittest.mock import patch
import unittest

# 这个类的名称好像可以随便取
class TestMagicMath(unittest.TestCase):
    # setUp 和 tearDown 方法可以用来在每个测试方法执行前后做一些准备工作和清理工作
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    # 以 test_ 开头的方法会被 unittest 识别为测试用例
    # 反之就是普通方法
    def test_magic_add(self):
        self.assertEqual(magic_add(1, 2), 5)
        self.assertEqual(magic_add(-1, 1), 2)
        self.assertEqual(magic_add(0, 0), 2)

# unittest 包含 Mock 功能，可以用来模拟对象和函数
class TestMagicMathMock(unittest.TestCase):
    # patch 表示用 mock 替换指定的对象或函数
    # 这里的 "src.magic_math.get_magic_number" 是原本的函数路径
    @patch("src.magic_math.get_magic_number")
    # 这个 mock_get_magic_number 就是被 patch 替换后的 mock 对象
    # 简单理解：
    # 创建一个 mock_get_magic_number 对象，用它替换 src.magic_math.get_magic_number 函数
    def test_magic_add_mock(self, mock_get_magic_number):
        # 对于我们创建的 mock 对象，我们可以随意控制它的行为
        mock_get_magic_number.return_value = 10
        self.assertEqual(magic_add(1, 2), 13)
        self.assertEqual(magic_add(-1, 1), 10)
        self.assertEqual(magic_add(0, 0), 10)

    # 只是为了演示 side_effect 的用法
    @patch("src.magic_math.get_magic_number")
    def test_magic_add_mock_side_effect(self, mock_get_magic_number):
        # 当只有 return_value 时，mock 对象每次调用都返回同样的值
        mock_get_magic_number.return_value = 3
        self.assertEqual(magic_add(1, 2), 6)

        mock_get_magic_number.side_effect = [4, 5, 6]
        # 当设置了 side_effect 为一个列表时，mock 对象每次调用会依次返回列表中的值
        # 原本的 return_value 会被忽略
        self.assertEqual(magic_add(1, 2), 7)  # 1 + 2 + 4
        self.assertEqual(magic_add(1, 2), 8)  # 1 + 2 + 5
        self.assertEqual(magic_add(1, 2), 9)  # 1 + 2 + 6

        with self.assertRaises(StopIteration):
            # 列表中的值用完后，再调用会抛出 StopIteration 异常
            magic_add(1, 2)

        mock_get_magic_number.side_effect = lambda: 20
        # 当设置了 side_effect 为一个函数时，mock 对象每次调用会调用该函数并返回其结果
        self.assertEqual(magic_add(1, 2), 23)  # 1 + 2 + 20

        mock_get_magic_number.side_effect = Exception("Mocked exception")
        # 当设置了 side_effect 为一个异常时，mock 对象每次调用会抛出该异常
        with self.assertRaises(Exception) as context:
            magic_add(1, 2)
        self.assertEqual(str(context.exception), "Mocked exception")

        # 还可以把 side_effect 设置为一个列表，列表中的元素可以是值、异常或函数
        mock_get_magic_number.side_effect = [1, Exception("Second call exception"), lambda: 5]