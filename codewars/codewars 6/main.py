def expanded_form(num):
    number_length = len(str(num))
    final_string = ""
    while number_length > 0 and num != 0:
        final_string += str((num // (10 ** (number_length - 1))) * (10 ** (number_length-1)))
        num -= (num // (10 ** (number_length - 1))) * (10 ** (number_length - 1))
        if number_length != 1:
            final_string += " + "
        number_length = len(str(num))
    return final_string.strip(" ").strip("+").strip(" ")

print(expanded_form(70304))
