def factorial(number:int) -> int:
    '''This funciton takes an integer as its input and returns the factorial'''
    if isinstance(number,int) and number > 0:
        result = 1
        for i in range(1,number+1):
            result *= i
        return result
    else:
        return None