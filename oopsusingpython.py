class StudentIdCard:
    college="Government Engg. College Aurangabad"
    branch="CSE(DS)"
    def __init__(self,name,regno):
        self.studname=name
        self.idnum=regno
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
student1id=StudentIdCard("Pallavi Kumari",23153147028)

student1id.generateIdcard()


student2id=StudentIdCard("Akarsh Kumar Mishra",24153147901)


student2id.generateIdcard()


        