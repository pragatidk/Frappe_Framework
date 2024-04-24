import frappe
from frappe.model.document import Document
from frappe import _
import random
import string

class AirplaneTicket(Document):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_seat()

    def generate_seat(self):
        if not self.seat:
            random_integer = random.randint(1, 99)
            random_alphabet = random.choice('ABCDE')
            seat = str(random_integer) + random_alphabet
            self.seat = seat

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw(_("Airplane Ticket cannot be submitted unless the status is 'Boarded'."))
        else:
            self.update_status()

    def update_status(self):
        if self.name:
            self.db_set("status", "Completed")

    def validate(self):
        self.check_capacity()
        self.remove_duplicate()
        self.calculate_total()

    def check_capacity(self):
        if self.flight:
            # Fetch the count of existing tickets for the flight
            ticket_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

            flight = frappe.get_doc("Airplane Flight", self.flight)
            if flight:
                airplane = frappe.get_doc("Airplane", flight.airplane)
                if ticket_count > airplane.capacity:
                    frappe.throw("Number of tickets exceeds airplane capacity. Cannot create Airplane Ticket.")

    def remove_duplicate(self):
        unique_add_ons = {}
        for a in self.add_ons:
            key = a.item
            if key not in unique_add_ons:
                unique_add_ons[key] = a
            else:
                frappe.msgprint(f"This item {key} is already exist.")
        self.set("add_ons", list(unique_add_ons.values()))

    def calculate_total(self):
        total = 0
        for row in self.add_ons:
            total += row.amount

        self.total_amount = total + self.flight_price
