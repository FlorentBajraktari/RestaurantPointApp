# login_controller.py

class LoginController:
    # Defino përdoruesit dhe fjalëkalimet e tyre në një dictionary
    USERS = {
        "user1": "test123",
        "user2": "test222",
        "user3": "test333",
        "user4": "test444",
    }

    @staticmethod
    def is_string_none_or_blank(value):
        return value is None or value.strip() == ""

    @staticmethod
    def login_user(username, password):
        # Kontrollo nëse kredencialet janë të sakta
        if username in LoginController.USERS and LoginController.USERS[username] == password:
            LoginController._logged_in_user = username
        else:
            LoginController._logged_in_user = None

    @staticmethod
    def get_logged_in_user():
        # Kthe përdoruesin që është regjistruar, ose None nëse login dështon
        return LoginController._logged_in_user

    @staticmethod
    def is_string_none_or_blank(value):
        return value is None or value.strip() == ""

    _logged_in_user = None
