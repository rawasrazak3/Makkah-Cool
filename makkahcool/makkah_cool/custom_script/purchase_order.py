from frappe.model.naming import make_autoname
import frappe


def autoname(doc, method):
    if doc.set_warehouse == "Shuwaikh Showroom - MCR&ACSP":
        doc.name= make_autoname(f"S-{doc.naming_series}")