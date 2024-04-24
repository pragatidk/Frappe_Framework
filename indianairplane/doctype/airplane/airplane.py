# Copyright (c) 2024, Pragati Dike and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airplane(Document):
	pass
	#  def validate(self):
    #     if self.flight and self.airplane:
    #         capacity = frappe.get_value("Airplane", self.airplane, "capacity")
    #         num_tickets = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
    #         if num_tickets >= capacity:
    #             frappe.throw(_("Cannot create more tickets for this flight. Capacity exceeded."))

