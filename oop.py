class Storybook:
    #class variable
    no_of_books = 0
    discount = 0.5



    def __init__(self,name,writer,price):
        self.name = name
        self.writer = writer
        self.publishingyear = 2020
        self.price = price

        Storybook.no_of_books += 1 #count how many instances

    #regular method
    def book_info(self):
        print(f'Book Name : {self.name}')

    def applyingDiscount(self):
        self.price = self.price - self.price * self.discount






""" #creating instances
book_1= Storybook()


#instance variable (Instance theke make kora)
book_1.name = 'Hamlet'
book_1.writer = 'Joy'

print(book_1.name)

book_2 = Storybook() #automatically calls def init constructor """

book_1 = Storybook('Hamlet','Shakespier',23)#passing using constructor
book_2 = Storybook('lol','Shakes',24)#passing using constructor

book_1.book_info()

#calling by class
Storybook.book_info(book_2)

print(Storybook.no_of_books)

#apply discount
print(book_1.price)
book_2.discount = 0.2 #overiding using self.discount
book_2.applyingDiscount()
print(book_2.price)