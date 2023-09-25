// Copyright (c) 2023, sastechnologies.co and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Prices', {
	refresh(frm) {
		//
	}
});

// frappe.ui.form.on('Item Prices', {
//     refresh: function(frm) {
//         // Fetch Valuation Rate from stock_ledger_entry
//         frappe.call({
//             method: "valuation_rate_1",
//             args: {
//                 item_code: frm.doc.item
//             },
//             callback: function(r) {
//                 if (r.message) {
//                     frm.set_value('valuation_rate', r.message);
//                 }
//             }
//         });
//     }
// });

// frappe.ui.form.on('Item Prices Table', {
//     buying_price: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];
//         // Update the Item Price with the new buying price
//         frappe.call({
//             method: "makkahcool.makkah_cool.doctype.item_prices.update_item_price",
//             args: {
//                 item_code: child.item_code,
//                 buying_price: child.buying_price,
//                 selling_price: child.selling_price
//             }
//         });
//     },
//     selling_price: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];
//         // Update the Item Price with the new selling price
//         frappe.call({
//             method: "makkahcool.makkah_cool.doctype.item_prices.update_item_price",
//             args: {
//                 item_code: child.item_code,
//                 buying_price: child.buying_price,
//                 selling_price: child.selling_price
//             }
//         });
//     }
// });

// frappe.ui.form.on('Item Prices Table', {
//     item_code: function(frm) {
//         // Fetch valuation_rate from stock_ledger_entry
//         frappe.call({
//             method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.valuation_rate",
//             args: {
//                 "item_code": frm.doc.item_code,
//             },
//             callback: function(r) {
//                 if (r.message) {
//                     frm.set_value('valuation_rate', r.message.valuation_rate);
//                 }
//             }
//         });
//     },
// });

frappe.ui.form.on('Item Prices Table', {
    refresh(frm){
        frm.trigger('item_code');
    },
    item_code(frm, cdt, cdn) {
      let co = locals[cdt][cdn];
      co.valuation_rate = 0;
      if (frm.doc.item_prices_table) {
		frappe.call({
			method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.valuation_rate",
			args: {
				item_code: co.item_code,
			},
			callback: function (r) {
				let valuation_rate = r.message;
				if (valuation_rate) {
					co.valuation_rate = valuation_rate;
					frm.refresh_field('item_prices_table');
				}
			}
		});
		frappe.call({
			method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.cost",
			args: {
				item_code: co.item_code,
			},
			callback: function (r) {
				let cost_price = r.message;
				if (cost_price) {
					co.cost_price = cost_price;
					frm.refresh_field('item_prices_table');
				}
			}
		});
		frappe.call({
			method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.selling_price_1",
			args: {
				item_code: co.item_code,
			},
			callback: function (r) {
				let selling_price_1 = r.message;
				if (selling_price_1) {
					co.selling_price_1 = selling_price_1;
					frm.refresh_field('item_prices_table');
				}
			}
		});
		frappe.call({
			method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.selling_price_2",
			args: {
				item_code: co.item_code,
			},
			callback: function (r) {
				let selling_price_2 = r.message;
				if (selling_price_2) {
					co.selling_price_2 = selling_price_2;
					frm.refresh_field('item_prices_table');
				}
			}
		});
        }
    }
});

frappe.ui.form.on('Item Prices Table', {
    refresh: function(frm) {
        // Add a custom button or trigger the update on another event
        frm.save(__('Update Item Price'), function() {
            // Get the cost from the form field (assuming you have a field with the name 'cost')
            var newCost = frm.doc.cost;
            var itemCode = frm.doc.item_code; // You need to adjust this based on your field names

            // Call the server-side function to update the Item Price
            frappe.call({
                method: "makkahcool.makkah_cool.doctype.item_prices.item_prices.update_item_price",
                args: {
                    item_code: itemCode,
                    new_cost: newCost
                },
                callback: function(r) {
                    // Handle the response if needed
                    if (r.message) {
                        frappe.msgprint('Item Price updated successfully.');
                    }
                }
            });
        });
    }
});