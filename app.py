import json
import os

file_data = 'library.txt'

def load_library():
    if os.path.exists(file_data):
        with open(file_data , 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(file_data , 'w') as file:
        json.dump (library, file)

# =========== Adding book defination


def add_book(library):
    book = {
       'title' : input('Enter title:'),
       'author' : input('Enter the author name:'),
        'year' : input('Enter the year:'),
        'genere' : input('Enter the genere:'),
        'is_read' : input('Have you read this book? (yes/ no):'),
    }
    library.append(book)
    save_library(library)
    print(f'{book["title"]} added successfully.......')
    
# =========== Removing book defination

def remove_book(library):
    remove = input('Enter the title to remove book:').lower()
    for book in library[:]:
      if book['title'].lower() == remove:
         library.remove(book)
         save_library(library)
         print(f'{book['title']} removed successfully')
         return
    print('Title does not match.')

# =========== Searching book defination

def search_book(library):
   search = input('Enter the book title:')
   for book in library:
      if book['title'].lower() == search:
         print(book)
         return
   print('No match found')

# =========== List book defination

def list_book(library):
   if library == []:
      print('No books found')
      return
   print("\nList of Books in Your Library:")  # Header for the list
   for index, book in enumerate(library, start=1):  # Enumerate to display numbered list
        print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, "
              f"Genre: {book['genere']}, Read: {'Yes' if book['is_read'] else 'No'}")
   



# =========== Print book defination in cli

def show():
   library = load_library()
   while True :
    print('Library mangement system')
    print('1: Add book')
    print('2: Remove book')
    print('3: Search book')
    print('4: List of book')
    print('5: Exit')
   
    choice = input('Select an operation:')
    if choice == '1':
      add_book(library)
    elif choice == '2':
      remove_book(library)
    elif choice == '3':
      search_book(library)
    elif choice == '4':
      list_book(library)
    elif choice == '5':
      print('Exit')
      break

if __name__ == '__main__':
   show()
      

