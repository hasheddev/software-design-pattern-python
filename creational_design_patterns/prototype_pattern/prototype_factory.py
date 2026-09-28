import copy


class Address:
    def __init__(self, street_address, suite, country) -> None:
        self.suite = suite
        self.street_address = street_address
        self.country = country
    
    def __str__(self) -> str:
        return f"{self.street_address}, {self.suite}, {self.country}"

class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} works at {self.address}"



class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    branch_office_employee = Employee("", Address("123C East Dr", 0, "London"))

    @staticmethod
    def __new_employee(prototype, name, suite):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result
    
    @staticmethod
    def new_main_employee(name, suite):
        main_office_employee = EmployeeFactory.main_office_employee
        return EmployeeFactory.__new_employee(main_office_employee, name, suite)

    @staticmethod
    def new_branch_employee(name, suite):
        branch_office_employee = EmployeeFactory.branch_office_employee
        return EmployeeFactory.__new_employee(branch_office_employee, name, suite)
        
    

john = EmployeeFactory.new_main_employee("John", 101)
print(john)
jane = EmployeeFactory.new_branch_employee("Jane", 102)
print(jane)