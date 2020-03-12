''' MOVIE PROJECT

In this movie project, the user can see all the movies list, add a new movie, retrieve the movie by searching,
and also can quit from the application.

First, the application will prompt the user to enter any one of the above mentioned operations by displaying 
this message:

"Enter 'list' to view all the movies, 'add' to add a new movie, 'search' to retrieve an existing movie and also
'exit' to close the application"

Upon entering, the application will direct the user to the specified operation

'''
movie = []


def menu():
	user_input = input("Enter 'list' to view all the movies, 'add' to add a new movie, 'search' to retrieve an existing movie and also'exit' to close the application: ")
	while user_input!="exit":
		if user_input=="list":
			see_movies(movie)
		elif user_input=="add":
			add_movies()
		elif user_input=="search":
			search_movies(movie)
		elif user_input=='exit':
			print("Closing the application.")
		else:
			print("You have entered wrong operation, please enter the correct one.")
		user_input = input("Enter 'list' to view all the movies, 'add' to add a new movie, 'search' to retrieve an existing movie and also'exit' to close the application: ")

def add_movies():
	name = input("Enter the movie name: ")
	director = input("Enter the move director: ")
	year = int(input("Enter the year of movie release: "))
	movie.append({'name': name, 'director': director, 'year': year})
	


def see_movies(movie):
	for m in movie:
		#print(m)
		print("Name: ", m['name'])
		print("Director: ", m['director'])
		print("Year: ", m['year'])

def search_movies(movie):
	search_list = []
	finding_item = input("From name, director, year of release, how would you like to search your movie: ")
	value_item = input("What is the value of it: ")
	for m in movie:
		if m[finding_item] == value_item:
			search_list.append(m)
			see_movies(search_list)
		else:
			print("You have entered wrong value.")
			
	

menu()



	
