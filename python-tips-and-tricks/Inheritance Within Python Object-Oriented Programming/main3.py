from shapes import Circle, Rectangle

circle = Circle(3, "blue")

print(circle.__dict__)
print(vars(circle))
print(Circle.__dict__)
print(circle.to_json())

rect = Rectangle(4, 5, "green")
print(rect.to_json())
