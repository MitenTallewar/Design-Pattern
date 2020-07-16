import copy
class Person:
    def __init__(self,pid,pnm,pag,pgen):
        self.PersonId = pid
        self.PersonName =pnm
        self.PersonAge =pag
        self.PersonGender = pgen

    def __str__(self):
        return f"""
        Person ID :{self.PersonId}
        Person Name :{self.PersonName}
        Person Age :{self.PersonAge}
        Person Gender :{self.PersonGender}        
    """

    def __repr__(self):
        return str(self)

    def get_clonned_instance(self):
        return copy.copy(self)

p1 =Person(1,'Miten',26,'Male') #entire chain execution  class loading + constructor -  more time required
p2 =p1.get_clonned_instance() #simply memory dump
p2.PersonName ='Pranav'
print(id(p1))
print(id(p2))
print(p1)
print(p2)