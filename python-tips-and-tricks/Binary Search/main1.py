numbers = [257, 281, 308, 494, 344, 12, 163, 72, 231, 332, 8, 235, 441, 436, 438, 375, 71, 308, 334, 364, 224, 461, 152, 57, 261, 241, 66, 412, 495, 482, 207, 316, 259, 
77, 270, 497, 98, 27, 488, 264, 132, 29, 170, 441, 151, 204, 319, 435, 243, 409, 313, 153, 182, 22, 368, 160, 200, 45, 483, 381, 140, 158, 7, 485, 411, 260, 403, 417, 2, 223, 105, 445, 287, 276, 493, 76, 15, 290, 142, 409, 44, 73, 424, 376, 3, 56, 208, 181, 299, 36, 342, 154, 299, 81, 457, 198, 159, 424, 305, 308]

numbers.sort() # TimSort 0(n log n)

counter = 0
def binary_search(numbers_list, number, left, right):
    global counter
    counter += 1
    if left > right:
        return -1

    mid = (left + right) // 2
    if number == numbers_list[mid]:
        return mid
    elif number < numbers_list[mid]:
        return binary_search(numbers_list, number, left, mid-1)
    else:
        return binary_search(numbers_list, number, mid+1, right)

print(numbers)
print(binary_search(numbers, 497, 0, len(numbers)-1))
print(counter)