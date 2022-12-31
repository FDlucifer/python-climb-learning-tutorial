numbers = [18,14,29,22,109,178,44,15,36,99,103]

found = False

for number in numbers:
    if number % 5 == 0:
        print(f"found a number! {number} is divisible by 5!")
        found = True
        break
    else:
        print(f"{number} is not divisible by 5!")

if not found:
    print("no number divisible by 5 was found!")

