import frappe

@frappe.whitelist()
def get_po_items(po_name):
    supply = {}
    po = frappe.get_doc("Purchase Order", po_name)
    # return [{"item": i.item_code, "qty": i.qty, "total": i.amount} for i in po.items]
    n  = 1
    for i in po.items:
        supply[n] = {
        "item": i.item_code,
        "qty": i.qty,
        "total": i.amount
        }
        n += 1
        

    return supply