class Book:
    page_material = "Paper"
    text_language = "English"
    is_reserved = False

    def __init__(self, book_name, author, pages_count, isbn):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn

    def reserve_book(self):
        self.is_reserved = not self.is_reserved

    def show_info(self):
        text = ("Name: " + self.book_name + ", Author: " + self.author +
                ", Pages: " + str(self.pages_count) + ", Material: " + self.page_material)
        if self.is_reserved:
            text += ", reserved"
        print(text)


class SchoolBook(Book):
    def __init__(self, book_name, author, pages_count, isbn, discipline, class_number, is_task_exist):
        super().__init__(book_name, author, pages_count, isbn)
        self.discipline = discipline
        self.class_number = class_number
        self.is_task_exist = is_task_exist

    def show_info(self):
        text = ("Name: " + self.book_name + ", Author: " + self.author +
                ", Pages: " + str(self.pages_count) + ", Discipline: " + self.discipline +
                ", Class: " + str(self.class_number))
        if self.is_reserved:
            text += ", reserved"
        print(text)


book1 = Book("To Kill a Mockingbird", "Harper Lee", 200, "999-9-99-111111-1")
book2 = Book("1984", "George Orwell", 300, "999-9-99-111111-2")
book3 = Book("Moby Dick", "Herman Melville", 400, "999-9-99-111111-3")
book4 = Book("Pride and Prejudice", "Jane Austen", 500, "999-9-99-111111-4")
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 600, "999-9-99-111111-5")

book2.reserve_book()

books = [book1, book2, book3, book4, book5]
for book in books:
    book.show_info()

textbook1 = SchoolBook("Mathematics", "John Doe",
                       320, "999-9-99-222222-1", "Mathematics",
                       8, True)
textbook2 = SchoolBook("Biology", "Alice Johnson",
                       280, "999-9-99-222222-2", "Biology",
                       10, False)
textbook3 = SchoolBook("English", "Michael Brown",
                       250, "999-9-99-222222-3", "English",
                       7, True)
textbook4 = SchoolBook("History", "Emma Clark",
                       400, "999-9-99-222222-4", "History",
                       9, False)
textbook5 = SchoolBook("Physics", "James Wilson",
                       350, "999-9-99-222222-5", "Physics",
                       11, True)


textbook4.reserve_book()
textbooks = [textbook1, textbook2, textbook3, textbook4, textbook5]
for book in textbooks:
    book.show_info()
