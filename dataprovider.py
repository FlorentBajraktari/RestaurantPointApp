from model import User


class DataProvider:
    def __init__(self):
        self.restaurants = self._create_restaurant_list()
        self.menu_items = self._create_menu_items()
        self.tables = self._create_table_list()
        self.users = self._create_user_list()  # Shtojmë përdoruesit

    def _create_restaurant_list(self):
        return [
            {'id': 1, 'name': 'Hyneshat Restaurant',
                'address': 'Nena Terez', 'phone': '+383111222'},
            {'id': 2, 'name': 'Hyneshat Restaurant',
                'address': 'Address 2', 'phone': '+383222333'},
            {'id': 3, 'name': 'Hyneshat Restaurant',
                'address': 'Address 3', 'phone': '+383333444'},
        ]

    def _create_menu_items(self):
        return [
            {'id': 1, 'restaurant_id': 1, 'name': 'Pizza Margherita', 'price': 5.00},
            {'id': 2, 'restaurant_id': 1, 'name': 'Pizza Pepperoni', 'price': 6.50},
            {'id': 3, 'restaurant_id': 1, 'name': 'Coca-Cola', 'price': 1.50},
            {'id': 4, 'restaurant_id': 2, 'name': 'Pizza Margherita', 'price': 5.00},
            {'id': 5, 'restaurant_id': 2, 'name': 'Fanta', 'price': 1.50},
            {'id': 6, 'restaurant_id': 3,
                'name': 'Pizza Quattro Stagioni', 'price': 7.00},
            {'id': 7, 'restaurant_id': 3, 'name': 'Water', 'price': 1.00},
        ]

    def _create_table_list(self):
        return [
            {'id': 1, 'restaurant_id': 1, 'seats': 4},
            {'id': 2, 'restaurant_id': 1, 'seats': 2},
            {'id': 3, 'restaurant_id': 2, 'seats': 6},
            {'id': 4, 'restaurant_id': 2, 'seats': 4},
            {'id': 5, 'restaurant_id': 3, 'seats': 8},
        ]

    def _create_user_list(self):
        # Shtojmë disa përdorues për testim
        return [
            User(username="admin", password="admin123", role="admin"),
            User(username="waiter1", password="waiter123", role="waiter"),
            User(username="waiter2", password="waiter123", role="waiter")
        ]

    def get_restaurants(self):
        return self.restaurants

    def get_menu_items(self):
        return self.menu_items

    def get_tables(self):
        return self.tables

    def get_users(self):
        return self.users  # Kthejmë listën e përdoruesve
