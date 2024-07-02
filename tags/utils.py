from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
import qrcode
import base64
from io import BytesIO


def GenerateQrCodeImage(tag_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_data = f"http://localhost:3000/track/{tag_id}"

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return img_str


def ExtractUserFromRequest(request):
    if request.user.is_superuser:
        return request.user

    jwt_auth = JWTAuthentication()

    try:
        auth_result = jwt_auth.authenticate(request)

        if auth_result is None:
            user = None
        else:
            user, _ = auth_result

        return user
    except AuthenticationFailed:
        return None
