class Dog:
    """小狗类"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} sit down")
    def roll_over(self):
        print(f"{self.name.title()} rolled over")
my_doy = Dog('white', 10)
my_doy.sit()
my_doy.roll_over()