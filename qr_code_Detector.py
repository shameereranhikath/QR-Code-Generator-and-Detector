# importing open CV module
import cv2
# Reading the QR Code image file
data, retval, straight_qrcode = cv2.QRCodeDetector().detectAndDecode(cv2.imread('football.jpg'))

# will return the data associated with the QR Code in the image format
print(data)
