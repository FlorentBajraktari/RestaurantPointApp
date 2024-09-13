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
