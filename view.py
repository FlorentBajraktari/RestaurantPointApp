from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(
            None, None), width='300dp', height='400dp', pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.username = MDTextField(
            hint_text='Username',
            size_hint_x=None,
            width='280dp'
        )

        self.password = MDTextField(
            hint_text='Password',
            password=True,
            size_hint_x=None,
            width='280dp',
            icon_right='eye-off'
        )
        self.password.bind(on_icon_right=lambda instance,
                           value: self.toggle_password_visibility())

        self.login_button = MDRaisedButton(
            text='Login',
            size_hint=(None, None),
            width='100dp',
            height='40dp',
            pos_hint={'center_x': 0.5}
        )
        self.login_button.bind(on_press=self.verify_credentials)

        self.layout.add_widget(self.username)
        self.layout.add_widget(self.password)
        self.layout.add_widget(self.login_button)

        self.add_widget(self.layout)

    def toggle_password_visibility(self):
        if self.password.password:
            self.password.password = False
            self.password.icon_right = 'eye'
        else:
            self.password.password = True
            self.password.icon_right = 'eye-off'

    def verify_credentials(self, instance):
        if self.username.text in ['1', '2', '3', '4'] and self.password.text == self.username.text:
            self.manager.current = 'management_panel'
        else:
            dialog = MDDialog(title='Login Failed',
                              text='Invalid username or password.',
                              size_hint=(0.8, 0.3))
            dialog.open()


class ManagementPanelScreen(Screen):
    def __init__(self, **kwargs):
        super(ManagementPanelScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=2, spacing=10)

        nav_panel = GridLayout(
            cols=1, padding=10, spacing=10, size_hint=(0.2, 1))
        nav_buttons = [
            ('Menu Manager', 'menu_manager'),
            ('Table Manager', 'table_manager'),
            ('Order Status Manager', 'order_status_manager'),
            ('Sign out', 'login')
        ]
        for btn_text, screen_name in nav_buttons:
            btn = MDRaisedButton(text=btn_text, size_hint=(
                1, None), height=50, md_bg_color=(0, 0.5, 0.4, 1))
            btn.bind(on_press=lambda instance,
                     sn=screen_name: self.switch_content(sn))
            nav_panel.add_widget(btn)

        self.content_panel = BoxLayout(
            orientation='vertical', padding=20, spacing=10)
        self.content_panel.add_widget(
            MDLabel(text='Content Pane', halign='center'))

        layout.add_widget(nav_panel)
        layout.add_widget(self.content_panel)
        self.add_widget(layout)

    def switch_content(self, screen_name):
        self.content_panel.clear_widgets()
        if screen_name == 'menu_manager':
            self.content_panel.add_widget(
                MenuManagerContent().create_content_panel())
        elif screen_name == 'table_manager':
            self.content_panel.add_widget(
                TableManagerContent().create_content_panel())
        elif screen_name == 'order_status_manager':
            self.content_panel.add_widget(
                OrderStatusManagerContent().create_content_panel())
        elif screen_name == 'login':
            self.manager.current = 'login'


class MenuManagerContent:
    def __init__(self):
        self.menu_list = [{'name': 'Meal #1', 'price': '$3.00'},
                          {'name': 'Meal #2', 'price': '$6.00'},
                          {'name': 'Drink #3', 'price': '$2.00'}]

    def create_content_panel(self):
        panel = GridLayout(cols=1, padding=20, spacing=10)

        self.menu_table = self.create_menu_table()
        panel.add_widget(self.menu_table)

        button_panel = GridLayout(cols=3, spacing=10)
        add_button = MDRaisedButton(
            text='Add Menu Item', on_press=self.add_menu_item)
        update_button = MDRaisedButton(
            text='Update Menu Item', on_press=self.update_menu_item)
        delete_button = MDRaisedButton(
            text='Delete Menu Item', on_press=self.delete_menu_item)

        button_panel.add_widget(add_button)
        button_panel.add_widget(update_button)
        button_panel.add_widget(delete_button)
        panel.add_widget(button_panel)

        return panel

    def create_menu_table(self):
        table_row_data = [(menu_item['name'], menu_item['price'])
                          for menu_item in self.menu_list]

        return MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Price", dp(40)),
            ],
            row_data=table_row_data
        )

    def refresh_menu_table(self):
        self.menu_table.row_data = [(menu_item['name'], menu_item['price'])
                                    for menu_item in self.menu_list]

    def add_menu_item(self, instance):
        popup = Popup(
            title='Add Menu Item',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Add Menu Item functionality")
        )
        popup.open()

    def update_menu_item(self, instance):
        popup = Popup(
            title='Update Menu Item',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Update Menu Item functionality")
        )
        popup.open()

    def delete_menu_item(self, instance):
        popup = Popup(
            title='Delete Menu Item',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Delete Menu Item functionality")
        )
        popup.open()


