# Copyright (c) 2023, qcs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json


class AccessControlDevice(Document):
	def validate(self):
		if(self.check_device_state==1):
			frappe.errprint("llllll")
			url= self.url + "/api/auth/login/challenge?username=" + self.user_name
			frappe.errprint(url)

			payload={}
			headers = {}

			response = requests.request("GET", url, headers=headers, data=payload)
			json_data = json.loads(response.text)
			try:
				if(json_data['salt']):
					frappe.msgprint("Device Successfully Login")
					self.status="Active"
					
			except:
				frappe.msgprint("Please Check Device Credential. Something Went Wrong")
				self.status="Inactive"
			
	 
