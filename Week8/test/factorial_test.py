import pytest,sys
sys.path.append('/home/wsl_ubuntu/DTU/22113/Week8/src')
from factorial import factorial

def test_1():
    assert factorial(12) == 479001600,'12'

def test_2():
    assert factorial(2) == 2, '2'

def test_3():
    assert factorial(1) == 1, '1'

def test_4():
    assert factorial(0) == 1, '0'

def test_5():
    with pytest.raises(ValueError):
        factorial(-1)

def test_6():
    assert factorial(3.0) == 6, 'Integer float'
    
def test_7():
    with pytest.raises(TypeError):
        factorial(3.4)

def test_8():
    assert factorial('3') == 6, 'Integer string'

def test_9():
    with pytest.raises(TypeError):
        factorial('3.1')

def test_10():
    with pytest.raises(TypeError):
        factorial('ABC')