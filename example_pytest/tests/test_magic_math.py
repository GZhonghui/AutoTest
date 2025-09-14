# 测试代码都放在 /tests 目录下（默认）
# 测试文件名以 test_ 开头，测试函数也以 test_ 开头
# 在模块的根目录下，运行：python -m pytest
# 进一步显示详细信息：python -m pytest -vv

from src.magic_math import magic_add
import pytest

# 在 pytest.ini 中定义标记
# 为函数添加自定义标记
# 测试某一个标记的函数：python -m pytest -m add
@pytest.mark.add
def test_magic_add():
    assert magic_add(2, 3) == 6
    assert magic_add(-1, 1) == 1
    assert magic_add(0, 0) == 1

# test函数可以自己随便写
def test_magic_add_type_error():
    # 预期抛出 TypeError
    with pytest.raises(TypeError):
        magic_add(2.5, 3)
    with pytest.raises(TypeError):
        magic_add("2", 3)
    with pytest.raises(TypeError):
        magic_add(2, None)