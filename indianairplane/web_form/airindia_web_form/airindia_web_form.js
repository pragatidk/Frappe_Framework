// frappe.ready(function() {
// 	// bind events here
// 	frappe.web_form.set_value("flight_price",2000)
// })



frappe.ready(function() {
    var randomPrice = Math.floor(Math.random() * (10000 - 1000 + 1)) + 1000;
    frappe.web_form.set_value("flight_price", randomPrice);
});
