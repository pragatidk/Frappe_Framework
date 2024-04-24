# Copyright (c) 2024, Pragati Dike and contributors
# For license information, please see license.txt
import frappe
from frappe import _

from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def before_submit(self):
        if self.status == "Scheduled":
            self.status = "Completed"
        else:
            self.update_status()

    def update_status(self):
        if self.status == "Scheduled":
            self.db_set("status", "Completed")
