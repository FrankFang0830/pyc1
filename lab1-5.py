# five classes {person passenger employee flight mileage member }
# each classes have their initialize method
class Person(object):  # person is a father
    def __init__(self, name, phone_num,id):
        self.name = name
        self.phone_num = phone_num
        self.id = id

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone_num

    def getID(self):
        return self.id


class Employee(Person):  # employee inherit person
    def __init__(self, name, phone_num, id, dept):
        super(Employee, self).__init__(name, phone_num,id)  # super call father's init method
        self.dept = dept

    def getDept(self):
        return self.dept


class Flight(object):  # flight is a father
    def __init__(self, start, dest, fid):
        self.fid = fid
        self.start = start
        self.dest = dest

    def getFid(self):
        return self.fid

    def getStart(self):
        return self.start

    def getDest(self):
        return self.dest


class Passenger(Person, Flight):  # passenger multiple inherit person and flight
    def __init__(self, name, phone_num, id, start, dest, fid):
        self.name = name
        self.phone_num = phone_num
        self.id = id             # passenger's id is private ,can't call it directly.
        self.fid = fid
        self.start = start
        self.dest = dest
    def setId(self,id):
        self.id=id


class MileageMember(Passenger):  # Mileage member inherit passenger
    def __init__(self, name, phone_num, id, start, dest, fid, level):
        super(MileageMember, self).__init__(name, phone_num, id, start, dest, fid)  # super call father's init method
        self.__level = level

    def getLevel(self):  # member's level is private we can't call it by member.level
        return self.__level  # we have to use get function to call it
    def setLevel(self,level):
        self.__level=level

person1=Person("Peihao","8167397505","6")
employee1 = Employee("Peihao Fang", "10086", "0001", "Development")
flight1=Flight("Kansas","Dallas","DL1")
pa1=Passenger("Peihao Fang","816","6","Kansas","Dallas","DL1")
mm1 = MileageMember("fang", '12123', '0001', 'beijing', 'kansas', 'DL1212', "diamond")
print("The personal id is ",person1.getID())
print("This employee belongs to",employee1.dept)
print("The flight number is %s from %s to %s" % (flight1.fid,flight1.start,flight1.dest))
print("The id:%s is a %s member"% (mm1.id,mm1.getLevel()))
mm1.setLevel('Gold')
print("After changed is a %s member"% mm1.getLevel())