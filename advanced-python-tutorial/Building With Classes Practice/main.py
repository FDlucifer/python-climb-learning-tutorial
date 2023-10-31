class Dog:
    species = "canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)

class ReviewExercise:
    difficulty = 1

    def __init__(self, exercise, solution):
        self.exercise = exercise
        self.solution = solution
        self._secret_message = "well done!"

    def ready(self):
        print(self.exercise)

    def done(self):
        print(self._secret_message)
        print(self.solution)


class Challenge(ReviewExercise):
    difficulty = 2

    def __init__(self, exercise, solution):
        super().__init__(exercise, solution)
        self._secret_message = "you did it! congratulations!"

woolf = Dog("woolf", 1)
print(woolf)
print(woolf.species)
print(Dog.species)
print(woolf.speak("woof"))

buddy = GoldenRetriever("BUDDY", 12)
print(buddy.speak("wau"))
