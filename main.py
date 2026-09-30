

class Employee:
    def __init__(self,employee_id=None,name=None,age=None,salary=None):
        self.__employee_id=employee_id
        self.name= name
        self.age= age
        self.__salary= salary
    
    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id
    def get_employee_id(self,employee_id):
        return self.__employee_id
    def display(self):
        print(f"Employee ID is {self.__employee_id} ") 
        print(f"Employee Name is {self.name} ") 
        print(f"Employee age is {self.age} ")
        print(f"Employee Salary is {self.__salary} :") 
        
    def __def__():
        print("Object Is Deleted!!")
         
        

class Manager(Employee):
     def __init__(self,employee_id,name,age,salary,department):
         self.department=department
         super().__init__(employee_id,name,age,salary)
    
     def display(self):
         super().display()
         print(f"Departmnet is {self.department}")
         
class Developer(Employee):
    def __init__(self, employee_id, name, age, salary,programming_lang):
        self.programming_lang=programming_lang
        super().__init__(employee_id, name, age, salary)
        
    def display(self):
        super().display()

print(f"Is Manager is Sub Class of Employee Class? : {issubclass(Manager,Employee)}")        
print(f"Is Developer is Sub Class of Employee Class? : {issubclass(Developer,Employee)}")     
        
 
print("---Python OOP Project: Employee Managemnet System---")
print()
      
person=None
employee=None
manager=None

while True:
    print()
    print("Choose an option: ")
    print("1. Create a Person")
    print("2. Create an employee")
    print("3. Create a Manager")
    print("4. Show details")
    print("5.Exit")
    print()
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        
        print()
        name= input("Enter Name : ")
        age= int(input("Enter Age : "))
        person=Employee(name=name,age=age)
        print(f"Person Created With Name :{name} and Age :{age}")
        
    elif choice == 2:
        print()
        print("=== Employee ==")
        ename= input("Enter Name : ")
        eage= int(input("Enter Age : "))
        eid= int(input("Enter ID : "))
        esalary= int(input("Enter Salary : "))
        print()
        employee=Employee(ename,eage,eid,esalary)
        print(f"Employee Created With Name : {ename} ,Age : {eage} ,ID : {eid} ,Salary : ${esalary}")
        
    elif choice == 3:
        print()
        print("=== Manager ===")
        emp_name= input("Enter Name : ")
        emp_age= int(input("Enter Age : "))
        emp_id= int(input("Enter ID : "))
        emp_salary= int(input("Enter Salary : "))
        emp_department= input("Enter Department : ")
        print()
        manager=Manager(emp_name,emp_age,emp_id,emp_salary,emp_department)
        print(f"Manager created with Name :{emp_name}, Age : {emp_age},ID : {emp_id}, Salary : ${emp_salary} and Department : {emp_department}")
    
    elif choice == 4:
            print()
            print("=== Show Details ===")
            print("Choose Details To Show :")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print()
            num=int(input("Enter an Option :"))
            if num == 1:
                if person!=None:
                    print("--- Person ---")
                    person.display()
                else:
                    print()
                    print("There is No Data ")
                    print()
            elif num == 2:
                if employee!=None:
                    print()
                    print("--- Employee ---")
                    employee.display()
                    print()
                else:
                    print()
                    print("There is No Data of Employees")
                    print()
            elif num == 3:
                if manager!=None:
                    print()
                    print("--- Manager ---")
                    manager.display()   
                    print()
                else:
                    print()
                    print("There is No Data of Manager ")
                    print()
                
            else:
                print("Invalid Option Please Choose Between (1-3)")
            
    elif choice == 5:
        print("Exiting From Python OOP Project !!")
        break
    else:
        print("Invalid Choice Please Choose Between (1-5)")
        print()

        
        
        
        
        
         