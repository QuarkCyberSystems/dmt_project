# Copyright (c) 2023, qcs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class Tenant(Document):
    def before_validate(self):
        tab=self.id_table
        tab_len=len(tab)
        allowed_reg=int(self.maximum_allowed_registration)
        
        if(self.number_of_people_lives_in < tab_len and allowed_reg > tab_len):
            frappe.msgprint("You Try add more People. Check the Number of people's lives Count.")
        if(allowed_reg < tab_len):
            frappe.throw("You Try add more People. Please Check Maximum Allowed Registration.")
        if(allowed_reg < self.number_of_people_lives_in):
            frappe.throw("Please Check Maximum Allowed Registration.")
     
    def on_submit(self):
        doc=frappe.get_doc("Apartments", self.apartment)
        doc.status="Occupied"
        doc.save()
        
        tab=self.id_table
        for j in range(0, len(tab)):
            
            id_name=tab[j].get("id_card_no")
            id_doc=frappe.get_doc("ID Card No", id_name)
            id_doc.id_status="Occupied"
            id_doc.save()
     
def contract_expiry():
    doc=frappe.get_all("Tenant", filters={"status":"Active"}, fields=["name", "contract_expiry"])
    for i in doc:
        ex_day=str(i.get("contract_expiry"))
        day=str(today())

        if(ex_day==day):
            frappe.errprint("ppp")
            doc2=frappe.get_doc("Tenant", i)
            
            tab=doc2.id_table
            for j in range(0, len(tab)):
                
                id_name=tab[j].get("id_card_no")
                id_doc=frappe.get_doc("Access Control Card", id_name)
                id_doc.id_status="Active"
                id_doc.save()
                
            doc3=frappe.get_doc("Apartments", doc2.apartment)
            doc3.status="Active"
            doc3.save()
            
            doc2.status="Inactive"
            doc2.save()
