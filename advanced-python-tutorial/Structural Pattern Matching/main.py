value = "hello"

match value:
    case "hello":
        print('hello world')
    case "exit":
        exit()
    case _:
        print('unknown command')

if value == 'hello':
    pass
elif value == "exit":
    pass
else:
    pass

