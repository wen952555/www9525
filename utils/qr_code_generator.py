import qrcode
from PIL import Image

def generate_qr_code(data: str) -> Image.Image:
    """
    Generate a QR code image from the provided data.
    :param data: The data to encode in the QR code.
    :return: A PIL Image object containing the QR code.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")