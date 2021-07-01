#converting datas to dictionary format
employees = {
    1001: {"id": 1000, "Name": "Vishal", "Gender": "Male", "Experience": 4 ,"Department":"HR"},
    1002: {"id": 1001, "Name": "Rani", "Gender": "Female", "Experience": 1,"Department":"Technical Support"},
    1003: {"id": 1002, "Name": "Divya", "Gender": "Female", "Experience": 2,"Department":"Junior Trainee"},
    1004: {"id": 1003, "Name": "Jyothy", "Gender": "Female", "Experience": 3,"Department":"Technical Lead"},
    1005: {"id": 1000, "Name": "Venu", "Gender": "Male", "Experience": 1,"Department":"Program coordinator"},
    1006: {"id": 1001, "Name": "Manu", "Gender": "Male", "Experience": 6,"Department":"Technical Support"},
    1007: {"id": 1002, "Name": "Jose", "Gender": "Male", "Experience": 3,"Department":"Technical Support"},
    1008: {"id": 1003, "Name": "Munna", "Gender": "Male", "Experience": 3,"Department":"Program assistant"},
    1009: {"id": 1003, "Name": "Rose", "Gender": "Female", "Experience": 2,"Department":"Software Tester"},
    1010: {"id": 1003, "Name": "Sam", "Gender": "Male", "Experience": 5,"Department":"QA"}
}

#function for accepting id ,property and to print the result
def getemployeedetails(**kwargs):
    id = kwargs["id"]
    if id in employees:
        print("Employee Name : ",employees[id]["Name"])
        if prop in employees[id]:
            print(prop," : ",employees[id][prop])
        else:
            print(prop,":","Not Available")
    else:
        print("ID ", id, " Doesnt Exist")
id=(int(input("Enter ID :")))          #inputting ID
prop=input("Enter Property :")         #inputting property
getemployeedetails(id=id,prop=prop)    #function call with arguments id and prop

