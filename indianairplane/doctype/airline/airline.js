// Copyright (c) 2024, Pragati Dike and contributors
// For license information, please see license.txt
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_web_link(frm.doc.website, 'Official Website').addClass('btn-primary');
        } else {
            // Remove the button if the website is not provided
            frm.remove_custom_button('Official Website');
        }
    }
});
