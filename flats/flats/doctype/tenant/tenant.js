// Copyright (c) 2023, qcs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenant', {
	refresh: function(frm) {

		frm.add_custom_button(__("Create Device Information"), function(){
			if(cur_frm.doc.id_table){
				frappe.call({
					method: "flats.bio_metric.bio_login.create_personal_id",
					args: {
						"name":cur_frm.doc.name
					},
					callback: function(r) {
						if(r.message){
							frappe.show_alert({
								message:__('Successfully Personal Details Updated in Device.'),
								indicator:'green'
							}, 10);
						}
					}
				});
			}
			else{
				frappe.msgprint("Please Fill The Informations")
			}
		}).css({'color':'white','font-weight': 'bold', 'background-color': '#1E90FF'});

		frm.set_query("id_card_no", 'id_table',function() {
			return {
				filters: {
					'status': 'Active'
				}
			}
		});
		frm.set_query("apartment",function() {
			return {
				filters: {
					'status': 'Active'
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
