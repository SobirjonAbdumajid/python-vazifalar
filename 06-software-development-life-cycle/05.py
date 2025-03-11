from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# Abstract ParkingSpot
class ParkingSpot(ABC):
    def __init__(self, spot_id: int):
        self.id = spot_id
        self.is_free = True

    def occupy_spot(self):
        self.is_free = False

    def free_spot(self):
        self.is_free = True

    def get_is_free(self):
        return self.is_free


# Different parking spot types
class LargeSpot(ParkingSpot):
    pass


class MotorcycleSpot(ParkingSpot):
    pass


class CompactSpot(ParkingSpot):
    pass


class HandicappedSpot(ParkingSpot):
    pass


# Abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, license_no: str):
        self.license_no = license_no

    def assign_ticket(self):
        return self.license_no


# Different vehicle types
class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class Van(Vehicle):
    pass


# Parking Ticket class
class ParkingTicket:
    def __init__(self, car_no: str, amount: float = 0.0):
        self.car_no = car_no
        self.timestamp = datetime.now()
        self.exit_time = None
        self.amount = amount
        self.payment = None

    def make_payment(self, amount: float):
        self.payment = CashPayment(amount, "Completed")
        self.exit_time = self.timestamp + timedelta(hours=amount / 10)  # Assume $10 per hour
        print(f"Paid till {self.exit_time} for {self.car_no}")


# Abstract Payment class
class Payment(ABC):
    def __init__(self, amount: float, status: str):
        self.amount = amount
        self.status = status
        self.timestamp = datetime.now()

    @abstractmethod
    def initiate_transaction(self):
        pass


# Different payment methods
class CashPayment(Payment):
    def initiate_transaction(self):
        self.status = "Completed"
        print("Cash payment processed.")


class CreditCardPayment(Payment):
    def initiate_transaction(self):
        self.status = "Completed"
        print("Credit card payment processed.")


# ParkingLot class
class ParkingLot:
    def __init__(self, lot_id: int, name: str):
        self.id = lot_id
        self.name = name
        self.parking_spots = []

    def add_parking_spot(self, spot: ParkingSpot):
        self.parking_spots.append(spot)

    def get_free_spot(self):
        for spot in self.parking_spots:
            if spot.get_is_free():
                return spot
        return None


# Entrance class
class Entrance:
    def __init__(self, entrance_id: int):
        self.id = entrance_id

    def get_ticket(self, car_no: str) -> ParkingTicket:
        print(f"Ticket issued for {car_no}")
        return ParkingTicket(car_no)


# Exit class
class Exit:
    def __init__(self, exit_id: int):
        self.id = exit_id

    def validate_ticket(self, ticket: ParkingTicket):
        if ticket.payment and ticket.payment.status == "Completed":
            print("Ticket validated. You may exit.")
        else:
            print("Payment required before exit.")


# Running the system
def run():
    lot = ParkingLot(1, "Main Parking")
    lot.add_parking_spot(CompactSpot(1))
    lot.add_parking_spot(LargeSpot(2))

    entrance = Entrance(1)
    ticket = entrance.get_ticket("01ABS001")
    ticket.make_payment(20)  # Paying for 2 hours

    exit_gate = Exit(1)
    exit_gate.validate_ticket(ticket)


if __name__ == "__main__":
    run()
