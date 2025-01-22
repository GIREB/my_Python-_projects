class countries():
    def __init__(self,Türkiye,England,USA,China,Russia):
        self.Türkiye=Türkiye
        self.England=England
        self.USA=USA
        self.China=China
        self.Russia=Russia
    def object(self):###abstract method provides abstraction from your inheritance class
        pass
class cities(countries):
    def __init__(self,city,Türkiye,England,USA,China,Russia):
        super().__init__(Türkiye,England,USA,China,Russia)
        self.city=city
    def object(self):
        return self.city**2

my_city=cities(5,"istanbul","London","New York","Hong Kong","Moscow")
print(my_city.object())
