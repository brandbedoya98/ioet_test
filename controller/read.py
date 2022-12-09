import json
from module.file import openReadFile, closeFile

def readEmployees(file):
    """Read a TXT file and convert it to a list

    Args:
        file (str): Name of the file

    Returns:
        (list): List of content TXT
    """
    
    employees = openReadFile(file)
    employees_list = employees.readlines()
    closeFile(employees)
    return employees_list


def readHours(file):
    """Read a JSON file and convert it to a dictionary

    Args:
        file (str): Name of the file

    Returns:
        (dict): JSON content dictionary
    """
    hours = openReadFile(file)
    hours_dict = json.load(hours)
    closeFile(hours)
    return hours_dict
