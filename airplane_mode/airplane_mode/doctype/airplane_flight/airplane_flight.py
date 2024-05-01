# Copyright (c) 2024, Lay Virak and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(WebsiteGenerator,Document):

	# def after_submit(self):
	# 	# self.set_flight_status()
	

	def before_submit(self):
		self.status = "Completed"
		
	@frappe.whitelist()
	def set_flight_status(self):
		flight = frappe.get_doc("Airplane Flight",)
		flight.status = "Completed"
		flight.save()
