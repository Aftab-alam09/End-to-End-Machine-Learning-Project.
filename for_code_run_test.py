class animal:
    def __init__(self, Breed, age):
        self.Breed = Breed
        self.age=age
        print(f"the animal's breed is {Breed} and the age is {age}")

    def sound(sound):
        return f"the animal sounds like{sound}"
    
class Dog(animal):
    def __init__(self,Breed,age,name):
        super().__init__(Breed,age)
        self.name=name
        print("details filled successfully")

    def display_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.Breed}")
        print(f"Age: {self.age}")

dog1=Dog("any",0,"whatever")
display_info=dog1.display_info()
print(display_info)
