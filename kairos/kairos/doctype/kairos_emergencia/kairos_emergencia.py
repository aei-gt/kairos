# Copyright (c) 2024, AEI and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document


class kairos_emergencia(Document):
	def after_insert(self):
		send_whatsapp_message(self)
	def on_update(self):
		send_whatsapp_message(self)

def send_whatsapp_message(self):
	settings = frappe.get_doc("Evolution Api Settings", "Evolution Api Settings")
	url = settings.url
	api_key = settings.api_key
	number = settings.number
	message = settings.message
	# url = "https://api2.fraijanes.gt/message/sendText/MDF V2 Global"
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
		frappe.msgprint("Message sent successfully")
	except requests.exceptions.RequestException as e:
		frappe.throw(f"Failed to send message: {str(e)}")