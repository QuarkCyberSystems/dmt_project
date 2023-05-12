// Copyright (c) 2023, qcs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenants', {
	refresh: function(frm) {
		frm.set_query("person_name", 'id_table',function() {
			return {
				filters: {
					't_status': 'Active'
				}
			}
		});
		frm.set_query("id_card_no", 'id_table',function() {
			return {
				filters: {
					'id_status': 'Active'
				}
			}
		});
		frm.set_query("tenant",function() {
			return {
				filters: {
					't_status': 'Active'
				}
			}
		});
	},
	contract_expiry: function(frm){
		if(cur_frm.doc.contract_expiry < frappe.datetime.get_today()){
			frappe.throw("Please Check the Contract Expiry. It Less then Today")
		}
	}
});
