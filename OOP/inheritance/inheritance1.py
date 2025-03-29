# Inheritance 
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_pay(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, salary, bonus=0, taxpc=0):
        super().__init__(name, employee_id)
        self.salary = salary
        self.bonus = bonus
        self.taxpc = taxpc

    def calculate_pay(self):
        return (self.salary - self.salary * self.taxpc) * 12 + (self.bonus - self.bonus * self.taxpc)
    
    def displayPay(self):
        print(f"Total payment for {self.name} is: {self.calculate_pay()}")
    
class ContractedEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked, taxpc = 0):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.taxpc = taxpc

    def calculate_pay(self):
        self.total_payment = self.hourly_rate * self.hours_worked
        # print(f"total_payment: %.2f" % self.total_payment)
        return (self.total_payment - self.total_payment * self.taxpc)
    
    def displayPay(self):
        print(f"Total payment for {self.name} is: {self.calculate_pay()}")
    
def main():
    salemp = SalariedEmployee("Deepak", 1, 5000, 1000, 0.1)
    salemp.displayPay()
    # print(f"Salary: {salemp.displayPay()}")
    contemp = ContractedEmployee("Ramesh", 2, 5000, 1000, 0.15)
    contemp.displayPay()
    # print(f"Salary: {contemp.displayPay()}")

if __name__ == "__main__":
    main()