class Employee:
    """
    Generic Employee class with name, family, salary and department
    """

    # data member to count the number of Employees
    no_of_employees = 0

    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(employees):
        """
        function to average salary
        """
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees


class Full_time_Employee(Employee):
    """
    Full Time Employee is a sub class of Employee
    """

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("Benefits as full time employee.")


def main():
    employees = []
    fte1 = Full_time_Employee("Employee1", "FamilyName1", 120000, "Management")
    fte1.full_time_benefits()
    employees.append(fte1)
    fte2 = Full_time_Employee("Employee2", "FamilyName2", 180000, "RnD")
    employees.append(fte2)
    employee1 = Employee("Employee3", "FamilyName3", 160000, "Marketing")
    employees.append(employee1)
    employee2 = Employee("Employee4", "FamilyName4", 135000, "HR")
    employees.append(employee2)
    print("Average-salary:", Full_time_Employee.average_salary(employees))


if __name__ == "__main__":
    main()