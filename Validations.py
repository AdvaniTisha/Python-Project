def isValidId(id):
    if(id.isdigit()):
        if(len(id)==6):
            return True
        else:
             print("Length must be 6 digit..")
             return False
    else:
        print("Invalid name...Enter only digits..")
        return False
        


def isValidName(name):
    n=name.split()
    for i in n:
        if i.isalpha():
            if(i.istitle()):
                return True
            else:
                print("First letter should be capital")
                return False
        else:
            print("Name should contain only alphabets..")
            return False

def isValidSal(sal):
    if(sal.isdigit()):
        s=int(sal)
        if(s >0):
            return True
        else:
            print("Salary must be greater than 0")
            return False
    else:
        print("Salary should be in digits..")
        return False

def isValidAge(age):
    if(age.isdigit()):
        a=int(age)
        if(a>18 and len(age)==2):
            return True
        else:
            print("Age must be greater than 18")
            return False
    else:
        print("Age must contain only digits")
        return False

def isValidGender(gender):
    g=['Male','Female','Others']
    if(gender.isalpha()):
        if( gender in g ):
            return True
        else:
            print("Invalid gender Type ")
            return False
    else:
        print("Gender must contain alphabets only..")

def isValidAddress(address):
    if(address.isalpha()):
        return True
    else:
        print("Invalid Address..")
        return False

def isValidCity(city):
    c=['Mumbai','Pune','Hyderabad','Chennai','Kolkata','Delhi','Lucknow','Patna','Surat','Nagpur']
    if(city.isalpha()):
        if( city in c):
            return True
        else:
            print("Invalid city name..")
            return False
    else:
        print("City name should contain alphabets only..")
        return False

def isValidDate(dob):
    if(len(dob)==10):
            d1=dob[0:2]
            d2=dob[3:5]
            d3=dob[6:]
            if(d1.isdigit() and d2.isdigit() and d3.isdigit()):
                return True
            else:
                print("Invalid")
                return False
        
    else:
        print("Invalid Date...")
        return False

def isValidDept(dept_name):
    if(dept_name.isalpha()):
        return True
    else:
        return False

def isValidPan(pan):
    if len(pan)==10:
        p1=pan[0:5]
        p2=pan[5:9]
        p3=pan[9:]

        if( p1.isalpha()):
            if(p2.isdigit()):
                if(p3.isalpha()):
                    return True
    else:
        print("Length must be equal to 10")
        return False
        

def isValidAadhar(aadhar):
    if(len(aadhar)==12):
       if(aadhar.isdigit()):
           return True
        
    else:
        print("Length must be equal to 12")
        return False
        


                
                
                
        
        
        
            
