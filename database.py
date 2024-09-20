import json
import os

class ConnectDatabase:
    def __init__(self, book_file='./data/books.json' , operation_file='./data/opirations.json',users_file='./data/users.json'):
        self.book_file = book_file
        self.operation_file = operation_file
        self.users_file = users_file
        self.load_data(self.book_file)
        self.load_data(self.operation_file)
        self.load_data(self.users_file)
    # Functions helper
    def load_data(self,fileName):
        """Load data from JSON file into memory."""
        if os.path.exists(fileName):
            with open(fileName, 'r') as file:
                self.data = json.load(file)
                return self.data
        else:
            self.data = []
            return self.data
    def save_data(self,file):
        """Save data from memory to JSON file."""
        with open(file, 'w') as file:
            json.dump(self.data, file, indent=4)
    # ----------------------------------------------------------------
    
    # Functions for book
    def add_book(self, id, title, desc, price, auther, publisher,category):
        """Add new book to JSON file."""
        self.load_data(self.book_file)
        new_book = {
            "id": id,
            "title": title,
            "description": desc,
            "price": price,
            "auther": auther,
            "publisher": publisher,
            "category" : category,
        }
        self.data.append(new_book)
        self.save_data(self.book_file)
    def update_book(self, id,title, auther, publisher, price, category,description):
        """Update Book info in JSON file."""
        self.load_data(fileName=self.book_file)
        for book in self.data:
            if book['id'] == id:
                book.update({
                    'title': title,
                    'auther': auther,
                    'publisher': publisher,
                    'price': price,
                    'category': category,
                    'description': description
                })
                self.save_data(file=self.book_file)
                return
    def delete_book(self, id):
        """Delete Book info from JSON file."""
        self.load_data(fileName=self.book_file)
        
        # check if data is loaded or not
        if not hasattr(self, 'data') or self.data is None:
            print("No data loaded or 'data' attribute not found.")
            return
        
        found = False
        
        for book in self.data:
            if book["id"] == id:
                self.data.remove(book)
                found = True
                break
            
        if not found:
            print(f"book ID {id} not found.")
            return
        try:
            self.save_data(file=self.book_file)
            print(f"Book ID {id} successfully deleted.")
        except Exception as e:
            print(f"Error saving data: {e}")
    def search_book_info(self, book_id=None,title=None, auther=None, publisher=None, price=None, desciption=None):
        """Search for Book info."""
        self.load_data(fileName=self.book_file)
        result = []
        for book in self.data:
            if book_id == book["id"]:
                result.append(book)
                return result
    # ----------------------------------------------------------------
    
    # Functions for operation
    def add_opiration(self,username, title, type, days):
        """Add new book to JSON file."""
        self.load_data(self.book_file)
        for book in self.data:
            if book['title'] == title:
                self.load_data(self.operation_file)
                new_operation = {
                    "username": username,
                    "type": type,
                    "days": days,
                    "id": book['id'],
                    "title": title,
                    "description": book["description"],
                    "price": book["price"],
                    "auther": book["auther"],
                    "publisher": book["publisher"],
                    "category" : book["category"],
                }
                self.data.append(new_operation)
                self.save_data(self.operation_file)
                return new_operation
        print(f"Book '{title}' not found.")
        return False
    # ----------------------------------------------------------------
    
    # Functions for user
    def save_current_user(self,user):
        print(f"current user info {user}")
        return user 
    def add_user(self,username,name,email,password,type="user"):
        """Add new user to JSON file."""
        self.load_data(self.users_file)
        new_user = {
            "username": username,
            "name": name,
            "email": email,
            "password": password,
            "type" : type
        }
        self.data.append(new_user)
        self.save_data(self.users_file)
    def delete_user(self, username):
        """Delete user info from JSON file."""
        self.load_data(fileName=self.users_file)
        
        # check if data is loaded or not
        if not hasattr(self, 'data') or self.data is None:
            print("No data loaded or 'data' attribute not found.")
            return
        
        found = False
        
        for user in self.data:
            if user["username"] == username:
                self.data.remove(user)
                found = True
                break
            
        if not found:
            print(f"username {username} not found.")
            return
        try:
            self.save_data(file=self.users_file)
            print(f"username {username} successfully deleted.")
        except Exception as e:
            print(f"Error saving data: {e}")
    def update_user(self, username,name,email,password):
        """Update User info in JSON file."""
        self.load_data(fileName=self.users_file)
        for user in self.data:
            if user['username'] == username:
                user.update({
                    'username': username,
                    'name': name,
                    'email': email,
                    'password': password,
                })
                self.save_data(file=self.users_file)
                return
    # ----------------------------------------------------------------