from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Twilio configurations
twilio_account_sid = 'AC279242798af6f7b8eb68bf456fabd420'
twilio_auth_token = 'e64fcd2b58091958cf2e8c31e5dbd165'
twilio_phone_number = '+14849928592'
receiver_phone_number = '+918005757690'

# Email configurations
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Example for Gmail
sender_email = 'bkbiet.shagunkaler@gmail.com'
sender_password = '20ebkai022'

# WhatsApp configurations
driver_path = 'path_to_chromedriver'

# Function to send SMS messages using Twilio
def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=receiver_phone_number
    )
    print("SMS message sent successfully.")

# Function to send emails using SMTP
def send_email(subject, message, receiver_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Please check your email credentials.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {str(e)}")

# Usage
email_subject = 'Test Email'
email_message = 'Hello, this is a test email.'
receiver_email = 'recipient@example.com'

send_email(email_subject, email_message, receiver_email)


# Function to send WhatsApp messages using Selenium
def send_whatsapp(message):
    driver = webdriver.Chrome(driver_path)
    driver.get("https://web.whatsapp.com")
    input("Press Enter after scanning the QR code...")
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(receiver_phone_number + Keys.ENTER)
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message + Keys.ENTER)
    driver.quit()
    print("WhatsApp message sent successfully.")
# Example usage
sms_message = "Hello from Python!"
email_subject = "Greetings"
email_message = "Hello from Python!"
whatsapp_message = "Hello from Python!"
receiver_email='shagunkaler01@gmail.com'

# Sending SMS
send_sms(sms_message)

# Sending Email
send_email(email_subject, email_message, receiver_email)

# Sending WhatsApp message
send_whatsapp(whatsapp_message)
