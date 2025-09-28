import pytest

def factorial(number:int) -> int:
    '''This funciton takes an integer as its input and returns the factorial'''
    try:
        if float(number) == int(number):
            number = int(number)
    except:
        pass

    if isinstance(number,int):
        if number >= 0:
            if number == 0:
                return 1
            result = 1
            for i in range(1,number+1):
                result *= i
            return result
        else:
            raise ValueError('The integer must be positive')
    else:
        raise TypeError('The input must be an integer')
    
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