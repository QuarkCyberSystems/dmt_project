# Copyright (c) 2022, White Hat Global and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

# @frappe.whitelist(allow_guest=True)
# def mark_checkin(employee,device,dtime,time=datetime.today().date()):
#     form1 = frappe.db.get_value('Employee Checkin', filters={"employee": employee , "date":time},fieldname="employee")
#     if not form1:
#         doc = frappe.new_doc('Employee Checkin')
#         doc.employee = employee
#         doc.time = dtime 
#         doc.log_type = "IN"
#         doc.device_id = device
#         doc.save(ignore_permissions=True)
#         frappe.db.commit()
#         return employee
#     else:
#         form = frappe.get_last_doc('Employee Checkin', filters={"employee": employee})
        
#         if form.log_type == 'OUT':
#             doc = frappe.new_doc('Employee Checkin')
#             doc.employee = employee
#             doc.time = dtime 
#             doc.log_type = "IN"
#             doc.device_id = device
#             doc.save(ignore_permissions=True)
#             frappe.db.commit()
#             return employee
#         elif form.log_type == 'IN':
#             doc = frappe.new_doc('Employee Checkin')
#             doc.employee = employee
#             doc.time = dtime 
#             doc.log_type = "OUT"
#             doc.device_id = device
#             doc.save(ignore_permissions=True)
#             frappe.db.commit()
#             return employee
    
    