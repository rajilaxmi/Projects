# Concerned with storing and retrieving books from a csv file.

books_file = 'books.txt'
#books = []

def add_book(name, author):
	with open('books.txt', 'a') as file
	file.write(f'{name},{author},0\n')

	''' 
	books.append({
		'name' : name,
		'author' : author,
		'read' : False
		})'''


def get_all_books():
	with open(books_file, 'r') as file:
		lines = [line.strip().split(',') for line in file.readlines()]
	
	#books = 
	return [ 
		{'name': line[0], 'author' : line[1], 'read' : line[2]}
		for line in lines
		]
	#return books


def mark_book_as_read(name):
	books = get_all_books()
	for book in books:
		if book['name'] == name:
			book['read'] = '1'
	_save_all_books(books)
	'''for book in books:
		if book['name'] == name:
			book['read'] = True'''

def _save_all_books(books):
	with open(books_file.txt, 'w') as file:
		for book in books:
			file.write(f"{book['name']}, {book['author']},{book['read']}\n")


def delete_book(name):
	books = get_all_books()
	books = [book for book in books if book['name'] != name]
	_save_all_books(books) 

	'''global books
	books = [book for book in books if book['name'] != name] # add each book to new list of book['name'] != name'''
	