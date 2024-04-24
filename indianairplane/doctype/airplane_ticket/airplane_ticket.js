// Copyright (c) 2024, Pragati Dike and contributors
// For license information, please see license.txt
function assignSeat() {
    frappe.prompt(
        [
            {
                label: 'Seat Number',
                fieldname: 'seatNumber',
                fieldtype: 'Data',
                reqd: 1 
            }
        ],
        function(values) {
            cur_frm.set_value('seat', values.seatNumber);
        },
        'Assign Seat',
        'Save'
    );
}

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign Seat'), assignSeat);
    }
});
