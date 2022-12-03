#Association
class A():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums(self):
        self.b + self.c


class B():
    def __init__(self, d, e):
        self.d = d
        self.e = e

    def addAllNums(self, Ab, Ac):
        x = self.d + self.e + Ab + Ac
        return x

ting = A("yo", 2, 6)
ling = B(5, 9)

print(ling.addAllNums(ting.b, ting.c))


#Composition ппппваыыицитп
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
       return (self.pay * 12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total()+self.bonus)


obj_emp = Employee(100, 10)
print(obj_emp.annual_salary())


#Aggregation
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
       return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return "Total: " + str(self.pay.get_total() + self.bonus)


obj_sal = Salary(100)
obj_emp = Employee(obj_sal, 10)
print(obj_emp.annual_salary())
