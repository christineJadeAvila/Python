class Robot:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduceYourSelf(self):
        print("ROBOT COLOR: " + self.color)
        print("my name is " + self.name)
        print("age: ")
        print(self.age)
        print(" ")

robot1 = Robot("Jade", 19, "Violet")
robot2 = Robot("Erecka", 19, "Green")

robot1.introduceYourSelf()
robot2.introduceYourSelf()

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0

for number in range(len(num)):

    sum = sum + number

    print(number)