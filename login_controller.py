class LoginController:
    USERS = {
        "1": {"password": "1", "role": "admin"},
        "2": {"password": "2", "role": "waiter"},
        "3": {"password": "3", "role": "waiter"},
        "4": {"password": "4", "role": "waiter"},
    }

    _logged_in_user = None

    @staticmethod
    def is_string_none_or_blank(value):
        return value is None or value.strip() == ""

    @staticmethod
    def login_user(username, password):
        if username in LoginController.USERS and LoginController.USERS[username]["password"] == password:
            LoginController._logged_in_user = {
                "username": username, "role": LoginController.USERS[username]["role"]}
            return True
        else:
            LoginController._logged_in_user = None
            return False

    @staticmethod
    def get_logged_in_user():
        return LoginController._logged_in_user
