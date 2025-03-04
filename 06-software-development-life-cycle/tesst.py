from abc import ABC, abstractmethod
from datetime import datetime


class ParkingSpot(ABC):
    def __init__(self, spot_id: int, is_free: bool = True):
        self.id = spot_id
        self.is_free = is_free

    def get_is_free(self):
        return self.is_free


class Vehicle(ABC):
    def __init__(self, license_no: str):
        self.license_no = license_no

    def assign_ticket(self):
        return self.license_no


class ParkingTicket:
    def __init__(self, car_no: str, amount: float = 0.0):
        self.car_no = car_no
        self.timestamp = datetime.now()
        self.exit_time = None
        self.amount = amount
        self.payment = None

    def make_payment(self):
        user_payment = float(input("Enter your payment amount: "))
        price_per_our = 10
        paid_time = user_payment / price_per_our
        # self.payment = user_payment
        # self.exit_time = self.timestamp + paid_time
        # print(self.exit_time, paid_time)
        print(f"Paid till {paid_time} hours for: {self.car_no}")


class Payment(ABC):
    def __init__(self, amount: float, status: str):
        self.amount = amount
        self.status = status
        self.timestamp = datetime.now()

    @abstractmethod
    def initiate_transaction(self):
        pass


class CashPayment(Payment):
    def initiate_transaction(self):
        self.status = "Completed"
        print("Cash payment processed.")


class CreditCardPayment(Payment):
    def initiate_transaction(self):
        self.status = "Completed"
        print("Credit card payment processed.")


class Entrance:
    def __init__(self, entrance_id: int):
        self.id = entrance_id

    def get_ticket(self, car_no: str) -> ParkingTicket:
        p = ParkingTicket(car_no)
        p.make_payment()
        return


class Exit:
    def __init__(self, exit_id: int):
        self.id = exit_id

    def validate_ticket(self, ticket: ParkingTicket):
        if ticket.payment and ticket.payment.status == "Completed":
            print("Ticket validated. You may exit.")
        else:
            print("Payment required before exit.")


def run():
    entrance = Entrance(1)
    ticket = entrance.get_ticket("01ABS001")
    # print(ticket)


if __name__ == "__main__":
    run()
