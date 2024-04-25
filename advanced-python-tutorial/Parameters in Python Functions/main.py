def myfunction(p1, /, p2, *, p3):
    print(p1, p2, p3)

# myfunction(10, 20, 30)
myfunction(10, p2=50, p3=40)
