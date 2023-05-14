# Copyright (c) 2023, qcs and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class hi(Document):
	def onload(self):
		if not self.parent_error_snapshot:
			self.db_set("seen", 1, update_modified=False)

			for relapsed in frappe.get_all("Error Snapshot", filters={"parent_error_snapshot": self.name}):
				frappe.db.set_value("Error Snapshot", relapsed.name, "seen", 1, update_modified=False)

			frappe.local.flags.commit = True