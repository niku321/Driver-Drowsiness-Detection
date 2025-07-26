import smtplib
from email.message import EmailMessage
import requests
import json

# Email setup
Sender_Email = "dymmy27@gmail.com"
Reciever_Email = "saritasadgir1@gmail.com"
Password = 'wnkncgxdhyfparuh'
newMessage = EmailMessage()    # Creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Driver Safety"  # Defining email subject
newMessage['From'] = Sender_Email  # Defining sender email
newMessage['To'] = Reciever_Email  # Defining receiver email

# Get location using IPStack API
location_req_url = 'http://api.ipstack.com/103.51.95.183?access_key=a7003977af457525708100fca423928d'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)

lat = location_obj.get('latitude', 'N/A')  # Default to 'N/A' if latitude is not found
lon = location_obj.get('longitude', 'N/A')  # Default to 'N/A' if longitude is not found
city = location_obj.get('city', 'Unknown')  # Get city name, default to 'Unknown'

# Log latitude, longitude, and city to console
print(f"Latitude: {lat}")
print(f"Longitude: {lon}")
print(f"City: {city}")

# Add location and city to the email content
email_body = (
    "Hi,\n\n"
    "Driver drowsiness detected. Please help me urgently.\n\n"
    f"Location details:\n"
    f"Latitude: {lat}\n"
    f"Longitude: {lon}\n"
    f"City: {city}\n\n"
    "Best regards,\n"
    "Your Safety App"
)
newMessage.set_content(email_body)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)
    smtp.send_message(newMessage)
    print("Mail sent successfully")


    



