from Validations import *
class Employee:
    EmpDict={}
    def __init__(self,id,name,sal,age,gender,address,city,dob,doj,dept_name,desig,pan,aadhar):
        self.id=id
        self.name=name
        self.sal=sal
        self.age=age
        self.gender=gender
        self.address=address
        self.city=city
        self.dob=dob
        self.doj=doj
        self.dept_name=dept_name
        self.desig=desig
        self.pan=pan
        self.aadhar=aadhar

        
        if self.dept_name in self.EmpDict.keys():
            self.EmpDict[self.dept_name].append(self.name)
        else:
            self.EmpDict[self.dept_name]=[self.name]

        
        

    def display(self):
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        print("ID       NAME     SALARY    AGE  GENDER     ADDRESS      CITY     DOB        DOJ      DEPT_NAME    DESIG     PAN NO           AADHAR NO       ")
        print(self.id," ",self.name," ",self.sal," ",self.age,"  ",self.gender,"  ",self.address,"  ",self.city,"  ",self.dob,"   ",self.doj,"   ",self.dept_name,"   ",self.desig,"  ",self.pan,"   ",self.aadhar)
        


    def updatesalary(self,new_sal):
        self.sal=new_sal
        print("Salary sucessfully updated")
            
                   
    @classmethod
    def SearchDept(self):
        for k,v in self.EmpDict.items():
            print("Department Details =>",k)
            for name in v:
                print(name,end=" ")
            print(" ")
emplist=[]

print("EMPLOYEE MANAGEMENT SYSTEM")


   
    
