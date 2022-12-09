from controller.read import readEmployees, readHours
from controller.write import writeEmployees

class Salary:

    def __init__(self) -> None:
        self.json_dir = 'static/hours.json'
        self.txt_dir = 'files/input/employees.txt'
        self.salary_dir = 'files/output/employees.txt'

    def splitWorkers(self, employees):
        """Separates the employees from TXT file and returns the values to be paid

        Args:
            employees (list): List of the employees entered in txt file

        Returns:
            (dict): Dictionary of the employee's name and salary to be paid
        """
        self.workers = {}
        weekdays = []
        for employee in employees:
            idx = employee.find("=")
            self.workers[employee[:idx]] = 0
            weekdays = employee[(idx+1):].replace("\n", "").split(",")
            self.splitHours(weekdays, employee[:idx])
        return self.workers

    def splitHours(self, weekdays, name):
        """Separates the work times of the week for each employee

        Args:
            weekdays (list): Employee business days
            name (str): Employee's name
        """
        weekday = ""
        time = []
        for days in weekdays:
            weekday = days[:2]
            time = days[2:].split("-")
            self.calculateHours(time, weekday, name)
            
    def arrayHours(self):
        """Get end time of time ranges

        Returns:
            (list): List with hours
        """
        self.hours_json = readHours(self.json_dir)
        self.hours = []
        for hour in self.hours_json.keys():
            self.hours.append(hour[6:])
        return self.hours


    def calculateHours(self, time, weekday, name):
        """Calculates the hours worked in each hourly range

        Args:
            time (list): Time range of a working day
            weekday (str): Day of the week [MO, TU, WE, TH, FR, SA, SU]
            name (str): Employee's name

        Returns:
            _type_: _description_
        """
        hour_difference = 0
        cont = 0
        for cont in range(0, len(self.hours)-1):
            if time[0] >= self.hours[cont] and time[0] < self.hours[cont + 1]:
                hour_difference = int(time[1][:2]) - int(time[0][:2])
                self.findCost(cont+1, weekday, hour_difference, name)
            elif time[0] >= self.hours[cont] and time[0] < "24:00":
                hour_difference = int(time[1][:2]) - int(time[0][:2])
                self.findCost(len(self.hours)-1, weekday, hour_difference, name)
                break
            cont += 1
        if hour_difference == 0:
            hour_difference = int(time[1][:2]) - int(time[0][:2])
            self.findCost(0, weekday, hour_difference, name)
        return 0

    def findCost(self, idx, weekday, h, name):
        """Calculate the total salary to be paid to the employee

        Args:
            idx (int): 
            weekday (str): Day of the week [MO, TU, WE, TH, FR, SA, SU]
            h (int): Hours worked per day
            name (str): Employee's name
        """
        hours_list = list(self.hours_json)
        key = hours_list[idx]
        for item, value in self.hours_json[key].items():
            if item.find(weekday) > -1:
                self.workers[name] += value * h
    
    def main(self):
        """Main method
        """
        if __name__ == "__main__":
            self.arrayHours()
            writeEmployees(self.salary_dir, self.splitWorkers(readEmployees(self.txt_dir)))


prueba = Salary()
prueba.main()
