class Person:
    def __init__(self,id,nm,age):
        self.PersonId = id
        self.PersonName =nm
        self.PersonAge =age

class Student(Person):
    def __init__(self,id,nm,age,fees,clg):
        super().__init__(id,nm,age)
        self.StudentFees =fees
        self.StudentCollege = clg

    def __str__(self):
        return f"""
        Student Id : {self.PersonId}
        Student Name : {self.PersonName}
        Student Age : {self.PersonAge}
        Student Fees : {self.StudentFees}
        Student College : {self.StudentCollege}
        """


class Employee(Person):
    def __init__(self,id,nm,age,sal,comp):
        super().__init__(id,nm,age)
        self.EmployeeSalary = sal
        self.EmployeeCompany = comp

    def __str__(self):
        return f"""
        Employee Id : {self.PersonId}
        Employee Name : {self.PersonName}
        Employee Age : {self.PersonAge}
        Employee Salary : {self.EmployeeSalary}
        Employee Company : {self.EmployeeCompany}
        """

class PersonFactory:
    @staticmethod
    def get_person(whichype,id,nm,age,amnt,org):
        if type(id) == int and id >0 and type(age)== int and age>0:
            if whichype == "E":
                if age> 22:
                    return Employee(id,nm,age,amnt,org)
                else:
                    print('age shuld be greater than 22')
            elif whichype == "S":
                if age > 6:
                    return Student(id,nm,age,amnt,org)
                else:
                    print('age should be greater than 6')
        raise BaseException("Invalid Person type")

p1 = PersonFactory.get_person('S',1,'Miten',26,50000.00,'Capegimini')
print(p1)
print(type(p1)== Person)
print(type(p1)== Employee)
print(type(p1)== Student)
print("-------------")
print(isinstance(p1,Person))
print(isinstance(p1,Employee))
print(isinstance(p1,Student))
