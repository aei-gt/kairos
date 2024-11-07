# Copyright (c) 2024, AEI and contributors
# For license information, please see license.txt

import frappe
import requests
from datetime import datetime
from frappe.model.document import Document


class kairos_expediente(Document):
	def before_insert(self):
		current_year = datetime.now().strftime("%y")
		prefix = f"E{current_year}-"
		last_id = frappe.db.get_value(
            "Kairos Expediente", 
            {"document_id": ["like", f"{prefix}%"]}, 
            "document_id", 
            order_by="creation desc"
        )
		if last_id:
			next_number = int(last_id.split("-")[-1]) + 1
		else:
			next_number = 1
		self.document_id = f"{prefix}{str(next_number).zfill(2)}"

	def on_update(self):
		settings = frappe.get_doc("Evolution Api Settings", "Evolution Api Settings")
		url = settings.url
		api_key = settings.api_key
		base_url = frappe.utils.get_url()  # This will fetch the base URL of your Frappe site
		doc_name = f"{base_url}/app/issue/{self.name}"
		if self.default_department:
			manager = frappe.db.get_value("Department", self.default_department, 'custom_manager')
			if manager:
				manager_number = frappe.db.get_value("Employee", manager, 'cell_number')
				if manager_number:
					manager_message = f"Se le asigno la solicitud con referencia {self.document_id} this id_document with the full url {doc_name}, asunto & {self.description}"
					send_message(manager_number, manager_message, api_key, url)

		if self.employee:
				employee_number = frappe.db.get_value("Employee", self.employee, 'cell_number')
				if employee_number:
					emp_message = f"Se le asigno la solicitud con referencia {self.document_id} this id_document with the full url {doc_name}, asunto & {self.expediente_detalle_nota}"
					send_message(manager_number, emp_message, api_key, url)

def send_message(number, message, api_key, url):
	"""Helper function to send WhatsApp message."""
	payload = {
		"number": number,
		"text": message
	}
	headers = {
		"apikey": api_key,
		"Content-Type": "application/json"
	}
	try:
		response = requests.post(url, json=payload, headers=headers)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		frappe.log_error(message=str(e), title="WhatsApp Message Sending Failed")