#user upi id as input
# Function to accept UPI payment
# This function generates a QR code for UPI payment using the provided UPI ID.
# save the QR code as an image file.
# Required libraries: qrcode, PIL (Pillow)
import qrcode
from PIL import Image

upi_id = input("Enter your UPI ID (e.g., example@upi): ")

# upi://pay?pa=UPI_ID&pn=YourName&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Generate QR code for PhonePe
phonepe_qr = qrcode.make(phonepe_url)
# Generate QR code for Paytm
paytm_qr = qrcode.make(paytm_url)
# Generate QR code for Google Pay
google_qr = qrcode.make(google_url)

# Save the QR codes as image files
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_qr.save("google_qr.png")

print("QR codes generated and saved successfully!")

# Display the generated QR codes (using PIL)
phonepe_qr.show()
paytm_qr.show()
google_qr.show()