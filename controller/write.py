from module.file import openWriteFile, closeFile

def writeEmployees(file, salary_employees):
    """Write a dictionary into TXT file

    Args:
        file (str): Name of the file
        salary_employees (dict): Dictionary with salaries per employees
    """
    salary = openWriteFile(file)
    for key, value in salary_employees.items():
        print(f"The amount to pay {key} is: {value} USD")
        line = f"The amount to pay {key} is: {value} USD\n"
        salary.writelines(line)

    closeFile(salary)