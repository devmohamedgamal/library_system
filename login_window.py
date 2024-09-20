import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QMessageBox
from PyQt5.uic import loadUi

from qt_ui.login_ui import Ui_login
from main import MainWindow
from database import ConnectDatabase

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.db = ConnectDatabase()
        # Connect the login button
        self.ui.login_btn.clicked.connect(self.handle_login)
        self.ui.sign_up_btn.clicked.connect(self.handle_sign_up)
        self.ui.login_tab.clicked.connect(self.go_to_login_tab)
        self.ui.sign_up_tab.clicked.connect(self.go_to_sign_up_tab)
        # to hide tab bar from ui
        self.ui.tabWidget.tabBar().setVisible(False)

    def handle_login(self):
        username = self.ui.login_user_name.text()
        password = self.ui.login_password.text()
        
        self.login(username, password)
    def go_to_login_tab(self):
        self.ui.tabWidget.setCurrentIndex(0)
    def go_to_sign_up_tab(self):
        self.ui.tabWidget.setCurrentIndex(1)
    def login(self, username, password):
        self.db.load_data(fileName=self.db.users_file)
        for user in self.db.data:
            if user['username'] == username and user['password'] == password:
                self.open_main_window()
                return
        QMessageBox.information(self, "Error", "Username or password is incorect", QMessageBox.StandardButton.Ok)
    def handle_sign_up(self):
        username = self.ui.sign_up_user_name.text()
        name = self.ui.sign_up_name.text()
        email = self.ui.sign_up_address.text()
        password = self.ui.sign_up_password.text()
        
        self.sign_up(username,name,email, password)
    def sign_up(self, username,name,email, password):
        self.db.load_data(fileName=self.db.users_file)
        
        self.ui.sign_up_btn.setDisabled(True)
        user_info = {
            "username": username,
            "name": name,
            "email": email,
            "password": password,
            "type" : "user"
        }
        if user_info["username"] and user_info["name"] and user_info["email"] and user_info["password"]:
            check_username = self.check_username(username=user_info["username"])
            if check_username:
                QMessageBox.information(self, "Error", "username already exists! , Enter new username", QMessageBox.StandardButton.Yes)
                self.ui.sign_up_btn.setDisabled(False)
                return
            add_result = self.db.add_user(
                username=user_info["username"],
                name=user_info["name"],
                email=user_info["email"],
                password=user_info["password"]
                )
            QMessageBox.information(self, "Success", f"Sign up Scussed", QMessageBox.StandardButton.Ok)
            self.ui.sign_up_btn.setDisabled(False)
            self.open_main_window()
            if add_result:  
                QMessageBox.information(self, "Warning", f"User added Failll : {add_result} try again", QMessageBox.StandardButton.Yes)
                self.ui.sign_up_btn.setDisabled(False)

                return
        else:
            QMessageBox.information(self, "Error", "All fields are required!", QMessageBox.StandardButton.Yes)
            self.ui.sign_up_btn.setDisabled(False)
            return                   # Close the login window
    def check_username(self, username):
        # function to check if a student username already exists
        result = self.db.search_user_info(username=username)
        return result

    def open_main_window(self):
        self.main_window = MainWindow()  # Create the main window
        self.main_window.show()          # Show the main window
        self.close()                     # Close the login window

# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Start with the login window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())
