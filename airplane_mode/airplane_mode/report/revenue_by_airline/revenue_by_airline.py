# Copyright (c) 2024, Lay Virak and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{
			"fieldname": "airline",
			"label": "Airline",
			"fieldtype": "Data",
            "width": 150
		},
		{
			"fieldname": "amount",
			"label": "Amount",
			"fieldtype": "Currency",
            "width": 150
		},
	]
	data = []
	# get all the Airline
	airline_list = frappe.get_list("Airline",fields=['name'])
	# get all the Airplane Ticket
	airplan_tickey_list_list = frappe.get_all("Airplane Ticket", fields=["flight.airplane","total_amount"])

	
	for item in airline_list:
		data.append({
			'airline':item.name,
			'amount':0.00
		})
	
	# Loop data for total amount
	for item in airplan_tickey_list_list:
		get_airline = frappe.get_value("Airplane", {"name" : item.airplane}, ["airline"])
		for i, item_data in enumerate(data):
			if item_data['airline'] == get_airline:
				data[i]['amount'] += item.get('total_amount')

	# sort data by amount
	data.sort(key=myFunc,reverse=True)	

	# Create chart
	labels = []
	values = []
	for item in data:
		labels.append(item['airline'])
		values.append(item['amount'])
	
	chart = {
			"data": {
				"labels": labels,
				"datasets":  [{'name': ' ', 'values': values, 'chartType': 'bar'}]
			},
			"type": "donut" 
		}

	sum_total=sum(values)
	format = "${:,.2f}".format(sum_total)	

	message = [
        '<p style="text-align:center">Total Revenue By Airline</p>',
        f'<h3 style="text-align:center;color:green;font-size: 30px">{format}</h3>',
    ]

	return columns, data, message, chart

def myFunc(e):
  return e['amount']