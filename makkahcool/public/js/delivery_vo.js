frappe.ui.form.on('Delivery Note', {
	refresh(frm) {
        //
	}
});


frappe.ui.form.on('Delivery Note Item', {
    refresh(frm){
        frm.trigger('item_code');
    },
    item_code(frm, cdt, cdn) {
      let co = locals[cdt][cdn];
      co.last_buy_price = 0;
      co.sqty = 0;
      if (frm.doc.items && frm.doc.customer) {


            // frappe.call({
            //     method: "makkahcool.makkah_cool.custom_script.delivery_note.stock_qty_1",
            //     args: {
            //         "item_code": co.item_code,
            //     },
            //     callback: function (r) {
            //         let sqty = r.message;
            //         if (sqty) {
            //             co.sqty = sqty;
            //         }
            //     }
            // });

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
