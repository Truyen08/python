#  python -m ensurepip --upgrade
# pip install qrcode
# pip install pillow

import qrcode
from PIL import Image

url = "https://www.vku.udn.vn"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=8, border=5)
qr.add_data(url)
qr.make(fit=True)

# Create an image with logo
image = qr.make_image(fill_color="black", back_color="pink").convert("RGB")

logo = Image.open("logovku.png")  # Add logo to the QR code
logo_size = image.size[0] // 4
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# If logo has alpha channel, use mask
mask = logo.split()[3] if logo.mode == "RGBA" else None
pos = ((image.size[0] - logo.size[0]) // 2, (image.size[1] - logo.size[1]) // 2)
image.paste(logo, pos, mask=mask)
image.save("qr_code.png")  # Save the image
image.show()  # Open the image