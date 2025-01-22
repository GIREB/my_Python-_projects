class worker():
    def __init__(self,name,salary,department):
        print("the init function of worker class")
        self.name=name
        self.salary=salary
        self.department=department
    def Show_Infos(self):
        print("ınformations of class worker:")
        print("name:{}\nsalary:{}\ndepartment:{}\n".format(self.name,self.salary,self.department))
    def change_department(self,new_dep):
        self.department=new_dep

###inheritance
class Manager(worker):
    def give_rise(self,amount_of_rise):
        self.salary+=amount_of_rise
manager=Manager("can",50000,"ceo")
manager.Show_Infos()
manager.give_rise(20000)
manager.Show_Infos()


