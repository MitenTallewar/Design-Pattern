class Student:

    innerstudentref = None

    class InnerStudent:
        def __init__(iself,sid,snm):
            iself.StudentId = sid
            iself.StudentName =snm

    def __init__(self,sid,snm):
        if Student.innerstudentref ==  None:
            Student.innerstudentref = Student.InnerStudent(sid,snm)
        else:
            Student.innerstudentref.StudentId = sid
            Student.innerstudentref.StudentName = snm
    def __str__(self):
        return f"""
        Student ID : {Student.innerstudentref.StudentId},
        Student Name : {Student.innerstudentref.StudentName}
        """

s1 =Student(101,'Miten')
s2 = Student(102,'Pranav')
print(s1)
print(s2)
print(id(s1))
print(id(s2))
