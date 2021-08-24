// Copyright (c) 2021, Bantoo Accounting Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wish', {
	// refresh: function(frm) {

	// }

      refresh: function(frm) {

        frm.add_custom_button(__('Get asset Detailes'), function(){
          frappe.msgprint(frm.doc.asset);
      }, __("Utilities"));

    }
  });
