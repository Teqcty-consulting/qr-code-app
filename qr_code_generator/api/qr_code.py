import qrcode
import frappe
from frappe import _
import qrcode.image.svg
from io import BytesIO
import base64
from .purchase_order import get_po_items


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
    url = f"https://sge.teqcty.com/app/purchase-order/{data}"
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return f"data:image/png;base64,{img_str}"
