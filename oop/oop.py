# OOP 
class EmployeesRecord:
    def__init__(self, empName, empMobile, empSalary, empPosition):
    self.employeeName = empName
    self.employeeMobile = empMobile
    self.employeeSalary = empSalary
    self.employeePosition = empPosition

class Accounting:
    def__init__(self):
    self.profit = 15000
    self.sale = 45000
    self.salaries = 10000

class Marketing:
    def__init__(self):
    self.pendingOrders = 20
    self.deliveredOrders = 15
    self.totalOrders = 50

empObject = EmployeesRecord("Parker", "+639155517080", 2000, "Developer")

accountingObject = Accounting()
print(empObject.employeeName)
print(empObject.employeeSalary)
print(accountingObject.profit)