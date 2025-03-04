from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Payment:
    amount: float
    status: PaymentStatus
    timestamp: datetime

    def initiate_transaction(self):
        self.status = PaymentStatus.COMPLETED  # Imitatsiya uchun


class ParkingSpot(ABC):
    def __init__(self, id_: int, is_free: bool = True):
        self.id = id_
        self.is_free = is_free

    @abstractmethod
    def get_is_free(self) -> bool:
        return self.is_free


class Large(ParkingSpot):
    def get_is_free(self) -> bool:
        return self.is_free


class Compact(ParkingSpot):
    def get_is_free(self) -> bool:
        return self.is_free


class Handicapped(ParkingSpot):
    def get_is_free(self) -> bool:
        return self.is_free


class Vehicle(ABC):
    def __init__(self, license_no: str):
        self.license_no = license_no
        self.ticket = None

    def assign_ticket(self, ticket: 'ParkingTicket'):
        self.ticket = ticket


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Van(Vehicle):
    pass


@dataclass
class ParkingTicket:
    ticket_no: int
    entry_time: datetime
    exit_time: datetime = None
    amount: float = 0.0
    payment: Payment = None

    def close_ticket(self, amount: float):
        self.exit_time = datetime.now()
        self.amount = amount
        self.payment = Payment(amount, PaymentStatus.COMPLETED, datetime.now())


@dataclass
class Entrance:
    id: int

    def get_ticket(self) -> ParkingTicket:
        return ParkingTicket(ticket_no=1001, entry_time=datetime.now())


@dataclass
class Exit:
    id: int

    def validate_ticket(self, ticket: ParkingTicket):
        if ticket.exit_time is None:
            ticket.close_ticket(10.0)  # Misol uchun narx
            return "To'lov bajarildi"
        return "Ticket allaqachon yopilgan"


# Test qilish
entrance = Entrance(1)
ticket = entrance.get_ticket()

car = Car(license_no="ABC123")
car.assign_ticket(ticket)

exit_gate = Exit(1)
print(exit_gate.validate_ticket(ticket))  # "To'lov bajarildi"
print(exit_gate.validate_ticket(ticket))  # "Ticket allaqachon yopilgan"
