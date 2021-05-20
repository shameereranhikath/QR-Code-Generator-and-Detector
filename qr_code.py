# import qr code for generating
import qrcode

# here we are generating a QR code for the YouTube link "https://www.youtube.com/watch?v=3qquQqWGLJY"
img = qrcode.make("https://www.youtube.com/watch?v=3qquQqWGLJY")

# saving the qrcode image file to the directory
img.save("football.jpg")