class worker():
    def __init__(self,name,salary,department):
        print("the init function of worker class")
        self.name=name
        self.salary=salary
        self.department=department
    def Show_Infos(self):
        print("Informations of class worker:")
        print("name:{}\nsalary:{}\ndepartment:{}\n".format(self.name,self.salary,self.department))
    def change_department(self,new_dep):
        self.department=new_dep
class Manager(worker):
    def __init__(self,name,salary,department,num_of_person):
        print("init function of Manager class")
        super().__init__(name,salary,department)###super function usage refers to above functions to get same attributes and add them.
        self.num_of_person=num_of_person
    def give_rise(self,amount_of_rise):
        self.salary+=amount_of_rise

    def Show_Infos(self):
        print("ınformations of manager class:")
        print("name:{}\nsalary:{}\ndepartment:{}\nnum_of_person:{}".format(self.name, self.salary, self.department,
                                                                               self.num_of_person))
manager=Manager("can",120000,"ceo",100)
manager.Show_Infos()