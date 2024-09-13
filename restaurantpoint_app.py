from dataprovider import DataProvider
from enums import TableStatus
from model import Restaurant, MenuItem, Table


class RestaurantPointApp:
    def __init__(self):
        self.data_provider = DataProvider()
        self.restaurants = [Restaurant(**r)
                            for r in self.data_provider.get_restaurants()]
        # Use MenuItem for menu items with price and restaurant_id
        self.menu_items = [MenuItem(**mi)
                           for mi in self.data_provider.get_menu_items()]
        self.tables = [Table(**t, status=TableStatus.AVAILABLE)
                       for t in self.data_provider.get_tables()]

    def display_restaurants(self):
        print("Available Restaurants:")
        for restaurant in self.restaurants:
            print(
                f"ID: {restaurant.id}, Name: {restaurant.name}, Address: {restaurant.address}, Phone: {restaurant.phone}")

    def display_menus(self, restaurant_id):
        print(f"Menu Items for Restaurant ID {restaurant_id}:")

        # Kontrollo të gjitha menu_items përpara filtrimit
        print("All menu items:", self.menu_items)  # Debug print

        # Filtrimi i artikujve të menusë për restorantin e zgjedhur
        filtered_items = [
            item for item in self.menu_items if item.restaurant_id == restaurant_id]

        # Kontrollo nëse ka artikuj të filtruar
        print("Filtered items:", filtered_items)  # Debug print

        if not filtered_items:
            print(f"No menu items available for Restaurant ID {restaurant_id}")
        else:
            for item in filtered_items:
                print(item)

    def display_tables(self, restaurant_id):
        print(f"Tables for Restaurant ID {restaurant_id}:")
        for table in self.tables:
            if table.restaurant_id == restaurant_id:
                print(table)

    def reserve_table(self, restaurant_id):
        print(f"Available tables for Restaurant ID {restaurant_id}:")
        available_tables = [table for table in self.tables if table.restaurant_id ==
                            restaurant_id and table.status == TableStatus.AVAILABLE]

        if not available_tables:
            print("No available tables.")
            return

        for table in available_tables:
            print(
                f"Table ID: {table.id}, Seats: {table.seats}, Status: {table.status.value}")

        table_id = int(input("Enter Table ID to reserve: "))
        for table in available_tables:
            if table.id == table_id:
                table.status = TableStatus.OCCUPIED
                print(f"Table {table_id} has been reserved.")
                return

        print("Invalid Table ID.")

    def run(self):
        self.display_restaurants()
        restaurant_id = int(input("Select a Restaurant ID: "))

        while True:
            print("\nWhat would you like to do?")
            print("1. View Menu")
            print("2. Reserve a Table")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_menus(restaurant_id)
            elif choice == '2':
                self.reserve_table(restaurant_id)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    app = RestaurantPointApp()
    app.run()
