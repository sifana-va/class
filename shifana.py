# class employee:
#     name="ram"
#     age=30
#     place="calicut"
#     def display(self):
#         print(self.name,self.age,self.place)
# obj1=employee()
# obj1.display()
# class employee:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("place:",self.place)
# obj1=employee("sita",34,"calicut")
# obj1.display()
# obj2=employee("ram",45,"kottayam")
# obj2.display()  
# obj3=employee("setu",67,"kollam")  
# obj3.display()


class students:
    count=0
    def __init__(self,name,id,place):
        self.name=name
        self.id=id
        self.place=place
        students.count=students.count+1
    def display(self):
        print("name:",self.name)
        print("id:",self.id)
        print("place:",self.place)
    def studentscount(self):
        print("total no of students is %d" %(students.count))
student1=students("fath",5647,"cvd")
student1.display()
student2=students("faz",1234,"kzpb")
student2.display()
student3=students("niz",8976,"therat")
student3.display()
student4=students("jaz",65784,"potty")
student4.display()
student4.studentscount()
