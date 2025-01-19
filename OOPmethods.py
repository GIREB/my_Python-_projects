###We defined methods we can use in class struct that we built.Those can provide to give ability to change and manipulate the class struct we built.
###We assigned the objects to themselves using self reference and then defined the methods.
###We used format to send values we want into objects in Show_Infos  then we manipulated the way we want to form

class Software_Developer():
    def __init__(self,name,surname,number,salary,languages):
        self.name=name
        self.surname=surname
        self.number=number
        self.salary=salary
        self.languages=languages
    def Show_Infos(self):
        print("""
        features of Software_Developer object
        name:{}
        surname:{}
        number:{}
        salary:{}
        languages:{}
        """.format(self.name,self.surname,self.number,self.salary,self.languages))
    def Give_Raise(self,amountofraise):
        print("giving raise...")
        self.salary+=amountofraise
    def Add_Language(self,new_lang):
        print("adding new languages...")
        self.languages.append(new_lang)
developer=Software_Developer("CAN","CETIN",1453,50000,["PYTHON","C","C++"])
developer.Show_Infos()
developer.Add_Language("french")
developer.Show_Infos()
developer.Give_Raise(30000)
developer.Show_Infos()
