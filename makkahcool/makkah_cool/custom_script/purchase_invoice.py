#import frappe

#@frappe.whitelist()
#def last_price(supplier):
 #   results = {}
  #  query = []
   # query = frappe.get_all('Purchase Invoice',filters={"docstatus": '1'},fields=['name'], order_by='name asc',as_list=True)
   # for q in query:
    #    q = q[0]
     #   exst = frappe.db.exists('Purchase Invoice', {"docstatus": '1', "name": f'{q}'})
      #  if exst:
       #     qq = frappe.get_doc('Purchase Invoice',{"docstatus": '1', "name": f'{q}'})
        #    if qq:
         #       for it in qq.items:
          #          results[f'{it.item_code}'] = it.rate
    
#    return results

from frappe.model.naming import make_autoname
import frappe


def autoname(doc, method):
    if doc.set_warehouse == "Shuwaikh Showroom - MCR&ACSP":
        doc.name= make_autoname(f"S-{doc.naming_series}")