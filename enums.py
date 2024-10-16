from enum import Enum


class OrderStatus(Enum):
    QUEUE = "Queue"
    IN_PROGRESS = "In Progress"
    READY = "Ready"
    PAID = "Paid"


class TableStatus(Enum):
    AVAILABLE = "Available"
    OCCUPIED = "Occupied"
    RESERVED = "Reserved"

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"

class UserFeatures(Enum):
    VIEW_MENU = "view_menu"
    CREATE_ORDER = "create_order"
    MANAGE_EMPLOYEES = "manage_employees"
    VIEW_REPORTS = "view_reports"