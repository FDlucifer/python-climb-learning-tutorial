for i in range(10):
    for j in range(5):
        print(f"{i=}, {j=}")
        if i + j == 10:
            print("condition met, breaking out of the loop!")
            done = True
            break
    else:
        pass
