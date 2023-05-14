# Copyright (c) 2023, qcs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AcceptDataLog(Document):
	@staticmethod
	def clear_old_logs(days=130):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("Accept Data Log")
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
