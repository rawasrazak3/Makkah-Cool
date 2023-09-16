// frappe.ui.form.on('Purchase Invoice', {
//	refresh(frm) {
        // blaa blaa blaa
//	}
//});

// child table name
//frappe.ui.form.on('Purchase Invoice Item', {                                    
//    refresh(frm){
//        frm.trigger('item_code');
//    },
//  item_code(frm, cdt, cdn) {
//      let co = locals[cdt][cdn];
//      if (frm.doc.items && frm.doc.supplier) {
//            frappe.call({
//                method: "makkahcool.makkah_cool.custom_script.sales_invoice.last_price",
//                args: {
//                    "supplier": frm.doc.supplier,
//                },
//                callback: function (r) {
//                    let rmsg = r.message;
//                    if (rmsg) {
//                        Object.entries(rmsg).forEach(([itk, itv]) => {
//                            if (co.item_code == itk) {
//                                co.rate = itv;
//                              frappe.get_doc('Item Price', itk).price_list_rate = itv ;
  //                              alert('reached') ;
    //                        }
      //                  });
        //            }
          //      }
//            });
  //      }
//    }
//});
