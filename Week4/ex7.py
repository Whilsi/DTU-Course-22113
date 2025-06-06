def SD(numbers:list) -> float:
    '''Calculates the standard deviation from a list of numbers'''

    import math

    if isinstance(numbers,list):
        n = len(numbers)
        numbers_sum = 0
        for number in numbers:
            if isinstance(number,(float,int,str)):
                try:
                    numbers_sum += float(number)
                except ValueError:
                    return 'The list must only contain numbers'
            else:
                raise TypeError('The list must only contain numbers')
        mean = numbers_sum/n

        summa = 0
        for number in numbers:
            if isinstance(number,(float,int,str)):
                summa += (float(number)-mean)**2
            else:
                raise TypeError('The list must only contain numbers')
            

        return math.sqrt(summa/n)
    else:
        return None

