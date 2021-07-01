#converting datas to dictionary format
employees = {
    1001: {"Employee Id": 1001, "Employee Name": "Vishal", "Gender": "Male", "Years of Experiance": 2 ,"Department":"HR"},
    1002: {"Employee Id": 1002, "Employee Name": "Hima", "Gender": "Female", "Years of Experiance": 4,"Department":"Technical Support"},
    1003: {"Employee Id": 1003, "Employee Name": "Fathima", "Gender": "Female", "Years of Experiance": 1,"Department":"Junior Trainee"},
    1004: {"Employee Id": 1004, "Employee Name": "Jeeva", "Gender": "Male", "Years of Experiance": 4,"Department":"Technical Lead"},
    1005: {"Employee Id": 1005, "Employee Name": "Gini", "Gender": "Female", "Years of Experiance": 3,"Department":"Program Coordinator"},
    1006: {"Employee Id": 1006, "Employee Name": "Manu", "Gender": "Male", "Years of Experiance": 7,"Department":"Technical Lead"},
    1007: {"Employee Id": 1007, "Employee Name": "Jennifier", "Gender": "Female", "Years of Experiance": 3,"Department":"Technical Support"},
    1008: {"Employee Id": 1008, "Employee Name": "Mithun", "Gender": "Male", "Years of Experiance": 2,"Department":"Program Trainee"},
    1009: {"Employee Id": 1009, "Employee Name": "Kavitha", "Gender": "Female", "Years of Experiance": 1,"Department":"Software Training"},
    1010: {"Employee Id": 1010, "Employee Name": "Sakthi", "Gender": "Male", "Years of Experiance": 4,"Department":"Technical Support"}
}

#function for accepting id ,property and to print the result
def getemployeedetails(**kwargs):
    id = kwargs["id"]
    if id in employees:
        print("Employee Name : ",employees[id]["Employee Name"])
        if prop in employees[id]:
            print(prop," : ",employees[id][prop])
        else:
            print(prop,":","Not Available")
    else:
        print("ID ", id, " Doesnt Exist")
id=(int(input("Enter ID :")))          #inputting ID
prop=input("Enter Property :")         #inputting property
getemployeedetails(id=id,prop=prop)    #function call with arguments id and prop

