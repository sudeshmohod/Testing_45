class Person:
    '''this simple code i used'''
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('John', 25)
print(p.name,p.age)
print(p.__doc__)
class Person:
    '''this other code used'''
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)
    print(f"I'm {person.name}. I'm {person.age} years old.")
print(person.__doc__)