while(True):
    print("----------------------MENU--------------------")
    print("1.Add the record of employee")
    print("2.Delete the record of employee")
    print("3.Update Employee Details")
    print("4.Search details of Employee")
    print("5.Display details of Employee with highest salary")
    print("6.Display details of Employee with lowest salary")
    print("7.Display ")
    print("8.EXIT")

    choice=int(input("Enter your choice =>"))
    if(choice==1):
         while(True):
            id=input("Enter Employee id =>")
            if isValidId(id) :
                break
            else:
                print("Invalid id")

         while(True):
             name=input("Enter name of Employee =>")
             if isValidName(name):
                 break
             else:
                print("Invalid name")
         while True:
            sal=input("Enter Salary of Employee =>")
            if isValidSal(sal):
                break
            else:
                print("Invalid Salary..")

         while(True):
            age=input("Enter Age of Employee =>")
            if isValidAge(age):
                break
            else:
                print("Invalid Age..")
         while(True):
            gender=input("Enter Gender =>")
            if isValidGender(gender):
                break
            else:
                print("Invalid Gender Type..")
         while(True):
            address=input("Enter Address =>")
            if isValidAddress(address):
                break
            else:
                print("Invalid Address...")

         while(True):
            city=input("Enter City name =>")
            if isValidCity(city):
                break
            else:
                print("Invalid City")

         while(True):
            dob=input("Enter Date of Birth in format dd-mm-yyyy =>")
            if isValidDate(dob):
                break
            else:
                print("Invalid Date")

         while(True):
            doj=input("Enter Date of Joining dd-mm-yyyy =>")
            if isValidDate(doj):
                break
            else:
                print("Invalid Date")

         while(True):
            dept_name=input("Enter Department name =>")
            if isValidDept(dept_name):
                break
            else:
                print("Invalid Deptartment Name")

         while(True):
            desig=input("Enter Designation =>")
            if isValidDept(desig):
                break
            else:
                print("Invalid Designation Name")

         while(True):
            pan=input("Enter Pan Card number =>")
            if isValidPan(pan):
                break
            else:
                print("Invalid Pan number")

         while(True):
            aadhar=input("Enter Aadhar card number=>")
            if isValidAadhar(aadhar):
                break
            else:
                print("Invalid aadhar number")
         emp=Employee(id,name,sal,age,gender,address,city,doj,dob,dept_name,desig,pan,aadhar)
         emplist.append(emp)
        

         for i in emplist:
            i.display()

    elif(choice==2):
        eid=input("Enter The ID that you want to delete =>")
        for i in emplist:
            if i.id==eid:
                for v in Employee.EmpDict.values():
                    for j in v:
                        if i.name==j:
                            v.remove(j)
                
                emplist.remove(i)
                print("Record deleted successfully........")
            i.display()

    elif(choice==3):
        print("Press A to update name ")
        print("Press B to update address ")
        print("Press C to update DOB ")
        print("Press D to update  salary ")

        ch=input("Enter your choice for Update Menu =>")
        if(ch=="A" or ch=="a"):
            n=input("Enter name of Employee which you want to update =>")
            for i in emplist:
                if i.name==n:
                    flag=True
                    print("Found")
                    new_name=input("Enter new name =>")
                    emp.name=new_name
                    print("Name successfully updated...")
                    i.display()
                    break
                else:
                    flag=False
            if(flag==False):
                print("Name not Found")

        elif(ch=="B" or ch=="b"):
            eid=input("Enter Employee Id which you want to update =>")
            for i in emplist:
                if i.id==eid:
                    flag=True
                    new_address=input("Enter new address =>")
                    emp.address=new_address
                    print("Address successfully updated..")
                    i.display()
                    break
                else:
                    flag=False
            if(flag==False):
                print("ID not found...")

        elif(ch=="C" or ch=="c"):
            eid=input("Enter Employee id which you want to update =>")
            for i in emplist:
                if i.id==eid:
                    flag=True

                    new_dob=input("Enter DOB =>")
                    emp.dob=new_dob
                    print("DOB successfully updated..")
                    i.display()
                    break
                else:
                    flag=False
            if(flag==False):
                print("ID not found..")

        elif(ch=="D" or ch=="d"):
            print("a.Press a to update salary of  specific Employee by Employee id ")
            print("b.Press b to update salary of all employees working in specific department")
            print("c.Press c to update salary of all employees ")

            sub_ch=input("Enter subchoice for Update Salary MENU =>")
            if(sub_ch=="a"):
                eid=input("Enter Employee ID of which salary needs to be updated =>")
                for i in emplist:
                    flag=True
                    if(i.id==eid):
                        flag=True

                        new_sal=input("Enter new salary =>")
                        emp.sal=new_sal
                        print("Salary sucessfully updated..")
                        i.display()
                        break
                    else:
                        flag=False
                if(flag==False):
                    print("Invalid ID..")

                    
            elif(sub_ch=="b"):
                dn=input("Enter Department Name =>")
                if dn in Employee.EmpDict.keys():
                    new_sal=input("Enter New Salary =>")
                    for i in emplist:
                        flag=True
                        if i.dept_name==dn:
                           i.updatesalary(new_sal)
                           i.display()
                        else:
                            flag=False
                    if(flag==False):
                        print("Not Found ...")

            elif(sub_ch=="c"):
                new_sal=input("Enter New Salary =>")
                for i in emplist:
                    i.updatesalary(new_sal)
                    i.display()

            else:
                print("Invalid Choice...")

        
    elif(choice==4):
        
        print("Press A to search by Employee ID")
        print("Press B to search by Employee name")
        print("Press C to search by Department name")

        ch=input("Enter your choice for SEARCH MENU =>")
        if(ch=="A" or ch=="a"):
            eid=input("Enter the Employee Id to be searched =>")
            for i in emplist:
                flag=True
                if i.id==eid:
                    i.display()
                    break
                else:
                    flag=False
                
            if (flag==False):
                print("ID Not Found..")

        elif(ch=="B" or ch=="b"):
            nm=input("Enter name of Employee to be searched =>")
            for i in emplist:
                flag=True
                if i.name==nm:
                    i.display()
                    break
                else:
                    flag=False
            if(flag==False):
                print("Name Not Found..")

        elif(ch=="C" or ch=="c"):
            dn=input("Enter Department name =>")
            if dn in Employee.EmpDict.keys():
                for i in emplist:
                    flag=True
                    if i.dept_name==dn:
                        i.display()
                    else:
                        flag=False
                if(flag==False):
                    print("Not Found ...")
                        
                    
            

           
        else:
            print("Invalid choice...")

    elif(choice==5):
       
        max=0
        for i in emplist:
            s = int(i.sal)
            if s>max:
                max=s
        for i in emplist:
            s=int(i.sal)
            if s==max:
                print("Highest Salary => ")
                i.display()

    elif(choice==6):
        min=999999
        for i in emplist:
            if int(i.sal)<min:
                min=int(i.sal)
        for i in emplist:
            if int(i.sal)==min:
                print("Lowest Salary =>")
                i.display()

    elif(choice==7):
        for i in emplist:
            i.display()
        


    elif(choice==8):
        break
    else:
        print("Invalid...")
