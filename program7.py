print("==================STUDENT ELIGIBLITY CRITARIA FOR ADMISSSION===========================")



    


name = input("Enter Student Name: ")
marks = float(input("Enter Percentage: "))
age = int(input("Enter Age: "))

print("\nAdmission Result")
print("----------------")

if marks >= 50:
    if age >= 17:
        if marks >= 90:
            print(name, "- Admission Approved")
            print("Course Allotted: Computer Science")
            print(name," Congritulations Scholarship: 100%")
        elif marks >= 75:
            print(name, "- Admission Approved")
            print("Course Allotted: Information Technology")
            print( name,"  Congritulations you have get Scholarship: 50%")
        elif marks >= 60:
            print(name, "- Admission Approved")
            print("Course Allotted: Artifical Inteligince")
            print( name," Congritulations you have get Scholarship: 25%")
        else:
            print(name, "- Admission Approved")
            print("Course Allotted: electrical")
            print("Scholarship: No Scholarship")
    else:

        print("Admission is rejected")
        print("Reason: Minimum percentage should be 50%.")  
        print("Admission Rejected")
        print("Reason: Minimum age should be 17 years.")