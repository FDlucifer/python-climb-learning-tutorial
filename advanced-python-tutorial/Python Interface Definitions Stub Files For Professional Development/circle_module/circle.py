import math

def area(radius):
    return radius ** 2 * math.pi

def circumference(radius):
    return 2 * radius * math.pi

def radius_from_area(area):
    return math.sqrt(area / math.pi)

def radius_from_circumference(circumference):
    return circumference / (2 * math.pi)

def circle_info(radius):
    return area(radius), circumference(radius)

