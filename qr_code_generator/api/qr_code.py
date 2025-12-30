import qrcode
import os
import frappe
from frappe import _
import qrcode.image.svg
from io import BytesIO
import base64
from .purchase_order import get_po_items
from frappe.utils import get_url


@frappe.whitelist(allow_guest = True)
def gen_qr(data):
    user = frappe.session.user
    # if user == "Guest":
    #     return {
    #         "redirect_url": "/login?redirect-to=/verify-po?po=PUR-ORD-2025-00001",
    #     }
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    site_config = frappe.get_site_config()
    domains = site_config.get("domains", [])
    if domains:
        BASE_URL = f"https://{domains[0]}"
    else:
        BASE_URL = "http://localhost:8000" 

    url = f"{BASE_URL}/app/purchase-order/{data}"

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    qr_html =f"data:image/png;base64,{img_str}"
    # frappe.db.set_value("Purchase Order", data, "custom_qr_code", qr_html)

    return qr_html
