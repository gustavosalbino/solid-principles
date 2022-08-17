# Payroll application example. Implementation of design provided on
# MARTIN, R. C. Clean Architecture: A Craftsman’s Guide to Software Structure and Design. Prentice Hall, 2017

# Violation example:
class Employee:
    """
    The creation of an Employee class to handle different employee related functions is a natural idea for this kind
    of application. However, this can lead to methods that concern to different groups of stakeholders, therefore making
    the class a module with more than one reason to change.
    """
    def __init__(self, name, role, address=None):
        self._name = name
        self._role = role
        self._address = address

    def calculate_pay(self):
        """
        This method is of the accounting department interest, therefore is reported to the company's CFO.
        """
        pass

    def report_hours(self):
        """
        This method is of the HR department interest, therefore is reported to the company's COO.
        """
        pass

    def save(self):
        """
        This method is of the DBAs interest, therefore is reported to the company's CTO.
        """
        pass


# Solution to violation: It is possible to divide the classes so that every module has only one actor. Then, a facade
# can delegate the calls of the classes containing the actual methods. Also, a different class is created to store the
# employee data. Obs.: Since this example is for study purposes, the methods are only instatiated as simple functions
# and not implemented. This can lead to the wrong idea that the solution consists in separating every method in a
# different class. However, it is worth mentioning that every task will probably contain different methods inside a real
# payment application.


class EmployeeFacade:
    """
    It is possible to create a facade that will
    """
    def __init__(self, data):
        self.pay_calculator = PayCalculator(data)
        self.hour_reporter = HourReporter(data)
        self.saver = EmployeeSaver(data)

    def calculate_pay(self):
        self.pay_calculator.calculate_pay()

    def report_hours(self):
        self.hour_reporter.report_hours()

    def save(self):
        self.saver.save_employee()


class PayCalculator:
    def __init__(self, data):
        self.employee_data = data

    def calculate_pay(self):
        pass

    def _other_fancy_payment_algorithms(self):
        pass


class HourReporter:
    def __init__(self, data):
        self.employee_data = data

    def report_hours(self):
        pass

    def _other_fancy_report_algorithms(self):
        pass


class EmployeeSaver:
    def __init__(self, data):
        self.employee_data = data

    def save_employee(self):
        pass

    def _other_fancy_queries_optimizer(self):
        pass


class EmployeeData:
    def __init__(self, name, role, address=None):
        self._name = name
        self._role = role
        self._address = address


# Another solution: Instead of creating the facade for all methods, we can choose the most important actor and keep it
# in the original Employee class together with the data.

# noinspection PyRedeclaration
class Employee:
    def __init__(self, name, role, address=None):
        self._name = name
        self._role = role
        self._address = address

    def calculate_pay(self):
        pass

    def report_hours(self):
        pass

    def save(self):
        pass


# noinspection PyRedeclaration
class HourReporter:
    def __init__(self, data):
        self.employee_data = data

    def report_hours(self):
        pass

    def _other_fancy_report_algorithms(self):
        pass


# noinspection PyRedeclaration
class EmployeeSaver:
    def __init__(self, data):
        self.employee_data = data

    def save_employee(self):
        pass

    def _other_fancy_queries_optimizer(self):
        pass


