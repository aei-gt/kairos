# Copyright (c) 2024, AEI and contributors
# For license information, please see license.txt
import frappe
from datetime import datetime

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": "Employee Name",
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": "Department Name",
			"fieldname": "department_name",
			"fieldtype": "data",
			"width": 200
		},
		{
			"label": "Description",
			"fieldname": "description",
			"fieldtype": "data",
			"width": 200
		},
		{
			"label": "Date",
			"fieldname": "date",
			"fieldtype": "Date",
			"width": 200
		},
			{
			"label": "Finish Date",
			"fieldname": "finish_date",
			"fieldtype": "Date",
			"width": 200
		},
		{
			"label": "Status",
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 200
		},
	]
	return columns

def get_data(filters):
		data = []
		req_filters = {}
		
		if filters.get('employee_name'):
			req_filters['employee'] = filters.get('employee_name')
		if filters.get('department_name'):
			req_filters['department'] = filters.get('department_name')
		if filters.get('status'):
			req_filters['status'] = filters.get('status')
		if filters.get('department_name'):
			req_filters['department'] = filters.get('department_name')

		if filters.get('finish_date'):
			req_filters['finish_date'] = ["<", filters.get('finish_date')]

		req_client = frappe.get_list('Client Request', req_filters, ["*"])
		
		for req_data in req_client:
		

			data.append({
				"employee_name":req_data.employee,
				"description": req_data.description,
				"department_name": req_data.department,
				"date": req_data.date,
				"finish_date": req_data.finish_date,
				"status": req_data.status,
			})

		return data
