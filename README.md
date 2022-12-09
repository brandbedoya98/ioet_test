Company ACME.

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD



# Solution

Initially, I decided to use a JSON file to contain the structure of the hourly range with its respective prices, allowing modification from a single point in the project for possible future changes.

~~~json
{
  "00:01-09:00": {
​    "MO-TU-WE-TH-FR": 25,
​    "SA-SU": 30
  },
  "09:01-18:00": {
​    "MO-TU-WE-TH-FR": 15,
​    "SA-SU": 20
  },
  "18:01-00:00": {
​    "MO-TU-WE-TH-FR": 20,
​    "SA-SU": 25
  }
}
~~~

Later I created a directory for the storage of the input file and the output file where the list of employees is stored to calculate the salary and the result of each one respectively.

![image-20221208213505907](C:\Users\brahy\AppData\Roaming\Typora\typora-user-images\image-20221208213505907.png)

and finally for the logical part I decided to create 3 sessions to separate the code according to its function, the modules, the controllers and finally the main.



