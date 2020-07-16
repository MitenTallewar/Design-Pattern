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
