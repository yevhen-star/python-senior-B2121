import requests


def first_function():
    pass



class Human:
    pass

rq = requests


print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(__name__)


print(type(Human))
print(type(first_function))

list_cat = []

for method in dir(list_cat):
    print(method)

print("==========================================")
for method in dir():
    print(method)


print("==========================================")
name = "hello"
print(hasattr(name, "lower"))
print(getattr(name, "index"))
print(callable(name))
print(callable(first_function))


print("==========================================")


class Animal:
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass


print("subclass = ", issubclass(Animal, Cat))
print("subclass = ", issubclass(Cat, Animal))

vaska = Cat()

print("instance = ", isinstance(Animal, Cat))
print("instance = ", isinstance(vaska, Animal))
print("instance = ", isinstance(Cat, Animal))