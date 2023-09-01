from mailbox import linesep
from payroll import *
import os, os.path, shutil

"""I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy.
June 9th, 2022
Ash Olson
"""

PAY_LOGFILE = 'paylog.txt'
EMPLOYEE_FILE = 'employees.csv'
TIMECARDS = 'timecards.csv'
RECEIPTS = 'receipts.csv'
employees = []

def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘paylog.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees: # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification # object to compute the pay
        
def load_employees(): #done
    with open(EMPLOYEE_FILE) as file:
        for line in file:
            this = line.split(',')
            if this[0] != 'id': #removes the first line
                emp = Employees(this[0], this[1], this[2], this[3], this[4], this[5], this[6], this[7], this[8], this[9], this[10]) #creates each employee
                employees.append(emp) #adds to the employee list


# The process_timecards function reads timecards.csv and adds each hourly record to a list of floats representing the hours worked in the Hourly employee’s Hourly classification object. The timecards.txt file contains the IDs of hourly employees and their timecard entries:

def process_timecards(): #check
    with open(TIMECARDS) as file: #gets the file for reading
        lines = file.readlines() #gets the lines
        for line in lines: #goes thru lines
            hours = line.split(',') #makes a list of the receipts
            emp_id = hours[0]
            emp = find_employee_by_id(emp_id) #finds each emp in receipts
            emp.classification.hours_and_timecards = hours[1:] #gives it to compute
    with open(TIMECARDS, "w+") as file:
        file.write('') #gets rid of old hours

def process_receipts(): ##still need to do
    with open(RECEIPTS) as file: #gets the file for reading
        lines = file.readlines() #gets the lines
        for line in lines: #goes thru lines
            receipts = line.split(',') #makes a list of the receipts
            emp_id = receipts[0]
            emp = find_employee_by_id(emp_id) #finds each emp in receipts
            emp.classification.hours_and_timecards = receipts[1:] #gives it to compute
    with open(RECEIPTS, "w+") as file:
        file.write('') #gets rid of old hours

def find_employee_by_id(id): #done!
    for emp in employees: #goes thru each in the list
        if emp.emp_id == id: #checks for a match
            return emp #returns the Employee with the id

class Classification: #done!
    
    hourly_rate = 0
    salary = 0
    commission_rate = 0
    emp_id = ""
    hours_and_timecards = []
    
    def __init__(self, sal, commish, hour, emp): #initializes
        self.hourly_rate = hour
        self.salary = sal
        self.commission_rate = commish
        self.emp = emp
        self.emp_id = emp.emp_id
    
    '''creates abstract functions'''
    
    def add_timecard():
        pass
    
    def compute_pay():
        pass
    
    def add_receipt():
        pass
    
class Hourly(Classification): #almost
    
    def __init__(self, hour, emp):
        self.hourly_rate = hour
        self.emp = emp
        
    def add_timecard(self, time): #done!
        with open(TIMECARDS, 'r+') as file:
            is_in = False               #checks if the emp is already in there
            lines = file.readlines()
            if len(lines) == 0:                            #first line
                lines = str(self.emp.emp_id) + "," + str(round(time, 1))
            else: #new id
                for i in range(0, len(lines)):
                    check_id = lines[i].split(',')
                    if check_id[0] == self.emp.emp_id:    #checks each line for the id
                        data = lines[i]
                        data = data.replace('\n', '')
                        data += "," + str(round(time, 1))
                        lines[i] = data      #adds the new data to each line
                        is_in = True
                if is_in != True: #id isnt in timecards
                    lines.append('\n' + str(self.emp.emp_id) + "," + str(round(time, 1)))
                
        with open(TIMECARDS, "w+") as file:    #writes in the new lines
            file.seek(0)
            file.writelines(lines)
            file.truncate()
    
    def compute_pay(self): #wrong amount
        process_timecards()
        total = 0
        for i in range(len(self.hours_and_timecards)): #reads each hour
            total += float(self.hours_and_timecards[i]) * float(self.hourly_rate) #adds hours to total
        return total

class Salaried(Classification): #issues twice
    
    def __init__(self, sal, emp):
        self.salary = sal
        self.emp = emp
        
    def compute_pay(self):
        return float(self.salary) / 24

class Commissioned(Salaried): #fix the pay
    
    def __init__(self, sal, commish, emp):
        self.commission_rate = commish
        self.salary = sal
        self.emp = emp
        
    def add_receipt(self, amount): #done!
         with open(RECEIPTS, 'r+') as file:
            is_in = False       #checks if the emp is already in there
            lines = file.readlines()
            if len(lines) == 0:     #first line
                lines = str(self.emp.emp_id) + "," + str(round(amount, 2)) + "\n"
            else: #new id
                for i in range(0, len(lines)):
                    check_id = lines[i].split(',')
                    if check_id[0] == self.emp.emp_id: #checks each line for the id
                        data = lines[i]
                        data = data.replace('\n', '')
                        data += "," + str(round(amount, 2))
                        lines[i] = data   #adds the new data to each line
                        is_in = True
                if is_in != True: #id isnt in timecards
                    lines.append('\n' + str(self.emp.emp_id) + "," + str(round(amount, 2)))
                
            with open(RECEIPTS, 'w+') as file:         #writes in the new lines
                file.seek(0)
                file.writelines(lines)
                file.truncate()
        
    def compute_pay(self):
        process_receipts()
        total = 0
        for i in range(len(self.hours_and_timecards)): #reads each hour
            total += float(self.hours_and_timecards[i])
        total = total * float(self.commission_rate) / 100
        total += float(self.salary) / 24
        return total

class Employees: #done!
    emp_id = ""
    first_name = ""
    last_name = ""
    address = ""
    city = ""
    state = ""
    zipcode = ""
    classification = Classification
    
    def __init__(self, id, first, last, add, city, state, zip, classif, sal, commish, hour):
        self.emp_id = id
        self.first_name = first      #initializes everything
        self.last_name = last
        self.address = add
        self.city = city
        self.state = state
        self.zipcode = zip
        if classif == '1':           #classifies it
            self.make_salaried(sal)
        elif classif == '2':
            self.make_commissioned(sal, commish)
        elif classif == '3':
            self.make_hourly(hour)
            
    def make_hourly(self, hour):
        self.classification = Hourly(hour, self) #changes to hour
    
    def make_salaried(self, sal):
        self.classification = Salaried(sal, self) #changes to salaried
    
    def make_commissioned(self, sal, plus):
        self.classification = Commissioned(sal, plus, self) #changes to commissioned
    
    def issue_payment(self):
        money = self.classification.compute_pay() #sends to classifs to figure outhutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
        lines = []
        if os.path.exists('paylog.txt'):
            with open(PAY_LOGFILE, "a+") as file: #opens PAY_LOGFILE for writing
                lines = file.readlines()
                file.seek(0)
                file.writelines(lines) #puts back the text
                file.writelines("Mailing " + str(round(money, 2)) + " to " + self.first_name + " " + self.last_name + " at " + self.address + " " + self.city + " " + self.state + " " + self.zipcode + "\n") #'mails' wage
        else:
            with open(PAY_LOGFILE, "w") as file: #makes a new one if it doesnt exist
                file.writelines("Mailing " + str(round(money, 2)) + " to " + self.first_name + " " + self.last_name + " at " + self.address + " " + self.city + " " + self.state + " " + self.zipcode + "\n") #'mails' wage

'''
    p5.py: Illustrates the payroll module.
'''
from payroll import *
import os, os.path, shutil
def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()
    # Save copy of payroll file; delete old file
    shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()
    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()
    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()

if __name__ == '__main__':
    main()