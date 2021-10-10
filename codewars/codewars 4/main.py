# Who likes it?

def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) < 4:
        result = names[0]
        for i in range(1, len(names[1:]) + 1):
            symbol = ", " if i != len(names[1:]) else " and "
            result += symbol + names[i]
        if len(names) == 1:
            result += " likes this"
        else:
            result += " like this"
        return result
    else:
        result = f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
        return result