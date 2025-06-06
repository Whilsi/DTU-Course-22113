def fibonacci(no1,no2,count:int):
    '''Returns the fibonacci sequence from two start numbers and the length count'''
    
    if isinstance(no1,(int,float)) and isinstance(no2,(int,float)) and isinstance(count,int):
        fibonacci_list = [no1,no2]

        for i in range(count):
            fibonacci_list.append(fibonacci_list[-2]+fibonacci_list[-1])

        return fibonacci_list
    else:
        return None