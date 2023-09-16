frappe.ui.form.on('Sales Invoice', {
	refresh(frm) {
        //
	}
});


frappe.ui.form.on('Sales Invoice Item', {
    refresh(frm){
        frm.trigger('item_code');
    },
    item_code(frm, cdt, cdn) {
      let co = locals[cdt][cdn];
      co.last_buy_price = 0;
      co.sqty = 0;
      if (frm.doc.items && frm.doc.customer) {
            frappe.call({
                method: "makkahcool.makkah_cool.custom_script.sales_invoice.last_price",
                args: {
                    "customer": frm.doc.customer,
                },
                callback: function (r) {
                    let rmsg = r.message;
                    if (rmsg) {
                        Object.entries(rmsg).forEach(([itk, itv]) => {
                            if (co.item_code == itk) {
                                co.last_buy_price = itv;
                            }
                        });
                    }
                }
            });

            frappe.call({
                method: "makkahcool.makkah_cool.custom_script.sales_invoice.stock_qty_1",
                args: {
                    "item_code": co.item_code,
                },
                callback: function (r) {
                    let sqty = r.message;
                    if (sqty) {
                        co.sqty = sqty;
                    }
                }
            });

            frappe.call({
                method: "makkahcool.makkah_cool.custom_script.sales_invoice.last_buying",
                args: {
                    "item_code": co.item_code,
                },
                callback: function (r) {
                    let sqty = r.message;
                    if (sqty) {
                        co.buying_price_list = sqty;
                    }
                }
            });
        }
    }
});
