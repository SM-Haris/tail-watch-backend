import qrcode
import base64
from io import BytesIO

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr_data = "http://localhost:3000/track/hello"
qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
buffered = BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()
print("QR_Code Image: ", img_str)
