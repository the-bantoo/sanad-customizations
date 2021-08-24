import frappe
from frappe import _

@frappe.whitelist()
def check_stock(code, name):
    wish = frappe.get_doc('Wish', name)
    l = []

    item_warehouse = frappe.db.sql("select warehouse from `tabBin` where item_code = %s", (code), as_dict = 1)
    for key in item_warehouse:
        warehouse = key['warehouse']
        bin = frappe.db.sql("select actual_qty from `tabBin` where item_code = %s and warehouse = %s", (code, warehouse), as_dict = 1)
        qty = (bin[0]['actual_qty'])
        l.append(qty)

    if 0 not in l or len(len) == 0:
        wish.stock_qty = 'In Stock'
        wish.save()
    else:
        wish.stock_qty = 'Not In Stock'
        wish.save()