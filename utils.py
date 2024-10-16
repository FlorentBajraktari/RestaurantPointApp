from enums import UserFeatures
from admin_view import EmployeeManagerContentPanel, TaskManagerContentPanel, DepartmentManagerContentPanel, PayrollManagerContentPanel, AccountManagerContentPanel, CustomerManagementContentPanel, HolidayManagerContentPanel, SalesManagementContentPanel, CalendarManagementContentPanel


class UserFeatureContentPanelResolver:
    @staticmethod
    def get_user_feature_panel(feature):
        content_panel_mapping = {
            UserFeatures.MANAGE_EMPLOYEES: EmployeeManagerContentPanel,
            UserFeatures.MANAGE_TASKS: TaskManagerContentPanel,
            UserFeatures.MANAGE_DEPARTMENTS: DepartmentManagerContentPanel,
            UserFeatures.MANAGE_PAYROLL: PayrollManagerContentPanel,
            UserFeatures.MANAGE_ACCOUNTS: AccountManagerContentPanel,
            UserFeatures.MANAGE_CUSTOMERS: CustomerManagementContentPanel,
            UserFeatures.MANAGE_HOLIDAYS: HolidayManagerContentPanel,
            UserFeatures.MANAGE_SALES: SalesManagementContentPanel,
            UserFeatures.MANAGE_CALENDAR: CalendarManagementContentPanel,
        }

        return content_panel_mapping.get(feature, None)

    @staticmethod
    def get_user_feature_content_panel_map():
        return {
            "Employees": EmployeeManagerContentPanel(),
            "Tasks": TaskManagerContentPanel(),
            "Departments": DepartmentManagerContentPanel(),
            "Payroll": PayrollManagerContentPanel(),
            "Accounts": AccountManagerContentPanel(),
            "Customers": CustomerManagementContentPanel(),
            "Holidays": HolidayManagerContentPanel(),
            "Sales": SalesManagementContentPanel(),
            "Calendar": CalendarManagementContentPanel(),
        }


class AuthorizationService:
    @staticmethod
    def is_user_authorized(user, feature: UserFeatures):
        return feature in user.features
