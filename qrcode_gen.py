import qrcode
from PIL import Image

# QR Code info
data = "https://github.com/Jingyi-li/gen_qrcode"

qr = qrcode.QRCode(
    version=3,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # for insert logo
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# generate qr code
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# insert logo
logo_path = 'images.png'  
logo = Image.open(logo_path)

qr_width, qr_height = qr_img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# insert for position
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# save qrcode
qr_img.save('qrcode_with_logo.png')
# qr_img.show()
