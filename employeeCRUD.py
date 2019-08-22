import os

file_name: str = 'employees.csv'

print(os.path.exists(file_name))

class Employee:
    '''
    A class used to represent an Animal
    ...

    Attributes
    ----------
    id: int
        an integer representing an employee's id number

    name: str
        The name of the employee

    dept: str
        the department an employee works for

    '''

    def __init__(self, id: int, name: str, dept: str):
        self._id = id
        self._name = name
        self._dept = dept


lance: Employee = Employee(975, 'Lance', 'Student')


def to_string(employee: Employee):
    print('{}, {}, {}'.format(employee._id, employee._name, employee._dept))


def db_create(employee: Employee) -> bool:
    '''
    A function which takes an employee instance and writes it to the file as
    long as there is not already an instance in existence with the same id #

    Parameters
    ----------
    employee: Employee
        An instance of an employee object which


    Returns
    -------
    success : bool
        A boolean which indicates whether or not the operation was successful
    '''
    if (os.path.exists(file_name)):
        pass
