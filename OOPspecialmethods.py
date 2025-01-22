class Book():
    def __init__(self,name,writer,page_num,genre):###init method,to define objects
        print("init function of book class")
        self.name=name
        self.writer=writer
        self.page_num=page_num
        self.genre=genre
    def __str__(self):###str methods to print objects
        return "name:{}\nwriter:{}\npage_num:{}\ngenre:{}\n".format(self.name,self.writer,self.page_num,self.genre)
    def __len__(self):###len method to identify length
        return self.page_num
    def __del__(self):###del method to delete
        print("the Book object is deleting...")

book=Book("a tale of two cities","charles dickens",90,"novel")
print(book)
print(len(book))
del(book)
