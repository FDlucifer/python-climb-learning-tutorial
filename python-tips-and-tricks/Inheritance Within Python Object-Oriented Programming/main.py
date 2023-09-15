from aircraft import AirCraft, Plane

zeppelin = AirCraft("fdvoid0", "LZ 129")

print(zeppelin.make)
print(zeppelin.takeoff())

tomcat = Plane("fdluci", "f14", 2)

print(tomcat.model)
print(tomcat.takeoff())
