// Copyright (c) 2024, Pragati Dike and contributors
// For license information, please see license.txt
frappe.ui.form.on("Cost Breakup", {
    amount(frm, cdt, cdn) {
        let total = 0;
        frm.doc.cost_breakup.forEach(function(d) {
            total += d.amount;
        });
        frm.set_value("total", total);
    }
});

