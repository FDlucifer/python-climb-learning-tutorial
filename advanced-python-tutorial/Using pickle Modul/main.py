import pickle

class example_class:
    a_number = 35
    a_string = "lucifer11"
    a_list = [1,2,3]
    a_dict = {"first": "a", "second": 2, "third": [1,2,3]}
    a_tuple = (22, 23)

my_object = example_class()

my_pickled_object = pickle.dumps(my_object)
print(f"this is my pickled object:\n{my_pickled_object}\n")

my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_object)
print(
    f"a_dict of unpickled object:\n{my_unpickled_object.a_dict}\n"
)
