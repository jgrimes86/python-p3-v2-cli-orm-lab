from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    return [print(employee) for employee in employees]


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    if employee := Employee.find_by_name(name):
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(
        f"Employee {id_} not found"
    )


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee.create(name, job_title, int(department_id))
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error creating employee: ", exc)
# ### _NOTE: inputing a number into CLI creating a string?  Needed to turn into integer for Employee department_id property to not raise exception.

def update_employee():
    _id = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(_id):
        try:
            name = input("Enter the employee's name: ")
            employee.name = name
            job_title = input("Enter the employee's job title: ")
            employee.job_title = job_title
            department_id = input("Enter the employee's department's id: ")
            employee.department_id = int(department_id)
            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employe: ", exc)
    else:
        print(f"Employee {_id} not found")


def delete_employee():
    _id = input("Enter employee's id: ")
    if employee := Employee.find_by_id(_id):
        employee.delete()
        print(f"Employee {_id} deleted")
    else:
        print(f"Employee {_id} not found")


def list_department_employees():
    department_id = input("Enter department id: ")
    if department := Department.find_by_id(department_id):
        employees = department.employees()
        [print(employee) for employee in employees]
    else:
        print(f"Department {department_id} found")