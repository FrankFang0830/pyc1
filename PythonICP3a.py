class Employee(object):
    _num=0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family= family
        self.salary=salary
        self.department=department
    def getName(self):
        return self.name;
    def getFamily(self):
        return self.family;
    def getSalary(self):
        return self.salary;
    def getDepartment(self):
        return self.department

class Fulltime_Employee(Employee):
    pass

employee1=Employee("Peihao Fang","family","2000","Development")
employee2=Employee("PF","family","5000","Development")
employee3=Employee("Frank Fang","family","7000","HumanResource")

employees=[employee1,employee2,employee3]
n=0
numD=0     #total number of employees in development
numHR=0    #total number of employees in HumanResource
salaryD=0   #total salary of employees in HumanResource
salaryHR=0
while n<len(employees):
    if employees[n].getDepartment()=="Development":
        numD=numD+1
        salaryD=int(employees[n].getSalary())+salaryD
    elif employees[n].getDepartment()=="HumanResource":
        numHR=numHR+1
        salaryHR=int(employees[n].getSalary())+salaryHR
    n=n+1
print('The average salary of Development is %d' %(salaryD/numD))
print('The average salary of HumanResource is %d' %(salaryHR/numHR))
print("The total number of Development is %d"% numD)
print("The total number of Human resource is %d"% numHR)
fulltimeEmployee=Fulltime_Employee("Peihao Fang","family","2000","Development")
print("The name is %s" %fulltimeEmployee.getName())
print("The salary is %s" %fulltimeEmployee.getSalary())
print("The department is %s" %fulltimeEmployee.getDepartment())