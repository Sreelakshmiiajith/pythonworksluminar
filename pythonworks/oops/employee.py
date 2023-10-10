class student:
    addno:int
    rollno:int
    name:str
    department:str
    gender:str
    def create(self,addno,rollno,name,dept,gender):
        self.addno=addno
        self.rollno=rollno
        self.name=name
        self.department=dept
        self.gender=gender
    def display_stud(self):
        print(self.addno,self.rollno,self.name,self.department,self.gender)
obj=student()
obj.create(100,18,"hari","bca","male")
obj.display_stud()

# class mobile:
#     mobileid:int
#     model:str
#     name:str
#     color:str
#     memory:int
#     price:int
#     def create(self,mbl_id,mob_model,name,clr,memory,price):
#         self.mobileid=mbl_id
#         self.model=mob_model
#         self.name=name
#         self.color=clr
#         self.memory=memory
#         self.price=price
#     def display_mbl(self):
#         print(self.mobileid,self.model,self.name,self.color,self.memory,self.price)

# class book:
#     bookid:int
#     bookname:str