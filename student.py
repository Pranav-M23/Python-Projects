class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch

    def display(self):
        print(f"Name-{self.name},Age-{self.age},Branch-{self.branch}")


students=[]


def add_student():
    name=input("Enter name")
    age=input("Enter age")
    branch=input("Enter branch")
    students.append(Student(name,age,branch))

def delete_student():
    name=input("Which student to delete")
    for s in students:
        if s.name==name:
           students.remove(s)
           print(f"Student-{name} deleted")
           return
        
    print("Not Found")

def update_student():
    name=input("Which name to update")
    for s in students:
        if s.name==name:
            s.age=input("Enter new age")
            s.branch=input("Enter updated branch")
            return
        
    print("Not Found")

def display_student():
    for s in students:
        s.display()


while True:
    print("\n1.Add 2.Delete 3.Update 4.Show 5.Exit \n")
    choice=input("Enter choice")
    if choice=="1":
        add_student()
    elif choice=="2":
        update_student()
    elif choice=="3":
        delete_student()
    elif choice=="4":
        display_student()
    elif choice=="5":

        
        break
    else:
        print("Invalid choice")


         