def Hamming_distance(string1:str,string2:str) -> int:
    '''Returns the Hamming distance between two strings of equal length.'''

    if isinstance(string1,str) and isinstance(string2,str) and len(string1) == len(string2):
        distance = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                distance += 1
        return distance
    else:
        return None