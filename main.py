import sys
import os
import shutil
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QFileDialog, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic
# import the UI and Database connection class
from qt_ui.home_ui import Ui_MainWindow
from qt_ui.theme_ui import Ui_Theme
from database import ConnectDatabase

# Create a main Window class

# # Specify the folder to store the images (your "database")
# IMAGE_DATABASE_FOLDER = "image_database"

# # Create the folder if it doesn't exist
# if not os.path.exists(IMAGE_DATABASE_FOLDER):
#     os.makedirs(IMAGE_DATABASE_FOLDER)
    
class MainWindow(QMainWindow):  
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Initialize the UI properly
        #create a database connection object
        self.db = ConnectDatabase()
        
        # line Edit for add opiration
        self.nameOfCostumer = self.ui.name_customer_line_edit
        self.nameOfBook = self.ui.name_book_line_edit
        self.days = self.ui.days_combobox
        self.type = self.ui.type_combobox
        # button for add opiration
        self.addOpiration = self.ui.add_operation_btn
        
        # Line Edit for Add Book
        self.bookIdLineEdit = self.ui.book_id_lineEdit
        self.bookIdLineEdit.setValidator(QIntValidator())
        self.bookTitleLineEdit = self.ui.book_title_lineEdit
        self.bookAutherLineEdit = self.ui.book_auther_lineEdit
        self.bookPublisherLineEdit = self.ui.book_publisher_lineEdit
        self.bookPriceLineEdit = self.ui.book_price_lineEdit
        self.bookPriceLineEdit.setValidator(QIntValidator())
        self.bookCategoryLineEdit = self.ui.book_category_lineEdit
        self.bookDescriptionLineEdit = self.ui.desc_textEdit
        
        # Buttons for add book
        self.SaveBookBtn = self.ui.save_btn
        self.UpdateBookBtn = self.ui.update_btn
        self.searchBookBtn = self.ui.search_btn
        self.deleteBookBtn = self.ui.delete_btn
        self.clearBookForm = self.ui.clear_btn
        
        # Line Edit for Add User
        self.usernameLineEdit = self.ui.username_lineEdit
        self.nameLineEdit = self.ui.name_lineEdit
        self.emailLineEdit = self.ui.email_lineEdit
        self.passwordLineEdit = self.ui.password_lineEdit
        self.confermPasswordLineEdit = self.ui.conferm_password_lineEdit
        self.userType = self.ui.user_radioButton
        self.adminType = self.ui.admin_radioButton
        
        
        # Buttons for add user
        self.saveUserBtn = self.ui.save_btn_2
        self.updateUserBtn = self.ui.update_btn_2
        self.searchUserBtn = self.ui.search_btn_2
        self.deleteUserBtn = self.ui.delete_btn_2
        
        self.addBtn = self.ui.add_operation_btn
        self.todayTableWidget = self.ui.today_tableWidget
        self.showBooksTableWidget = self.ui.show_books_tableWidget
        self.usersTableWidget = self.ui.users_tableWidget
        self.todayTabWidget = self.ui.today_tabWidget
        self.booksTabWidget = self.ui.books_tabWidget
        self.usersTabWidget = self.ui.users_tabWidget
        self.editBooksTabWidget = self.ui.Edit_book_tabWidget
        self.showBooksTabWidget = self.ui.show_books_tabWidget
        
        # Buttons for the side sections
        self.todayBtn = self.ui.today_tool_btn
        self.booksBtn = self.ui.books_tool_btn
        self.usersBtn = self.ui.users_tool_btn
        self.settingsBtn = self.ui.settings_tool_btn
        self.themeBtn = self.ui.themes_tool_btn 
        
        # Buttons in books section and user section
        self.buttons_add_book_list = self.ui.verticalLayout_11.findChildren(QPushButton)
        self.buttons_add_user_list = self.ui.verticalLayout_19.findChildren(QPushButton)
        
        
        # to hide tab bar from ui
        self.ui.main_tabWidget.tabBar().setVisible(False)
        
        
        self.init_single_slot()
    def init_single_slot(self):
        #connect buttons to their Actions
        # Today section actions
        self.addOpiration.clicked.connect(self.add_opiration)
        self.todayBtn.clicked.connect(self.go_to_today_tab)
        ###### for desibled edit in table widgets
        self.todayTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.set_data_in_today_table()
        # ------------------------------------
        # Books section actions
        self.SaveBookBtn.clicked.connect(self.add_book)
        self.UpdateBookBtn.clicked.connect(self.update_book)
        self.clearBookForm.clicked.connect(self.clear_book_form_info)
        self.deleteBookBtn.clicked.connect(self.delete_book)
        self.booksBtn.clicked.connect(self.go_to_books_tab)
        ###### for desibled edit in table widgets
        self.showBooksTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.set_data_in_show_book_table()
        # # upload images
        # self.upload_image_label = self.ui.upload_image_label
        # self.ui.upload_btn.clicked.connect(self.upload_image)
        # # ----------------------------------------------------------------
        # Users section actions
        self.searchBookBtn.clicked.connect(self.search_info_by_id)
        self.usersBtn.clicked.connect(self.go_to_users_tab)
        self.settingsBtn.clicked.connect(self.go_to_settings_tab)
        self.saveUserBtn.clicked.connect(self.add_user)
        self.searchUserBtn.clicked.connect(self.search_user_by_username)
        self.updateUserBtn.clicked.connect(self.update_user_info)
        self.deleteUserBtn.clicked.connect(self.delete_user)
        self.set_data_in_users_table()
        # for desibled edit in table widgets
        self.usersTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # ----------------------------------------------------------------
        
        self.themeBtn.clicked.connect(self.open_theme_window)
        # self.disable_buttons_admin()
    # Today Section Functions
    def go_to_today_tab(self):
        self.ui.main_tabWidget.setCurrentIndex(0)
    def add_opiration(self):
        opiration_info = self.get_opiration_info()
        if opiration_info["username"] and opiration_info["title"]:
            add_result = self.db.add_opiration(
                username=opiration_info["username"],
                title=opiration_info["title"],
                type=opiration_info["type"],
                days=opiration_info["days"]
            )
            if not add_result:
                    QMessageBox.information(self, "Warning", f"the book named : {opiration_info["title"]} not found", QMessageBox.StandardButton.Yes)
                    self.enable_add_book_buttons()
                    return
                
            QMessageBox.information(self, "Success", f"Opiration added Scussed", QMessageBox.StandardButton.Ok)
            self.enable_add_book_buttons()
            self.clear_opiration_form()
            self.set_data_in_today_table()
        else:
            QMessageBox.information(self, "Error", "All fields are required!", QMessageBox.StandardButton.Yes)
            # self.search_info()
            self.enable_add_book_buttons()
            return
    def clear_opiration_form(self):
        self.nameOfCostumer.clear()
        self.nameOfBook.clear()
        self.type.setCurrentIndex(0)
        self.days.setCurrentIndex(0)
    def set_data_in_today_table(self):
        result = self.db.load_data(fileName=self.db.operation_file)
        self.todayTableWidget.setRowCount(len(result))
        tablerow = 0
        for row in result:
            self.todayTableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row["username"]))
            self.todayTableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(row["id"])))
            self.todayTableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row["title"]))
            self.todayTableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row["auther"]))
            self.todayTableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row["publisher"]))
            self.todayTableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row["category"]))
            self.todayTableWidget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(str(row["price"])))
            self.todayTableWidget.setItem(tablerow,7,QtWidgets.QTableWidgetItem(str(row["type"])))
            self.todayTableWidget.setItem(tablerow,8,QtWidgets.QTableWidgetItem(str(row["days"])))
        
            
            tablerow +=1
    def get_opiration_info(self):
        username = self.nameOfCostumer.text().strip()
        title = self.nameOfBook.text().strip()
        type = self.type.currentText()
        days = self.days.currentText()
        
        opiration_info = {
            "username": username,
            "title": title,
            "type": type,
            "days": days
        }
        return opiration_info
    # ----------------------------------------------------------------
    
    # Books Section Functions
    def go_to_books_tab(self):
        self.ui.main_tabWidget.setCurrentIndex(1)
    def add_book(self):
        self.disable_add_book_buttons()
        book_info = self.get_book_info()
        if book_info["id"] and book_info["title"]:
            check_result = self.check_book_id(book_id=int(book_info["id"]))

            if check_result:
                QMessageBox.information(self, "Error", "Book ID already exists! , Enter new Id", QMessageBox.StandardButton.Yes)
                self.enable_add_book_buttons()
                return
            add_result = self.db.add_book(
                id=int(book_info["id"]),
                title=book_info["title"],
                auther=book_info["auther"],
                publisher=book_info["publisher"],
                price=float(book_info["price"]),
                category=book_info["category"],
                desc=book_info['description']                )
            QMessageBox.information(self, "Success", f"Book added Scussed", QMessageBox.StandardButton.Ok)
            self.enable_add_book_buttons()
            self.clear_book_form_info()
            self.set_data_in_show_book_table()
                
            if add_result:  
                QMessageBox.information(self, "Warning", f"Book added Failll : {add_result} try again", QMessageBox.StandardButton.Yes)
                self.enable_add_book_buttons()
                return
        else:
            QMessageBox.information(self, "Error", "All fields are required!", QMessageBox.StandardButton.Yes)
            # self.search_info()
            self.enable_add_book_buttons()
            return
    def update_book(self):
        # function to update information Book 
        
        new_book_info = self.get_book_info()
        
        if new_book_info["id"]:
            update_result = self.db.update_book(
                id=int(new_book_info["id"]),
                title=new_book_info["title"],
                auther=new_book_info["auther"],
                category=new_book_info["category"],
                publisher=new_book_info["publisher"],
                price=new_book_info["price"],
                description=new_book_info["description"],
            )
            
            if update_result:
                QMessageBox.information(self, "Warning", f"Book updated Failll : {update_result} try again", QMessageBox.StandardButton.Yes)
            else:
                QMessageBox.information(self, "Success", f"Book updated successed", QMessageBox.StandardButton.Yes)
                self.clear_book_form_info()
                self.set_data_in_show_book_table()
                
        else:
            QMessageBox.information(self, "Error", "Book Not selected !", QMessageBox.StandardButton.Yes)
    def clear_book_form_info(self):
       # function for clearing the form
       self.bookIdLineEdit.clear()
       self.bookAutherLineEdit.clear()
       self.bookPublisherLineEdit.clear()
       self.bookPriceLineEdit.clear()
       self.bookCategoryLineEdit.clear()
       self.bookDescriptionLineEdit.clear()
       self.bookTitleLineEdit.clear()
    def set_data_in_show_book_table(self):
        result = self.db.load_data(fileName=self.db.book_file)
        self.showBooksTableWidget.setRowCount(len(result))
        tablerow = 0
        for row in result:
            self.showBooksTableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row["id"])))
            self.showBooksTableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row["title"]))
            self.showBooksTableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row["auther"]))
            self.showBooksTableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row["publisher"]))
            self.showBooksTableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row["category"]))
            self.showBooksTableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row["price"])))
            tablerow +=1
    def delete_book(self):
        # function for delete book information from table
        checkLineEdit = self.checkLineEdit(lineEdit=self.bookIdLineEdit)
        if checkLineEdit:
            select_option = QMessageBox.warning(self, "Warning", "Are you sure to delete it?", 
                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            
            if select_option == QMessageBox.StandardButton.Ok:
                book_id = int(self.bookIdLineEdit.text().strip())
                delete_result = self.db.delete_book(id=book_id)
                if not delete_result:
                    QMessageBox.information(self, "Success", f"Book deleted successfully", QMessageBox.StandardButton.Ok)
                    self.clear_book_form_info()
                    self.set_data_in_show_book_table()
                else:
                    QMessageBox.information(self, "Warning", f"Book deleted Failll : {delete_result} try again", QMessageBox.StandardButton.Ok)
    def disable_add_book_buttons(self):
        for button in self.buttons_add_book_list:
            button.setDisabled(True)
    def enable_add_book_buttons(self):
        for button in self.buttons_add_book_list:
            button.setDisabled(False)
    def get_book_info(self):
        # function to retrive book information from the form
        book_id = self.bookIdLineEdit.text().strip()
        title = self.bookTitleLineEdit.text().strip()
        auther = self.bookAutherLineEdit.text().strip()
        publisher = self.bookPublisherLineEdit.text().strip()
        price = self.bookPriceLineEdit.text().strip()
        category = self.bookCategoryLineEdit.text().strip()
        desc = self.bookDescriptionLineEdit.toPlainText().strip()
        
        book_info = {
            "id": book_id,
            "title": title,
            "auther": auther,
            "publisher": publisher,
            "price": price,
            "category": category,
            "description" : desc
        }
        return book_info
    def check_book_id(self, book_id):
        # function to check if a Book id already exists
        result = self.db.search_book_info(book_id=book_id)
        return result
    def set_book_data_in_line_edit(self, book_reslut):
        if book_reslut:
            self.bookIdLineEdit.setText(str(book_reslut[0]['id']))
            self.bookTitleLineEdit.setText(book_reslut[0]['title'])
            self.bookAutherLineEdit.setText(book_reslut[0]['auther'])
            self.bookPublisherLineEdit.setText(book_reslut[0]['publisher'])
            self.bookPriceLineEdit.setText(str(book_reslut[0]['price']))
            self.bookCategoryLineEdit.setText(book_reslut[0]['category'])
            self.bookDescriptionLineEdit.setText(book_reslut[0]['description'])
        else:
            QMessageBox.information(self, "Not Found", "Book ID not exists!", QMessageBox.StandardButton.Yes)
            self.set_data_in_today_table()
    # ----------------------------------------------------------------
    
    # Users Section Functions
    def go_to_users_tab(self):
        self.ui.main_tabWidget.setCurrentIndex(2)
    def search_user_by_username(self):
        try:
            username = self.usernameLineEdit.text().strip()
            user = self.db.search_user_info(username=username)
            self.set_user_data_in_line_edit(user_result=user)
        except Exception as er:
            print(f" Error in search info by id function : {er}")
            QMessageBox.information(self, "Warning", f"Please Entur the username", QMessageBox.StandardButton.Yes)
    def clear_user_form_info(self):
        self.usernameLineEdit.clear()
        self.nameLineEdit.clear()
        self.emailLineEdit.clear()
        self.passwordLineEdit.clear()
        self.confermPasswordLineEdit.clear()
    def set_data_in_users_table(self):
        result = self.db.load_data(fileName=self.db.users_file)
        self.usersTableWidget.setRowCount(len(result))
        tablerow = 0
        for row in result:
            self.usersTableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row["username"])))
            self.usersTableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row["name"]))
            self.usersTableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row["email"]))
            tablerow +=1
    def add_user(self):
        self.disable_add_user_buttons()
        user_info = self.get_user_info()
        if user_info["username"] and user_info["name"] and user_info["email"] and user_info["password"]:
            if user_info["password"] != user_info["conferm_password"]:
                QMessageBox.information(self, "Warning", f"Password Not Match", QMessageBox.StandardButton.Yes)
                self.enable_add_user_buttons()
                return
            check_username = self.check_username(username=user_info["username"])
            type = self.check_radio_option_selected()
            if check_username:
                QMessageBox.information(self, "Error", "username already exists! , Enter new username", QMessageBox.StandardButton.Yes)
                self.enable_add_user_buttons()
                return
            add_result = self.db.add_user(
                username=user_info["username"],
                name=user_info["name"],
                email=user_info["email"],
                password=user_info["password"],
                type=type
                )
            QMessageBox.information(self, "Success", f"User added Scussed", QMessageBox.StandardButton.Ok)
            self.enable_add_user_buttons()
            self.clear_user_form_info()
            self.set_data_in_users_table()
                
            if add_result:  
                QMessageBox.information(self, "Warning", f"User added Failll : {add_result} try again", QMessageBox.StandardButton.Yes)
                self.enable_add_user_buttons()
                return
        else:
            QMessageBox.information(self, "Error", "All fields are required!", QMessageBox.StandardButton.Yes)
            # self.search_info()
            self.enable_add_user_buttons()
            return
    def update_user_info(self):
        # function to update information Book 
        
        new_user_info = self.get_user_info()
        
        if new_user_info["username"]:
            update_result = self.db.update_user(
                username=new_user_info["username"],
                name=new_user_info["name"],
                email=new_user_info["email"],
                password=new_user_info["password"],
            )
            
            if update_result:
                QMessageBox.information(self, "Warning", f"User updated Failll : {update_result} try again", QMessageBox.StandardButton.Yes)
            else:
                QMessageBox.information(self, "Success", f"User updated successed", QMessageBox.StandardButton.Yes)
                self.clear_book_form_info()
                self.set_data_in_users_table()
                
        else:
            QMessageBox.information(self, "Error", "User Not selected !", QMessageBox.StandardButton.Yes)
    def delete_user(self):
        # function for delete book information from table
        checkLineEdit = self.checkLineEdit(lineEdit=self.usernameLineEdit)
        if checkLineEdit:
            select_option = QMessageBox.warning(self, "Warning", "Are you sure to delete it?", 
                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            
            if select_option == QMessageBox.StandardButton.Ok:
                username = self.usernameLineEdit.text().strip()
                delete_result = self.db.delete_user(username=username)
                if not delete_result:
                    QMessageBox.information(self, "Success", f"username deleted successfully", QMessageBox.StandardButton.Ok)
                    self.clear_user_form_info()
                    self.set_data_in_users_table()
                else:
                    QMessageBox.information(self, "Warning", f"username deleted Failll : {delete_result} try again", QMessageBox.StandardButton.Ok)            
    def disable_add_user_buttons(self):
        for button in self.buttons_add_user_list:
            button.setDisabled(True)
    def enable_add_user_buttons(self):
        for button in self.buttons_add_user_list:
            button.setDisabled(False)
    def check_username(self, username):
        # function to check if a Book username already exists
        result = self.db.search_user_info(username=username)
        return result
    def set_user_data_in_line_edit(self, user_result):
        if user_result:
            self.usernameLineEdit.setText(user_result['username'])
            self.nameLineEdit.setText(user_result['name'])
            self.emailLineEdit.setText(user_result['email'])
            self.passwordLineEdit.setText(user_result['password'])
        else:
            QMessageBox.information(self, "Not Found", "Username not exists!", QMessageBox.StandardButton.Yes)
            self.set_data_in_users_table()
    def get_user_info(self):
        # function to retrive user information from the form
        username = self.usernameLineEdit.text().strip()
        name = self.nameLineEdit.text().strip()
        email = self.emailLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()
        conferm_password = self.confermPasswordLineEdit.text().strip()
        
        user_info = {
            "username": username,
            "name": name,
            "email": email,
            "password": password,
            "conferm_password" : conferm_password
        }
        return user_info
    # ----------------------------------------------------------------
    
    # Helpers Functions --------------------------------
    def go_to_settings_tab(self):
        self.ui.main_tabWidget.setCurrentIndex(3)
    def search_info_by_id(self):
        try:
            book_id = int(self.bookIdLineEdit.text().strip())
            book = self.db.search_book_info(book_id=book_id)
            self.set_book_data_in_line_edit(book_reslut=book)
        except Exception as er:
            print(f" Error in search info by id function : {er}")
            QMessageBox.information(self, "Warning", f"Please Entur the id for book ", QMessageBox.StandardButton.Yes)
            # self.set_data_in_today_table()
    def upload_image(self):
        # Open a file dialog to select an image file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                   "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)",
                                                   options=options)
        if file_path:
            # Get the file name and copy it to the "image database" folder
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(IMAGE_DATABASE_FOLDER, file_name)
            
            # Copy the file to te image database folder
            shutil.copy(file_path, destination_path)

            # Update the label to confirm the image was uploaded
            self.upload_image_label.setText(f"Image uploaded: {file_name}")
            self.imagePath = destination_path
            print(f"Image '{file_name}' has been copied to '{IMAGE_DATABASE_FOLDER}'")
    def checkLineEdit(self,lineEdit):
        if not lineEdit.text().strip():
            QMessageBox.information(self, "Error", f"{lineEdit.objectName()} field is required!", QMessageBox.StandardButton.Ok)
            return False
        return True
    def disable_buttons_admin(self):
        self.UpdateBookBtn.setDisabled(True)
        self.deleteBookBtn.setDisabled(True)
        self.updateUserBtn.setDisabled(True)
        self.deleteUserBtn.setDisabled(True)
    def check_radio_option_selected(self):
        if self.userType.isChecked():
            return "user"
        elif self.adminType.isChecked():
            return "admin"
    def open_theme_window(self):
        self.theme_window = uic.loadUi("qt_ui/theme_ui.ui", QWidget())
        self.theme_window.show()
    # ----------------------------------------------------------------
# Application Entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
 