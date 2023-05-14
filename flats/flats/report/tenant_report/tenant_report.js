// Copyright (c) 2023, qcs and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Tenant Report"] = {
	"filters": [
		{
			"fieldname":"tanent",
			"label": __("Tenant"),
			"fieldtype": "Link",
			"options":  "Tenant Name",
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default":  frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname":"apartment",
			"label": __("Apartment"),
			"fieldtype": "Link",
			"options": "Apartments"
		},
		{
			"fieldname":"status",
			"label": __("Select"),
			"fieldtype": "Select",
			"options": ["", "Active", "Inactive"]
		},

	],
	"formatter": function(value, row, column, data, default_formatter) {
		if (data.name){
			value = $(`<span>${value}</span>`);
			var $value = $(value).css("font-weight", "bold");
			value = $value.wrap("<p></p>").parent().html();
		}
		return value;

	}
};
