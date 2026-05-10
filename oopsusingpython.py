class StudentIdCard:
    college="Government Engg. College Aurangabad"
    branch="CSE(DS)"
    def __init__(self):
        self.studname=input("Enter the name of the student: ")
        self.idnum=int(input("Enter the registration number: "))
    def generateIdcard(self):
        self.idc=f'''
        
        Name: {self.studname}
        Branch: {self.branch}
        Registration number: {self.idnum}
        College: {self.college}
        '''
        border()
        print(self.idc)
        border()
        
@staticmethod
def border():
    for n in range(55):
        print("-",end="")

print(__name__)
student1id=StudentIdCard()

student1id.generateIdcard()


student2id=StudentIdCard()


student2id.generateIdcard()


        