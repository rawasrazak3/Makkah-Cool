frappe.ui.form.on('Purchase Invoice', {
	refresh(frm) {
        // blaa blaa blaa
	}
});


frappe.ui.form.on('Purchase Invoice Item', {
    refresh(frm){
        frm.trigger('item_code');
    },
    item_code(frm, cdt, cdn) {
      let co = locals[cdt][cdn];
      co.stock_q = 0;
      if (frm.doc.items && frm.doc.supplier) {
            frappe.call({
                method: "makkahcool.makkah_cool.custom_script.sales_invoice.stock_qty_1",
                args: {
                    "item_code": co.item_code,
                },
                callback: function (r) {
                    let sqty = r.message;
                    if (sqty) {
                        co.stock_q = sqty;
                    }
                }
            });
        }
    }
});
