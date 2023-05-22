class myclass:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print("hello my name is:-",self.name)
        print("my roll no is:-", self.rollno)
        print("my maeks is:-", self.marks)

s=myclass('sudesh',102,28)
print(s.__dict__)
s.talk()