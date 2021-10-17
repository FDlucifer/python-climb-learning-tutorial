mynumbers = [5,7,18,28,8,2,3,109,4,23,56,4,5]

def process_number(n):
    return n ** 2 + 5

myresults = [result for x in mynumbers if (result := process_number(x)) < 100]
print(myresults)

myresults1 = [process_number(x) for x in mynumbers if process_number(x) < 100]
print(myresults1)