import database

user_choice = """
Enter:
-- 'a' to add a new book
-- 'l' to list all books
-- 'r' to mark a book as read
-- 'd' to delete a book
-- 'q' to quit

Your choice: """

def menu():
	user_input = input(user_choice)
	while user_input != 'q':
		if user_input == 'a':
			prompt_add_book()	
		elif user_input == 'l':
			list_books() 
		elif user_input == 'r':
			prompt_read_book()  
		elif user_input == 'd':
			propmt_delete_book()
		else:
			print("Unknown command. Please try again.")

	user_input = input(user_choice)


# A function that asks the user for the name and author of the new book
def prompt_add_book():
	name = input("Enter the neww book name: ")
	author = input("Enter the new book author: ")

	database.add_book(name, author)


# A function that shows a list of the books in oyur list
def list_books():
	books = database.get_all_books()
	for book in books:
		#read = 'Yes' if book['read'] else 'No'
		read = 'Yes' if book['read']=='1' else 'No'
		print(f"{book['name']} by {book['author']}, read: {book['read']}")


# A function that asks the user for book name and changes it to 'read' in our list
def prompt_read_book():
	name = input("Enter the name of the book you just finished reading: ")

	database.mark_book_as_read(name)


# A function that ask the user for the name of the book and removes the book from the list
def prompt_delete_book():
	name = input("Enter the name of the book you want to delete: ")

	database.delete_book(name)




#Main Program
menu()