class TableManagerContent:
    def __init__(self):
        self.table_list = [{'number': 'Table #1', 'seats': '4 seats'},
                           {'number': 'Table #2', 'seats': '2 seats'},
                           {'number': 'Table #3', 'seats': '6 seats'}]

    def create_content_panel(self):
        panel = GridLayout(cols=1, padding=20, spacing=10)

        self.table_table = self.create_table_table()
        panel.add_widget(self.table_table)

        button_panel = GridLayout(cols=3, spacing=10)
        add_button = MDRaisedButton(text='Add Table', on_press=self.add_table)
        update_button = MDRaisedButton(
            text='Update Table', on_press=self.update_table)
        delete_button = MDRaisedButton(
            text='Delete Table', on_press=self.delete_table)

        button_panel.add_widget(add_button)
        button_panel.add_widget(update_button)
        button_panel.add_widget(delete_button)
        panel.add_widget(button_panel)

        return panel

    def create_table_table(self):
        table_row_data = [(table_item['number'], table_item['seats'])
                          for table_item in self.table_list]

        return MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Table Number", dp(40)),
                ("Seats", dp(40)),
            ],
            row_data=table_row_data
        )

    def refresh_table_table(self):
        self.table_table.row_data = [(table_item['number'], table_item['seats'])
                                     for table_item in self.table_list]

    def add_table(self, instance):
        popup = Popup(
            title='Add Table',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Add Table functionality")
        )
        popup.open()

    def update_table(self, instance):
        popup = Popup(
            title='Update Table',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Update Table functionality")
        )
        popup.open()

    def delete_table(self, instance):
        popup = Popup(
            title='Delete Table',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Delete Table functionality")
        )
        popup.open()


class OrderStatusManagerContent:
    def __init__(self):
        self.order_status_list = [{'table': 'Table #1', 'status': 'READY'},
                                  {'table': 'Table #2', 'status': 'IN PROGRESS'}]

    def create_content_panel(self):
        panel = GridLayout(cols=1, padding=20, spacing=10)

        # Data Table
        self.order_status_table = self.create_order_status_table()
        panel.add_widget(self.order_status_table)

        # Update, Revert buttons
        button_panel = GridLayout(cols=2, spacing=10)
        update_button = MDRaisedButton(
            text='Update Status', on_press=self.update_status)
        revert_button = MDRaisedButton(
            text='Revert Status', on_press=self.revert_status)

        button_panel.add_widget(update_button)
        button_panel.add_widget(revert_button)
        panel.add_widget(button_panel)

        return panel

    def create_order_status_table(self):
        table_row_data = [(order_item['table'], order_item['status'])
                          for order_item in self.order_status_list]

        return MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Table", dp(40)),
                ("Status", dp(40)),
            ],
            row_data=table_row_data
        )

    def refresh_order_status_table(self):
        self.order_status_table.row_data = [(order_item['table'], order_item['status'])
                                            for order_item in self.order_status_list]

    def update_status(self, instance):
        popup = Popup(
            title='Update Order Status',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Update Order Status functionality")
        )
        popup.open()

    def revert_status(self, instance):
        popup = Popup(
            title='Revert Order Status',
            size_hint=(None, None), size=(400, 400),
            content=Label(text="Revert Order Status functionality")
        )
        popup.open()


class RestaurantPointApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ManagementPanelScreen(name='management_panel'))
        return sm


if __name__ == '__main__':
    RestaurantPointApp().run()
