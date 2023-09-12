class Employe:
    def __init__(self,name1, id1):
        self.id = id1
        self.name = name1
    def display(self):
        print(self.id,self.name)




emp1 = Employe("akhil",111)
emp1.display()
emp2 = Employe("abcd",33)
emp2.display()
