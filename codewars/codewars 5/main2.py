def rot13(message):
    in_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    out_string = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    translate_dict = {in_string[i]: out_string[i] for i in range(len(in_string))}
    table = str.maketrans(translate_dict)
    return message.translate(table)
