# Copyright (c) 2023, sastechnologies.co and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemPrices(Document):
	pass
# @frappe.whitelist()
# def fetch_valuation_rate(item_code):
#     valuation_rate = frappe.db.sql("""
#         SELECT valuation_rate
#         FROM `tabStock Ledger Entry`
#         WHERE item_code = %s
#         ORDER BY posting_date DESC, posting_time DESC
#         LIMIT 1
#     """, item_code, as_dict=True)

#     return valuation_rate[0].get('valuation_rate') if valuation_rate else None

# @frappe.whitelist()
# def update_item_price(item_code, buying_price, selling_price):
#     item_price = frappe.get_doc('Item Price', {'item_code': item_code})
#     item_price.price_list_rate = "Cost Price"
#     item_price.price_list_rate = "Selling Price 1"
#     item_price.price_list_rate = "Selling Price 2"
#     item_price.save()
    
# @frappe.whitelist()
# def valuation_rate_1(item_code):
#     results = None  # Initialize results to None
#     entries = frappe.get_all(
#         'Stock Ledger Entry',
#         filters={'item_code': item_code},
#         fields=['valuation_rate'],
#         order_by='posting_date DESC, posting_time DESC',
#         limit=1  # Limit to one record, which is the latest
#     )

#     if entries:
#         results = entries[0].get('valuation_rate')

#     return results


# @frappe.whitelist()
# def fetch_item_data(item_code):
#     valuation_rate = frappe.db.get_value('stock_ledger_entry', {'item_code': item_code}, 'valuation_rate')
#     price_list_rate = frappe.db.get_value('Item Price', {'item_code': item_code, 'price_list': ['in', ['Cost', 'Selling Price 1', 'Selling Price 2']]}, 'price_list_rate')
#     return {'valuation_rate': valuation_rate, 'price_list_rate': price_list_rate}

# from frappe.model.document import Document

# class ItemPrices(Document):
#     def on_update(self):
#         # Fetch and update data from stock ledger entry
#         for row in self.get("item_prices_table"):
#             if row.item_code:
#                 stock_ledger = frappe.db.sql("""
#                     SELECT valuation_rate 
#                     FROM `tabStock Ledger Entry` 
#                     WHERE item_code = %s 
#                     ORDER BY posting_date DESC 
#                     LIMIT 1
#                 """, row.item_code, as_dict=True)
                
#                 if stock_ledger:
#                     row.valuation_rate = stock_ledger[0].valuation_rate

        # Update Item Price records
        # for row in self.get("item_prices_table"):
        #     if row.price_list == "Cost":
        #         self.cost_price = row.price_list_rate
        #     elif row.price_list == "Selling Price 1":
        #         self.selling_price_1 = row.price_list_rate
        #     elif row.price_list == "Selling Price 2":
        #         self.selling_price_2 = row.price_list_rate

@frappe.whitelist()
def valuation_rate(item_code):
    results = None  # Initialize results to None
    entries = frappe.get_all(
        'Stock Ledger Entry',
        filters={'item_code': item_code},
        fields=['valuation_rate'],
        order_by='posting_date DESC, posting_time DESC',
        limit=1  # Limit to one record, which is the latest
    )

    if entries:
        results = entries[0].get('valuation_rate')

    return results

@frappe.whitelist()
def cost(item_code):
    results = False
    exst = frappe.db.exists('Item Price', {"item_code": f'{item_code}', "price_list": "Cost Price"})
    if exst:
        item_price = frappe.get_last_doc('Item Price', {"item_code": f'{item_code}', "price_list": "Cost Price"})
        results = item_price.price_list_rate
    return results

@frappe.whitelist()
def selling_price_1(item_code):
    results = False
    exst = frappe.db.exists('Item Price', {"item_code": f'{item_code}', "price_list": "Selling Price 1"})
    if exst:
        item_price = frappe.get_last_doc('Item Price', {"item_code": f'{item_code}', "price_list": "Selling Price 1"})
        results = item_price.price_list_rate
    return results

@frappe.whitelist()
def selling_price_2(item_code):
    results = False
    exst = frappe.db.exists('Item Price', {"item_code": f'{item_code}', "price_list": "Selling Price 2"})
    if exst:
        item_price = frappe.get_last_doc('Item Price', {"item_code": f'{item_code}', "price_list": "Selling Price 2"})
        results = item_price.price_list_rate
    return results

# @frappe.whitelist()
# def update_item_price(cost_center):
# 	cost_center_doc = frappe.get_doc('Cost Center', cost_center)
# 	item_code = cost_center_doc.item_code
# 	cost = cost_center_doc.cost
# 	item_price = frappe.get_last_doc('Item Price', {"item_code": item_code, "price_list": "Cost Price"})
# 	item_price.price_list_rate = cost
# 	item_price.save()

@frappe.whitelist()
def update_item_price(item_code, new_cost):
    # Update the Item Price document with the new cost
    item_price = frappe.get_doc('Item Price', {"item_code": item_code, "price_list": "Cost Price"})
    item_price.price_list_rate = new_cost
    item_price.save()