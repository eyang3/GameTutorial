class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def kick(self, OtherPerson):
        print(self.name + ' has kicked ' + OtherPerson.name)
    
    def talk(self):
        print('I am ' + str(self.age) + ' years old')



emily = People('Emily', 9)
booger = People('Eric', 39)

emily.kick(booger)
emily.talk()