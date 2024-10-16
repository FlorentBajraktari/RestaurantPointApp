import kivy
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

# Example implementation of the components in Python using KivyMD

# Login Screen Implementation


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.username = MDTextField(hint_text='Username')
        self.password = MDTextField(hint_text='Password', password=True)
        login_button = MDRaisedButton(text='Login', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        login_button.bind(on_press=self.verify_credentials)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def verify_credentials(self, instance):
        if self.username.text in ['1', '2', '3', '4'] and self.password.text == self.username.text:
            self.manager.current = 'menu_manager'
        else:
            dialog = MDDialog(title='Login Failed',
                              text='Invalid username or password.',
                              size_hint=(0.8, 0.3))
            dialog.open()

# Menu Manager Screen Implementation


class MenuManagerScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuManagerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.menu_list = MDLabel(
            text='Menu Items: \n1. Meal #1 - $3.00\n2. Meal #2 - $6.00\n3. Drink #1 - $2.00', halign='center')
        add_button = MDRaisedButton(text='Add Menu Item', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        update_button = MDRaisedButton(text='Update Menu Item', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        delete_button = MDRaisedButton(text='Delete Menu Item', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        layout.add_widget(self.menu_list)
        layout.add_widget(add_button)
        layout.add_widget(update_button)
        layout.add_widget(delete_button)
        self.add_widget(layout)

# Table Manager Screen Implementation


class TableManagerScreen(Screen):
    def __init__(self, **kwargs):
        super(TableManagerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.table_list = MDLabel(
            text='Tables: \n1. Table #1 - 4 seats\n2. Table #2 - 2 seats\n3. Table #3 - 6 seats', halign='center')
        add_button = MDRaisedButton(text='Add Table', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        update_button = MDRaisedButton(text='Update Table', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        delete_button = MDRaisedButton(text='Delete Table', size_hint=(
            0.5, 0.2), pos_hint={'center_x': 0.5})
        layout.add_widget(self.table_list)
        layout.add_widget(add_button)
        layout.add_widget(update_button)
        layout.add_widget(delete_button)
        self.add_widget(layout)

# Order Status Manager Screen Implementation


class OrderStatusManagerScreen(Screen):
    def __init__(self, **kwargs):
        super(OrderStatusManagerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.order_status_list = MDLabel(
            text='Order Status:\n1. Table #1 - READY\n2. Table #2 - IN PROGRESS', halign='center')
        update_status_button = MDRaisedButton(
            text='Update Status', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        revert_status_button = MDRaisedButton(
            text='Revert Status', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        layout.add_widget(self.order_status_list)
        layout.add_widget(update_status_button)
        layout.add_widget(revert_status_button)
        self.add_widget(layout)

# Main App Manager


class RestaurantPointApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuManagerScreen(name='menu_manager'))
        sm.add_widget(TableManagerScreen(name='table_manager'))
        sm.add_widget(OrderStatusManagerScreen(name='order_status_manager'))
        return sm


# Running the App
if __name__ == '__main__':
    RestaurantPointApp().run()
