from login_controller import LoginController


def test_login():
    controller = LoginController()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    controller.login(username, password)


if __name__ == "__main__":
    test_login()
