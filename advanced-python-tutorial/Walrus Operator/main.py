print(myvalue := 10)

done = False
while not done:
    command = input("please enter a command ('q' for quit): ")
    if command == 'q':
        done = True
    else:
        print(f"your command was {command}")