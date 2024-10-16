from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from dataprovider import DataProvider
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown


class TaskManagerContentPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_task_index = None  # Track selected task for update and delete
        self.orientation = 'vertical'
        self.add_widget(self.create_task_input_data_panel())
        self.add_widget(self.create_management_panel())

    def create_task_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400
        self.name_input = MDTextField(
            multiline=True, font_size='18sp', hint_text='Name')
        input_data_component_panel.add_widget(self.name_input)
        self.description_input = MDTextField(
            multiline=True, font_size='18sp', hint_text='Description')
        input_data_component_panel.add_widget(self.description_input)
        input_data_component_panel.add_widget(
            self.create_priority_input_data_panel())
        input_data_component_panel.add_widget(
            self.create_button_component_panel())
        return input_data_component_panel

    def create_priority_input_data_panel(self):
        self.priority_input_panel = GridLayout(cols=2, spacing=20)
        self.priority_input_panel.size_hint = (None, None)
        # Assuming there are three priority levels: Low, Medium, High
        self.priority_options = ['Low', 'Medium', 'High']
        self.priority_checkboxes = {}

        for priority in self.priority_options:
            checkbox = CheckBox(
                group='priority', active=False, color=(0, 0, 0, 1))
            checkbox_label = Label(text=priority, color=(0, 0, 0, 1))
            self.priority_input_panel.add_widget(checkbox)
            self.priority_input_panel.add_widget(checkbox_label)
            self.priority_checkboxes[priority] = checkbox

        return self.priority_input_panel

    def create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self.create_department_selector_panel())
        content_panel.add_widget(self.create_employee_selector_panel())
        content_panel.add_widget(self.create_table())
        return content_panel

    def create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(text='Add', size_hint=(
            None, None), size=(80, 40), background_color=(0, 1, 1, 1))
        add_button.bind(on_press=self.add_task)
        update_button = Button(text='Update', size_hint=(
            None, None), size=(80, 40), background_color=(0, 1, 1, 1))
        update_button.bind(on_press=self.update_task)
        delete_button = Button(text='Delete', size_hint=(
            None, None), size=(80, 40), background_color=(0, 1, 1, 1))
        delete_button.bind(on_press=self.delete_task)
        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel

    def create_department_selector_panel(self):
        button = Button(text='Select a department', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))
        button.bind(on_release=self.show_department_list)
        return button

    def show_department_list(self, button):
        menu_items = []
        department_list = DataProvider().department_list

        for department in department_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': department.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def create_employee_selector_panel(self):
        button = Button(text='Select an employee', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))
        button.bind(on_release=self.show_employee_list)
        return button

    def show_employee_list(self, button):
        menu_items = []
        employee_list = DataProvider().department_list[0].employee_list

        for employee in employee_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': employee.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def create_table(self):
        table_row_data = []
        department = DataProvider().department_list[0]
        employees = department.employee_list
        task_list = employees[0].task_list if employees else []

        for task in task_list:
            table_row_data.append(
                (task.name, task.description, task.priority.value))

        self.task_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Description", dp(30)),
                ("Priority", dp(20))
            ],
            row_data=table_row_data
        )
        self.task_table.bind(on_row_press=self.select_task)
        return self.task_table

    def add_task(self, instance):
        name = self.name_input.text
        description = self.description_input.text
        priority = self.get_selected_priority()

        if name and description and priority:
            task = {'name': name, 'description': description,
                    'priority': priority}
            # Add the task to the employee's task list
            department = DataProvider().department_list[0]
            employee = department.employee_list[0]
            employee.task_list.append(task)
            self.refresh_task_table()
            self.clear_inputs()

    def update_task(self, instance):
        if self.selected_task_index is not None:
            department = DataProvider().department_list[0]
            employee = department.employee_list[0]
            task = employee.task_list[self.selected_task_index]

            task['name'] = self.name_input.text
            task['description'] = self.description_input.text
            task['priority'] = self.get_selected_priority()

            self.refresh_task_table()
            self.clear_inputs()

    def delete_task(self, instance):
        if self.selected_task_index is not None:
            department = DataProvider().department_list[0]
            employee = department.employee_list[0]
            employee.task_list.pop(self.selected_task_index)

            self.selected_task_index = None
            self.refresh_task_table()
            self.clear_inputs()

    def select_task(self, instance, row_data):
        # This method will handle selecting a task from the table
        self.selected_task_index = self.task_table.row_data.index(row_data)
        department = DataProvider().department_list[0]
        employee = department.employee_list[0]
        task = employee.task_list[self.selected_task_index]

        # Set the inputs to the selected task data
        self.name_input.text = task['name']
        self.description_input.text = task['description']
        self.set_selected_priority(task['priority'])

    def get_selected_priority(self):
        for priority, checkbox in self.priority_checkboxes.items():
            if checkbox.active:
                return priority
        return None

    def set_selected_priority(self, priority):
        for key, checkbox in self.priority_checkboxes.items():
            checkbox.active = key == priority

    def refresh_task_table(self):
        # Refresh the task table after add/update/delete
        department = DataProvider().department_list[0]
        employees = department.employee_list
        task_list = employees[0].task_list if employees else []

        table_row_data = [
            (task['name'], task['description'], task['priority']) for task in task_list
        ]
        self.task_table.row_data = table_row_data

    def clear_inputs(self):
        self.name_input.text = ""
        self.description_input.text = ""
        self.set_selected_priority(None)
