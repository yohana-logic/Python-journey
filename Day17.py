import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)

file_name = "qrcode.png"
qr.save(file_name)

print(f"QR Code saved as {file_name}")