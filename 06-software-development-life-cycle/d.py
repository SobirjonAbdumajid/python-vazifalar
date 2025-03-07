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


class ParkingSpot(ABC):
    @abstractmethod
    def get_is_free(self) -> bool:
        pass


class Vehicle(ABC):
    pass


# Parking Spots
class Motorcycle(ParkingSpot):
    def __init__(self):
        self.is_free = True

    def get_is_free(self) -> bool:
        return self.is_free


@dataclass
class Compact(ParkingSpot):
    id: int
    is_free: bool

    def get_is_free(self) -> bool:
        return self.is_free


@dataclass
class Handicapped(ParkingSpot):
    id: int
    is_free: bool = True

    def get_is_free(self) -> bool:
        return self.is_free

    def get_ticket(self) -> 'ParkingTicket':
        return ParkingTicket(ticket_no=self.id, entry_time=datetime.now())


# Vehicles
@dataclass
class Car(Vehicle):
    plate_number: str


@dataclass
class Truck(Car):
    ticket_no: int
    entry_time: datetime
    exit_time: datetime = None
    amount: float = 0.0
    payment: Payment = None


@dataclass
class MotorVehicle(Car):
    payment: Payment


@dataclass
class Van(Car):
    amount: float
    status: PaymentStatus
    timestamp: datetime

    def initiate_transaction(self):
        self.payment = Payment(amount=self.amount, status=PaymentStatus.PENDING, timestamp=datetime.now())
        print(f"Transaction initiated for {self.amount}")


# Parking System Components
@dataclass
class Entrance:
    id: int

    def get_ticket(self) -> 'ParkingTicket':
        print(f"Ticket issued at entrance {self.id}")
        return ParkingTicket(ticket_no=self.id, entry_time=datetime.now())


@dataclass
class ParkingTicket:
    ticket_no: int
    entry_time: datetime
    exit_time: datetime = None
    amount: float = 0.0
    payment: Payment = None


@dataclass
class Exit:
    id: int

    def validate_ticket(self, ticket: ParkingTicket):
        ticket.exit_time = datetime.now()
        ticket.amount = 10.0  # Assuming a fixed charge
        ticket.payment = Payment(amount=ticket.amount, status=PaymentStatus.COMPLETED, timestamp=ticket.exit_time)
        print(f"Ticket {ticket.ticket_no} validated at exit {self.id}. Amount: {ticket.amount}")


def main():
    entrance = Entrance(id=1)
    exit_gate = Exit(id=1)

    ticket = entrance.get_ticket()
    print(f"Ticket {ticket.ticket_no} issued at {ticket.entry_time}")

    # Simulating exit after some time
    exit_gate.validate_ticket(ticket)
    print(f"Exit time: {ticket.exit_time}, Payment status: {ticket.payment.status}")


if __name__ == "__main__":
    main()
