from frappe.model.naming import make_autoname
import frappe


def autoname(doc, method):
    if doc.payment_type == "Receive":
        doc.name= make_autoname(f"REC-{doc.naming_series}")
    if doc.payment_type == "Pay":
        doc.name= make_autoname(f"PAY-{doc.naming_series}")
        