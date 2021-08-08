# Are they the "same"?

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    temp_array = [x ** 2 for x in array1]
    return sorted(temp_array) == sorted(array2)