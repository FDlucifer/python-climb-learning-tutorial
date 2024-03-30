try:
    print(10 / 0)
except:
    print("error occured! division failed!")

print("hello")

import logging

values = [10, 5, 6, 0, 9, 8, 2]

for value in values:
    try:
        print(10 / value)
    except ZeroDivisionError as e:
        print(str(e))
    except ValueError as e:
        print(str(e))
    except Exception as e:
        logging.exception(e)

