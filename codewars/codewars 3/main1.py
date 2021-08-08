# Create Phone Number

def create_phone_number(n):
    numbers = "".join([str(num) for num in n])
    return f"({numbers[:3]}) {numbers[3:6]}-{numbers[6:]}"