# core/qr_utils.py

import qrcode

def generate_qr(data: str):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

