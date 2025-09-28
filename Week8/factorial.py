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