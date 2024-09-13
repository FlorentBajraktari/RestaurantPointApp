class Restaurant:
    def __init__(self, id, name, address, phone):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return f"Restaurant(ID: {self.id}, Name: {self.name}, Address: {self.address}, Phone: {self.phone})"


class MenuItem:
    def __init__(self, id, restaurant_id, name, price):
        self.id = id
        self.restaurant_id = restaurant_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"MenuItem(ID: {self.id}, Restaurant ID: {self.restaurant_id}, Name: {self.name}, Price: {self.price})"


class Table:
    def __init__(self, id, restaurant_id, seats, status):
        self.id = id
        self.restaurant_id = restaurant_id
        self.seats = seats
        self.status = status

    def __repr__(self):
        return f"Table(ID: {self.id}, Restaurant ID: {self.restaurant_id}, Seats: {self.seats}, Status: {self.status})"


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Role mund të jetë 'admin', 'waiter', etj.

    def __repr__(self):
        return f"User(username: {self.username}, role: {self.role})"

    def check_password(self, password):
        return self.password == password
