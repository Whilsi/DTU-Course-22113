def combinations(list_of_strings:list[str]):
    n = len(list_of_strings)
    counter = [0 for i in range(n)]
    while counter[0] < len(list_of_strings[0]):
        string = ''
        for j in range(n):
            string += list_of_strings[j][counter[j]]
        yield string

        counter[-1] += 1
        for j in range(n-1,0,-1):
            if counter[j] >= len(list_of_strings[j]):
                counter[j] = 0
                counter[j-1] += 1

strings = ['0123456789','0123456789','0123456789']
for string in combinations(strings):
    print(string)