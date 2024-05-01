# Copyright (c) 2024, Lay Virak and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
	def before_save(self):
		if self.seat == None:
			self.generate_seat()
		self.cal_total_amount()

	def validate(self):
		unique_data = set()
		filtered_res = []
		for item in self.add_ons:
			if item.get('item') not in unique_data:
				filtered_res.append(item)
				unique_data.add(item.get('item'))
		self.set('add_ons', filtered_res)

	def on_submit(self):
		airplane = frappe.db.get_value("Airplane Flight", {'name': self.flight}, ['airplane'])
		capacity = frappe.db.get_value("Airplane", {'name': airplane}, ['capacity'])
		get_seat_gen=int(self.seat[:-1])
		if self.status != "Boarded":
			frappe.throw("The flight is on boarded")
		
		elif get_seat_gen > capacity :
			frappe.throw("Seat number more then capacity")
	
	# def after_insert(self):
	# 	print('ssssssssssssssss')
	# 	self.remove_douplicate_data()

	def cal_total_amount(self):
		total_ammount_add_ons = 0
		
		for ammount in self.add_ons:
			total_ammount_add_ons += ammount.amount
		self.total_amount = total_ammount_add_ons + float(self.flight_price)

	def generate_seat(self):
		seat_number = random.randint(1, 100)  # Assuming 100 seats
		seat_letter = random.choice(string.ascii_uppercase[:5])  # A to E
		self.seat= f"{seat_number}{seat_letter}"



