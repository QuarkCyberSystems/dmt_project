# Copyright (c) 2023, qcs and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters={}

	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data


def get_columns(filters):
	columns= [
		{
			"label": ("Name"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options":"Tenants",
			"width": 185,	
		},
		{
			"label": ("Tenant"),
			"fieldname": "tenant",
			"fieldtype": "Link",
			"options":"Tenant Name",
			"width": 185,	
		},
		{
			"label": ("Apartment Name"),
			"fieldname": "apt",
			"fieldtype": "Data",
			"width": 100,
			
		},
		{
			"label": ("Apartment No"),
			"fieldname": "aot_no",
			"fieldtype": "Data",
   			"width": 100,
		},
		{
			"label": ("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": ("Contract Expiry"),
			"fieldname": "ce",
			"fieldtype": "Date",
			"width": 100,
			
		},
	
	]
	
	return columns

def get_data(filters):
	query_filters=[]
	if filters.get("from_date"):
		query_filters.append(["contract_expiry", ">=", filters["from_date"]])
	if filters.get("to_date"):
		query_filters.append(["contract_expiry", "<=", filters["to_date"]])
	if filters.get("tanent"):
		query_filters.append(["tenant", "=", filters["tanent"]])
	if filters.get("apartment"):
		query_filters.append(["apartment", "=", filters["apartment"]])
	if filters.get("status"):
		query_filters.append(["tenant_status", "=", filters["status"]])
   
	query_filters.append(["docstatus", "=", 1])
 
	data=[]
	doc=frappe.get_all("Tenants", filters=query_filters, fields=['name', 'tenant', 'apt', 'apt_no', 'tenant_status', 'contract_expiry'])
	for i in doc:
		data.append([i.get("name"),i.get("tenant"), i.get("apt"),i.get("apt_no"),i.get("tenant_status"),i.get("contract_expiry")])
		name=i.get("name")
		inside_data=item(name)
		for j in inside_data:
				data.append(j)
	return data
	
def item(name):
	doc=frappe.get_doc("Tenants", name)
	tab=doc.id_table
	datas=[]
	for i in range(0, len(tab)):
		datas.append(["", tab[i].get("person_name"),"", "", "", ""])
	
	return datas